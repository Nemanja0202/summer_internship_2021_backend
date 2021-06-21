import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gjaspdfladsjifoaskasjpodifja'

    ENV_TYPE = "Development"
    DB_NAME = "airvironment_db"
    DB_USER = "nemanja_praksa"
    DB_PASSWORD = "test123"
    DB_HOST = "127.0.0.1"
    DB_PORT = 5432

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
