# simple-django-db-manager
Simple db manager for Django projects
##### Author: Francisco Rosal 
##### GitHub: https://github.com/FR98

## To use this repo

* [Install psycopg2](https://www.psycopg.org/)
    * Install and test installation
  ```shell
  $ pip install psycopg2
  $ python -c "import psycopg2" --verbose
  ```

* Clone this repo inside your django project
    (Tip: next to manage.py)

* Modify /your-django-project/credentials.py

* To reset db and load data
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
