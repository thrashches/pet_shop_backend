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