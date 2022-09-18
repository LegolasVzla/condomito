import os
from configparser import RawConfigParser

BASE_DIR = os.getcwd()

# Loading settings.ini file with PostgreSQL database credentials
config = RawConfigParser()
config.read(BASE_DIR + '/settings.ini')

DB_NAME = config.get('postgresdbConf', 'DB_NAME')
DB_USER = config.get('postgresdbConf', 'DB_USER')
DB_PASSWORD = config.get('postgresdbConf', 'DB_PASS')
DB_HOST = config.get('postgresdbConf', 'DB_HOST')
DB_PORT = config.get('postgresdbConf', 'DB_PORT')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
