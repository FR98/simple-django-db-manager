
# IMPORTANT
# Add this file to your .gitignore if you are working in a team
# or if you dont want others to see this credentials

# Replace with your own info
DEVELOPMENT_DATABASE = {
    'NAME': 'dbname_dev_db',
    'USER': 'your_user',
    'PASSWORD': 'your_password',
    'HOST': 'your_host',
    'PORT': 'your_port',
    'CONNECTION': 'your_connection_db', # This is for connect to postgres and delete your working db to reset
}

# If you are using postgresql probably will be like...

EXAMPLE_DATABASE = {
    'NAME': 'dbname_dev_db',
    'USER': 'postgres',
    'PASSWORD': 'your_password',
    'HOST': 'localhost',
    'PORT': '5432',
    'CONNECTION': 'postgres',
}

# Feel free to add more credentials for diff env :)
