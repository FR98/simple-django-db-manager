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
    * Put the files outside the folder simple-django-db-manager
      ```txt
      your-django-project/
         your-django-project/
         manage.py
         credentials.py
         load_data.py
         README.md
      ```

* Modify /your-django-project/credentials.py
   * Read instructions inside credentials.py

* Add this lines
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

* Create project
  ```shell
  $ django-admin startproject your-django-project
  ```
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
* Use Python Environment!
  ```shell
  $ sudo apt install python3-env
  $ python3 -m venv venv
  $ source venv/bin/activate
  $ deactivate
  ```

* Use ipython 
  ```shell
  $ pip install ipython
  ```
    
* Use React-Redux with your django project!
  ```shell
  $ npx create-react-app your-react
  $ yarn add react-redux
  $ yarn add redux
  $ yarn add redux-saga
  ```
    
    Usefull to know
  ```shell
  $ yarn add uuid
  $ yarn add lodash
  $ yarn add express
  $ yarn add react-router
  ```
