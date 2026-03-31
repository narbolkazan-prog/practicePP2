import psycopg2
from config import load_config

def connect():
    conn = psycopg2.connect(**load_config())
    return conn