import json
import csv
from itertools import cycle

# Чтение пользователей из JSON
with open('user.json', 'r') as user_file:
    users = json.load(user_file)

# Оставляем только необходимые поля у пользователей
processed_users = []
for user in users:
    processed_user = {
        "name": user.get("name", ""),
        "gender": user.get("gender", ""),
        "address": user.get("address", ""),
        "age": user.get("age", 0),
        "books": []
    }
    processed_users.append(processed_user)

# Чтение книг из CSV
with open('books.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    books = []
    for row in reader:
        book = {
            "title": row["Title"],
            "author": row["Author"],
            "pages": int(row["Pages"]),
            "genre": row["Genre"]
        }
        books.append(book)

# Распределение книг циклически между пользователями
user_cycle = cycle(processed_users)
for book in books:
    user = next(user_cycle)
    user['books'].append(book)

# Сохранение результата в JSON с форматированием
with open('result.json', 'w') as result_file:
    json.dump(processed_users, result_file, indent=2)