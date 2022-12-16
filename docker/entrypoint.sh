#!/usr/bin/env sh

set -e

# Ожидаем запуска postgres
dockerize -wait tcp://${PSQL_HOST}:${PSQL_PORT}

# Миграция и синхронизация
./manage.py migrate --noinput
./manage.py insert_data

# Запуск команды
./manage.py runserver 0.0.0.0:${APP_PORT}