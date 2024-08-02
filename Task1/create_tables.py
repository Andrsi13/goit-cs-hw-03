# create_tables.py
import psycopg2

# Підключення до бази даних PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Створення таблиці users
cur.execute('''
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    );
''')

# Створення таблиці status
cur.execute('''
    CREATE TABLE status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    );
''')

# Створення таблиці tasks
cur.execute('''
    CREATE TABLE tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER REFERENCES status(id),
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
    );
''')

# Збереження змін і закриття з'єднання
conn.commit()
cur.close()
conn.close()
