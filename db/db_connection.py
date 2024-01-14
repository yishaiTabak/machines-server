import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
DATABASE_NAME = os.environ.get('DATABASE_NAME')

connection = psycopg2.connect(host=DATABASE_HOST, database=DATABASE_NAME, port=DATABASE_PORT,
                              user=DATABASE_USER, password=DATABASE_PASSWORD)