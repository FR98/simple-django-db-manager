
# Author: Francisco Rosal 
# GitHub: https://github.com/FR98
# Repo: https://github.com/FR98/simple-django-db-manager

# Clone this repo inside your django project :)

import os
import credentials
import psycopg2     # Need help? https://www.psycopg.org/

host = credentials.DEVELOPMENT_DATABASE['HOST']
dbname = credentials.DEVELOPMENT_DATABASE['NAME']
user = credentials.DEVELOPMENT_DATABASE['USER']
password = credentials.DEVELOPMENT_DATABASE['PASSWORD']
port = credentials.DEVELOPMENT_DATABASE['PORT']
conndb = credentials.DEVELOPMENT_DATABASE['CONNECTION']

def reset_DB():
  print("\n"*100)
  input('Please disconnect any connection to the db and then press enter... ')

  conn = psycopg2.connect(
    host = host,
    dbname = conndb,
    user = user,
    password = password,
    port = port
  )
  
  conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
  cursor = conn.cursor()
  
  sure = input('Are you sure? You are going to delete all [y/n]... ')
  if sure == 'y':
      cursor.execute("DROP DATABASE IF EXISTS {dbname}".format(dbname=dbname))
      cursor.execute("CREATE DATABASE {dbname}".format(dbname=dbname))
      print('\n -- Reset database completed!')
  else:
      print('\n -- Reset database canceled :)')

def load_data():
  reset = input('Maybe you would like to reset the db first [y/n]... ')
  if reset == 'y':
      reset_DB()
  
  input("Press enter to load initial database...")
  dbDump = input("Enter the name of the sql dump file (with extension): \n\t- ")

  try:
      file = open(dbDump, "r")

      print("Restoring data...")
      print("\t{db} < {dump}".format(
        db = dbname,
        dump = dbDump
      ))

      os.system("psql -h {host} -U {user} -v --disable-triggers --set ON_ERROR_STOP=on {db} < {dump}".format(
        host = host,
        user = user,
        db = dbname,
        dump = dbDump
      ))

      print("~ " * 75)
      option = input("Do you want to make migrations? [y/n]... ")
      if option == 'y':
          migrations()
      print("Data loaded successfully!")
  except IOError:
      print("There is no file named {dump}!".format(dump = dbDump))
  except:
      print("There is an E.N.I. \n\t (Error Not Indentified)")

def migrations():
    print('Loading data structure...')
    print("~ " * 75)
    os.system("python manage.py makemigrations")
    print("~ " * 75)
    os.system("python manage.py migrate --fake-initial")
    print("~ " * 75)
    print(" - Migrations Done!")

def menu():
    return """
          Menu:
      1. Create or Reset DB
      2. Load Initial Data
      3. Migrations
      4. Exit
    """

continuar = True
while continuar:
  print(menu())
  opcion = input("Select an option: ")
  if opcion == '1':
      reset_DB()
  elif opcion == '2':
      load_data()
  elif opcion == '3':
      migrations()
  elif opcion == '4':
      continuar = False
      print("Bye bye")
      print("Credits: https://github.com/FR98")
  else:
      print('Invalid option')
