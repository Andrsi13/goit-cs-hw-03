from pymongo import MongoClient
from pymongo.errors import PyMongoError

def get_db_connection():
    try:
        # Замініть <username>, <password>, <cluster-address>, <database> на ваші дані
        uri = "mongodb+srv://Andrsi:20041995aA@cluster0.2j3nyfz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri)
        db = client['cat_database']  # Назва бази даних
        return db
    except PyMongoError as e:
        print(f"Не вдалося підключитися до MongoDB: {e}")
        return None

# Функції для CRUD-операцій
def create_cat(name, age, features):
    db = get_db_connection()
    if db is not None:
        try:
            cats_collection = db['cats']
            new_cat = {
                "name": name,
                "age": age,
                "features": features
            }
            result = cats_collection.insert_one(new_cat)
            print(f"Документ додано з id: {result.inserted_id}")
        except PyMongoError as e:
            print(f"Помилка при додаванні документа: {e}")
    else:
        print("Не вдалося підключитися до бази даних.")

def read_all_cats():
    db = get_db_connection()
    if db is not None:
        try:
            cats_collection = db['cats']
            cats = cats_collection.find()
            for cat in cats:
                print(cat)
        except PyMongoError as e:
            print(f"Помилка при читанні документів: {e}")
    else:
        print("Не вдалося підключитися до бази даних.")

def read_cat_by_name(name):
    db = get_db_connection()
    if db is not None:
        try:
            cats_collection = db['cats']
            cat = cats_collection.find_one({"name": name})
            if cat:
                print(cat)
            else:
                print(f"Кот з ім'ям {name} не знайдено.")
        except PyMongoError as e:
            print(f"Помилка при читанні документа: {e}")
    else:
        print("Не вдалося підключитися до бази даних.")

def update_cat_age(name, new_age):
    db = get_db_connection()
    if db is not None:
        try:
            cats_collection = db['cats']
            result = cats_collection.update_one(
                {"name": name},
                {"$set": {"age": new_age}}
            )
            if result.matched_count > 0:
                print(f"Вік кота {name} оновлено на {new_age} років.")
            else:
                print(f"Кот з ім'ям {name} не знайдено.")
        except PyMongoError as e:
            print(f"Помилка при оновленні документа: {e}")
    else:
        print("Не вдалося підключитися до бази даних.")

def add_feature_to_cat(name, feature):
    db = get_db_connection()
    if db is not None:
        try:
            cats_collection = db['cats']
            result = cats_collection.update_one(
                {"name": name},
                {"$addToSet": {"features": feature}}
            )
            if result.matched_count > 0:
                print(f"Характеристика '{feature}' додана до кота {name}.")
            else:
                print(f"Кот з ім'ям {name} не знайдено.")
        except PyMongoError as e:
            print(f"Помилка при оновленні документа: {e}")
    else:
        print("Не вдалося підключитися до бази даних.")

def delete_cat_by_name(name):
    db = get_db_connection()
    if db is not None:
        try:
            cats_collection = db['cats']
            result = cats_collection.delete_one({"name": name})
            if result.deleted_count > 0:
                print(f"Кот з ім'ям {name} видалено.")
            else:
                print(f"Кот з ім'ям {name} не знайдено.")
        except PyMongoError as e:
            print(f"Помилка при видаленні документа: {e}")
    else:
        print("Не вдалося підключитися до бази даних.")

def delete_all_cats():
    db = get_db_connection()
    if db is not None:
        try:
            cats_collection = db['cats']
            result = cats_collection.delete_many({})
            print(f"Видалено {result.deleted_count} документів.")
        except PyMongoError as e:
            print(f"Помилка при видаленні документів: {e}")
    else:
        print("Не вдалося підключитися до бази даних.")

if __name__ == "__main__":
    # Приклад використання функцій
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    read_all_cats()
    read_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_feature_to_cat("barsik", "любить гратись")
    delete_cat_by_name("barsik")
    delete_all_cats()
