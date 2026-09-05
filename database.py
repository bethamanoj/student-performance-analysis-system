import mysql.connector as connector
from config import db_config
def get_connection():
    try:
        return connector.connection(**db_config)
    except connector.Error as error:
        print('Database connection error:',error)
        return None
    