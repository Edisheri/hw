import json
import csv

# Чтение пользователей
with open('user.json', 'r') as f:
    users = json.load(f)

# Чтение книг
books = []
with open('books.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        books.append({
            'title': row['Title'],
            'author': row['Author'],
            'pages': int(row['Pages']),
            'genre': row['Genre']
        })

# Распределение книг
total_users = len(users)
total_books = len(books)
base = total_books // total_users
remainder = total_books % total_users

result = []
current_book = 0

for i in range(total_users):
    # Определяем количество книг для текущего пользователя
    num_books = base + 1 if i < remainder else base

    # Формируем список книг для пользователя
    user_books = books[current_book:current_book + num_books]
    current_book += num_books

    # Формируем структуру пользователя
    user_data = {
        'name': users[i]['name'],
        'gender': users[i]['gender'],
        'address': users[i]['address'],
        'age': users[i]['age'],
        'books': user_books
    }

    result.append(user_data)

# Запись результата
with open('result.json', 'w') as f:
    json.dump(result, f, indent=2)