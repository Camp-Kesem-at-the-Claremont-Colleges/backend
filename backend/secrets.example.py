""" The secret file for all your secret info. Rename this to secrets.py! """
# don't worry about production key for now
PRODUCTION_KEY = 'super_secret_key'

# use to change db settings
is_production = False

# information from mysql setup goes here
DEV_HOST = 'genna.czvta9z7dure.us-east-2.rds.amazonaws.com'
DEV_DB = 'cknewsletter'
DEV_USER = 'genna'
DEV_PASSWORD = 'buttmunch123'

LOCAL_HOST = 'localhost'
LOCAL_DB = 'cknewsletter'
LOCAL_USER = 'root'
LOCAL_PASSWORD = ''

if is_production:
    DATABASE_HOST =  DEV_HOST 
    DATABASE_NAME = DEV_DB
    DATABASE_USER = DEV_USER
    DATABSE_PASSWORD = DEV_PASSWORD
else:
    DATABASE_HOST =  LOCAL_HOST 
    DATABASE_NAME = LOCAL_DB
    DATABASE_USER = LOCAL_USER
    DATABSE_PASSWORD = LOCAL_PASSWORD
