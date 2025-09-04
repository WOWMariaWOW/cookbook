
# main.py
import sqlite3
import os

# Путь к базе данных
db_path = 'cookbook.db'

# Проверяем, существует ли файл базы данных
if not os.path.exists(db_path):
    print("База данных cookbook.db не найдена. Создаю новую...")
    
    # Подключаемся к базе (если не существует, она будет создана)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Создаем таблицу cookbooks
    cursor.execute('''
        CREATE TABLE cookbooks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER,
            price REAL
        )
    ''')
    
    # Вставляем данные о 5 книгах (используем параметризованные запросы для безопасности)
    books = [
        ("Кулинарные шедевры", 2020, 25.99),
        ("Итальянская кухня", 2018, 19.50),
        ("Вегетарианские рецепты", 2021, 22.00),
        ("Десерты мира", 2019, 30.00),
        ("Здоровая еда", 2022, 18.75)
    ]
    
    cursor.executemany('INSERT INTO cookbooks (title, year, price) VALUES (?, ?, ?)', books)
    
    # Сохраняем изменения
    conn.commit()
    conn.close()
    
    print("База данных создана и заполнена данными!")
else:
    print("База данных cookbook.db уже существует.")

print("Приложение 'Cookbook' готово. База содержит таблицу cookbooks с книгами.")


    