from peewee import PostgresqlDatabase

DATABASE = {
    'name': 'lmsdb',
    'user': 'librarian',
    'password': '123456',
    'host': 'localhost',
    'port': 5432
}

db = PostgresqlDatabase(
    DATABASE['name'], 
    user=DATABASE['user'], 
    password=DATABASE['password'], 
    host=DATABASE['host'], 
    port=DATABASE['port']
)


