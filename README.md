# simple-django-db-manager

##### Author: Francisco Rosal 
##### GitHub: https://github.com/FR98
Simple db manager for Django projects

## To use this repo

* [Install psycopg2](https://www.psycopg.org/)
    * Install and test installation
  ```shell
  $ pip install psycopg2
  $ python -c "import psycopg2" --verbose
  ```

* Clone this repo inside your django project
    * Tip: next to manage.py
      ```txt
      your-django-project/
         your-django-project/
         manage.py
         credentials.py
         load_data.py
      ```

* Modify /your-django-project/credentials.py
   * Read instructions inside credentials.py

* Add this lines on /your-django-project/settings.py
    * Below import os
  ```python
  import os
  import sys
  sys.path.insert(1, '../')
  import credentials
  ```
    * Replace default in DATABASES
  ```python
  'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': credentials.DEVELOPMENT_DATABASE['NAME'],
      'USER': credentials.DEVELOPMENT_DATABASE['USER'],
      'PASSWORD': credentials.DEVELOPMENT_DATABASE['PASSWORD'],
      'HOST': credentials.DEVELOPMENT_DATABASE['HOST'],
      'PORT': credentials.DEVELOPMENT_DATABASE['PORT'],
  }
  ```
    * Recommendation: Add too...

  ```python
  LOGIN_URL = "/"
  LOGIN_REDIRECT_URL = "home"
  LOGOUT_REDIRECT_URL = "/"
  ```

* To reset db and load data run
  ```shell
  $ python load_data.py
  ```

## Tips for start your project

* [Instalar Python](https://www.python.org/)
* [Instalar Postgres](https://www.postgresql.org/)
* Instalar Python Environment
    ```shell
    $ sudo apt install python3-env
    ```
* Crear, activar y desactivar python env
    ```shell
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
* [Instalar Django](https://docs.djangoproject.com/en/3.0/topics/install/)
    ```shell
    $ python -m pip install Django
    ```
* [Instalar psycopg2](https://www.psycopg.org/)
    * Instalar y comprobar instalación
    ```shell
    $ pip install psycopg2
    $ python -c "import psycopg2" --verbose
    ```
* Instalar ipython 
    ```shell
    $ pip install ipython
    ```
* Create project
  ```shell
  $ django-admin startproject your-django-project
  ```
* Configure database 
* Run Server
  ```shell
  $ python manage.py runserver
  ```
* Create an app
  ```shell
  $ python manage.py startapp myapp
  ```
* Open shell
  ```shell
  $ python manage.py shell
  ```
    
 ## You would like to know...
* Requirements
  ```shell
  $ pip freeze >> requirements.txt
  $ pip install -r requirements.txt
  ```
* Conexión a Interfaz Postgres
    ```shell
    $ psql -h localhost -U postgres -W
    ```

## Make an API
* To do list:
   * Apps
   * Models
   * [Django RestFramework](https://www.django-rest-framework.org/)
   * Serializers
   * ViewSets
   * Routers and Urls
   * Custom Actions
   * [JWT Authentication and Authorization](https://jpadilla.github.io/django-rest-framework-jwt/)
   * Object Level Permissions
      * pip install django-guardian
      * [Permissions Manager](https://github.com/samuelchvez/django-rest-framework-viewset-permissions)

    
## Use React-Redux with your django project!
* Create React App  
  ```shell
  $ npx create-react-app your-react
  $ yarn add react-redux
  $ yarn add redux
  $ yarn add redux-saga
  $ yarn add react-router-dom
  ```
    
* Usefull to know
  ```shell
  $ yarn add uuid
  $ yarn add lodash
  $ yarn add express
  ```
* To do list:
   * State
   * Types and Actions Creators
   * Reducers
   * Global Reducer
   * Selectors
   * Global Selector
   * Dummy Components
   * Smart Components
