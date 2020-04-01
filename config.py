import os

from dotenv import load_dotenv


load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
     SECRET_KEY = os.getenv('SECRET_KEY') or 'very_hard_key'
     DEBUG = True
#     print(f'From dotenv: {os.getenv("DATABASE_URL")}')
#    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
#     'sqlite:///' + os.path.join(basedir, 'prog.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     POSTGRES_USER = os.getenv('POSTGRES_USER')
#     POSTGRES_PW = os.getenv('POSTGRES_PW')
#     POSTGRES_URL = os.getenv('POSTGRES_URL')
#     POSTGRES_DB = os.getenv('POSTGRES_DB')
     POSTGRES_DB = os.getenv('DATABASE_URL')
     if not (POSTGRES_DB and POSTGRES_PW and POSTGRES_URL and POSTGRES_USER):
         print('ENV ERROR')
     SQLALCHEMY_DATABASE_URI = \
     f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'
     SQLALCHEMY_TRACK_MODIFICATIONS = False
     LOG_TO_STDOUT = os.getenv('LOG_TO_STDOUT')
