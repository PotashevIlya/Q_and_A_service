# bash-скрипт, выполняющий команды при запуске приложения в Docker

# На всякий случай ждём запуска Postgres
echo "Waiting for PostgreSQL to start..."
sleep 20

# Применяем миграции
alembic upgrade head
sleep 10

# Запускаем uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000
