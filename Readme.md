# Проект интернет магазина

## Варианты запуска:

### docker-compose

```bash
cd infra
docker compose up
```

### virtualenv

```bash
python3.10 -m venv venv
. venv/bin/activate
pip install -r shop_backend/requirements.txt

cd shop_backend
python manage.py runserver
```

## Оформление коммитов

В сообщении коммита указываем название таски в проектах и кратко то что сделано в коммите. Например:
```
Авторизация пользователей через почту
Добавлено обязательное поле email
```
