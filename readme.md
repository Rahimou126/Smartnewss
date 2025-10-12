# Smartnewss

Smartnewss is a Django application for managing news. This guide explains how to install and configure the project
locally.

---

## Prerequisites

- Python 3.10+
- pip
- Git
- PostgreSQL / MySQL / SQLite database according to configuration

## 1. Clone the project

```bash
git clone git@github.com:Rahimou126/Smartnewss.git
cd Smartnewss
```

---

## 2. Create and activate a virtual environment

### On Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

---

## 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. Configure the database

1. Check `settings.py` for database configuration.
2. Create the database if needed (PostgreSQL example):

```sql
CREATE DATABASE smartnewss_db;
CREATE USER smartuser WITH PASSWORD 'motdepasse';
GRANT ALL PRIVILEGES ON DATABASE smartnewss_db TO smartuser;
```

3. Apply migrations:

```bash
python manage.py migrate
```

---

## 5. Create a superuser

```bash
python manage.py createsuperuser
```

---

## 6. Load fixtures

```bash
python manage.py loaddata news/fixtures/news.json
```

---

## 7. Run the server

```bash
python manage.py runserver
```

---

## 8. Additional notes

- To deactivate the virtual environment: `deactivate`
- To install new dependencies:
  ```bash
  pip install nom_package
  pip freeze > requirements.txt
  ```

