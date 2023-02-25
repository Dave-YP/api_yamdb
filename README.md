![](./api_yamdb/static/logo.png)
## Проект «Проект YaMDb»
1. [Описание проекта](#описание-проекта)
2. [Ресурсы API YaMDb](#ресурсы-api-yamdb)
3. [Как запустить проект](#как-запустить-проект)
4. [Примеры запросов](#примеры-запросов)
5. [Стек технологий](#стек-технологий)
6. [Авторы](#авторы)

## Описание проекта:

Проект YaMDb собирает отзывы пользователей на различные произведения. 

## Ресурсы API YaMDb:

- Ресурс auth: аутентификация.
- Ресурс users: пользователи.
- Ресурс titles: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
- Ресурс categories: категории (типы) произведений («Фильмы», «Книги», «Музыка»). Одно произведение может быть привязано только к одной категории.
- Ресурс genres: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс reviews: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс comments: комментарии к отзывам. Комментарий привязан к определённому отзыву.

Каждый ресурс описан в документации: указаны эндпоинты (адреса, по которым можно сделать запрос), разрешённые типы запросов, права доступа и дополнительные параметры, когда это необходимо.

## Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/pavelkor91/api_yamdb.git
```

```
cd api_yamdb
```

2. Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
Windows: source venv/Scripts/activate
Linux: source venv/bin/activate
```

3. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. Выполнить миграции:

```
Windows:
python manage.py makemigrations reviews
python manage.py makemigrations users
python manage.py migrate

Linux:
python3 manage.py makemigrations reviews
python3 manage.py makemigrations users
python3 manage.py migrate

Добавить данные из csv: 
python manage.py load_csv_data
python manage.py load_genre_title
```

Запустить проект:

```
python manage.py runserver
```
## Пример запросов:

Все примеры доступны в документации:
```
http://127.0.0.1:8000/redoc/
```
## Стек технологий:
- Django REST Framework
- библиотека django-filter
- библиотека Simple JWT
- git
- SQLite3
## Авторы:

- [pavelkor91](https://github.com/pavelkor91)  
- [Dave-YP](https://github.com/Dave-YP)
- [Xaliy](https://github.com/Xaliy)
