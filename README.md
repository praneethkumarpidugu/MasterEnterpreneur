# MASTER ENTERPRENEUR PROGRAM CONTENT MEMBERSHIP SITE

## ![logo](http://res.cloudinary.com/dnwvzsw7s/image/upload/v1456094192/Screen_Shot_2016-02-21_at_5.17.44_pm_gtqhrs.png)
## GIF


# Site is currently live in the production heroku server
[https://afternoon-lowlands-85210.herokuapp.com/](https://afternoon-lowlands-85210.herokuapp.com/)

```shell
source bin/activate && cd src && python manage.py runserver
```

## Loading static files
```shell
python manage.py collectstatic
```
## deactivate the virtual environment
```shell
deactivate
```
## Run the  Development Server

```shell
python manage.py runserver --port-number
```

## If you make any changes to models.py

```shell
python manage.py makemigrations
python manage.py migrate
```

## if you would like to clear the database
### delete sqlite3 db file
### make migrations and migrate again
