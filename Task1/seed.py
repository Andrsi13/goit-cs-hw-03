# seed.py
import psycopg2
from faker import Faker

# Підключення до бази даних PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Ініціалізація Faker
faker = Faker()

# Вставка початкових значень у таблицю status
cur.execute("INSERT INTO status (name) VALUES ('new'), ('in progress'), ('completed');")

# Вставка випадкових користувачів
for _ in range(10):
    fullname = faker.name()
    email = faker.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Отримання ID статусів
cur.execute("SELECT id FROM status")
status_ids = [row[0] for row in cur.fetchall()]

# Отримання ID користувачів
cur.execute("SELECT id FROM users")
user_ids = [row[0] for row in cur.fetchall()]

# Вставка випадкових завдань
for _ in range(20):
    title = faker.sentence(nb_words=6)
    description = faker.text()
    status_id = faker.random.choice(status_ids)
    user_id = faker.random.choice(user_ids)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", 
                (title, description, status_id, user_id))

# Збереження змін і закриття з'єднання
conn.commit()
cur.close()
conn.close()
