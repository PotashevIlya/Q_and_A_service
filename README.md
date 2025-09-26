# Сервис для вопросов и ответов

## Описание сервиса
Сервис позволяет публиковать вопросы и ответы на них. 

## Как запустить сервис с помощью Docker:
1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/PotashevIlya/Q_and_A_service
```
```
cd Q_and_A_service
```
2. Создать .env файл в корневой директории и заполнить его по образцу .env.example
3. Выполнить команду
```
docker compose up -d
```
## Как запустить сервис локально:
1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/PotashevIlya/Q_and_A_service
```
```
cd Q_and_A_service
```
2. Поднять базу PosgreSQL.
3. Создать .env файл в корневой директории и заполнить его по образцу .env.example
4. Создать и активировать виртуальное окружение.
```
python -m venv .venv
```
```
source .venv/Scripts/activate
```
5. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
6. Выполнить миграции.
```
alembic upgrade head
```
7. Запустить сервер.
```
uvicorn app.main:app
```

## Тесты
Для запуска тестов выполните команду pytest, находясь в корневой директории проекта при локальном запуске.

## Документация:
Доступные эндпоинты будут доступны по адресу /docs после запуска проекта.

## Технологический стек:
Python, FastAPI, Postgres, Alembic, SQLAlchemy, Pydantic, Pytest.

