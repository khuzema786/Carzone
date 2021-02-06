# Tech Mahindra Task 1 Pre-requisites – Learn Django Web Framework
![Project](https://github.com/khuzema786/Carzone/blob/master/carzone.gif)

## To get started
- Clone the repository
- Setup a virtual environment and activate it
    ```
    Pip install virtualenv
    python -m venv env
    .\env\Scripts\activate
    ```
- Download and install postgress and create an .env file with following field values
    ```
    SECRET_KEY = '243p#@408q#7jio7aq=#)*thtyq*9amb%$sy!%1ezpu+m8_rv('
    DEVELOPMENT = 'True'
    EMAIL_INTEGRATION = 'False'
    EMAIL_HOST = '<Email host provider>'
    EMAIL_PORT = <Email port number>
    EMAIL_HOST_USER = '<Your smtp associated email>'
    EMAIL_HOST_PASSWORD = '<Your smtp associated password>'
    POSTGRES_DB = 'carzone_db'
    POSTGRES_USER = 'postgres'
    POSTGRES_PASS = 'root'
    POSTGRES_HOST = 'localhost'
    ```
- Install the dependencies
    ```
    pip install requirements.txt
    ```
- Fill up rhe database with sample data
    ```
    python manage.py makemigrations
    python manage.py loaddata project_dump.json
    ```
- Starting the development server on localhost:8000
    ```
    python manage.py runserver 127.0.0.1:8000
    ```

# Some Included Functionalities
- PostgreSQL Database Setup
- Django Static Files & Media Files
- Django Admin Customisation
- Database Schema, Models and Migrations
- Implementing RichText Editor & Multi-Select Fields on Admin Backend
- Fetching Database Objects
- Pagination
- Search Functionality
- User Authentication
- Login with Facebook & Login with Google
- Send Emails  

## Some Important commands
### Virtual Environment Setup
```
Pip install virtualenv
python -m venv env
.\env\Scripts\activate
```

### Install Django & Start the project
```
Python –m Pip install django
django-admin startproject carzone
python manage.py startapp pages
python manage.py runserver
```

### To Add Static Files From STATIC_FILES_DIR to STATIC_ROOT
```
python manage.py collectstatic
For .env
pip install python-decouple
```

### For postgres sql
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### For Production
```
python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth Permission --indent 4 > project_dump.json
pip install gunicorn psycopg2-binary
pip install dj-database-url
pip install whitenoise
pip freeze > requirements.txt
```

### For Heroku
```
git add .
git commit –m “production”
git push heroku master
heroku open
heroku run python manage.py loaddata project_dump.json
Run a bash inside heroku
heroku login
heroku run bash -a APPNAME
$ cd app
```

### Website Themes
```
http://www.themelock.com/
https://www.themes24x7.com/xstore-v7-0-responsive-multi-purpose-woocommerce-wordpress-theme/
```

