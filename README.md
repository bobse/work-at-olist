# Work at Olist (Project)
## Project Description:
This project is built on Python and Django Rest Framework, it provides a REST API for a library to store book and authors data.

It uses a PostgreSQL Database instead of Sqlite3 because it has a some features which can make the project better with him. For performance reason, while testing, the project uses a Sqlite3 DB.

This project was made following the instructions from the work at olist challenge: https://github.com/olist/work-at-olist

---

## Installation:
- Clone repository:
```
    $ git clone https://github.com/bobse/work-at-olist.git 
```
- Create Virtual Environment, activate it and install requirements:
```
    $ python3 -m venv venv 
    $ source ./venv/bin/activate
    $ pip install -r requirements.txt
```
- Create .env file inside settings folder with secret key:
```
    SECRET_KEY="xxxxxx"
    DATABASE_URL="postgres://postgres:test@localhost:5432/postgres"
```
- Migrate database
```
    $ python manage.py makemigrations --settings=library.settings.development
    $ python manage.py migrate --settings=library.settings.development
```
- Import Authors
```
    $ python manage.py import_authors authors.csv --settings=library.settings.development
```
- Run server (Development Mode)
```
    $ python manage.py runserver --settings=library.settings.development
```
## POSTGRES SETUP (No longer necessary. Done in Django):
Since we have more than a million records for authors for faster search I created a trigram index for authors.
- Trigram Gin Index for Author name Search:
```
CREATE EXTENSION pg_trgm;
```
## Tests:
```
    $ python manage.py test --settings=library.settings.development
```
---
## Api Endpoints:
- /library/authors/
- /library/books/
- /library/docs/


