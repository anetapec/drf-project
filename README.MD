## CREATE VIRTUAL EINVORMENT
```bash
python3 -m venv venv
```
# Active your virtual env
```bash
source venv/bin/activate
```

# INSTALL Django
```bash
pip install django
```

# start project django
```bash
django-admin start-project watchmate .
```
# create app
```bash
python3 manage.py startapp watchlist_app
```

```bash
python3 manage.py runserver
```

# create database
```bash
python manage.py migrate
```
# create user
```bash
python manage.py createsuperuser
```
# when some changes in models.py :
```bash
python manage.py makemigraons

python manage.py migrate

python manage.py runserver
```

# regist your model in admin.py, views, url 

## django rest Api
```bash
pip install djangorestframework
```


