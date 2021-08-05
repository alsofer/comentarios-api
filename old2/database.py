from peewee import *
import os

user = os.getenv('dbuser')
password = os.getenv('dbpassword')
db_name = os.getenv('dbname')
db_host = os.getenv('dbhost')

conn = MySQLDatabase(
    db_name, user=user,
    password=password,
    host=db_host
)

class BaseModel(Model):
    class Meta:
        database = conn