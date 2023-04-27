from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .permissions import AuthorPermission
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)

from posts.models import Group, Post


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.select_related('user')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author')
    serializer_class = PostSerializer
    permission_classes = (AuthorPermission,
                          permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorPermission,
                          permissions.IsAuthenticatedOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.select_related('author')

    def perform_create(self, serializer):
        serializer.save(
            post=self.get_post(),
            author=self.request.user
        )
