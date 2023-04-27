# API_FINAL_YATUBE 

API_Final - законченная версия API для yatube. 

Стек: Python 3.7, Django Rest Framework, SQLite

# Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:Avdeeva23/api_final_yatube.git
```

- Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/bin/activate
```
- Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Выполнить миграции:
```
python manage.py migrate
```
- Запустить проект:
```
python manage.py runserver
```
