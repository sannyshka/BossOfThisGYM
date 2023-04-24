import json

phone_book = {}

# Завантаження даних з файлу
try:
    with open('phone_book.json', 'r') as f:
        phone_book = json.load(f)
except FileNotFoundError:
    phone_book = {}

#Збереження даних у файл
def save_data():
    with open('phone_book.json', 'w') as f:
        json.dump(phone_book, f)

# Додавання контакту
def add_contact():
    name = input("Введіть ім'я: ")
    phone_number = input("Введіть номер телефону: ")
    phone_book[name] = phone_number
    print("Контакт додано.")
    save_data()

# Видалення контакту
def delete_contact():
    name = input("Введіть ім'я контакту, який хочте видалити: ")
    if name in phone_book:
        del phone_book[name]
        print("Контакт видалено.")
    else:
        print("Контакт не знайдено.")
        save_data()

# Виведення списку всіх контактів
def list_contacts():
    if not phone_book:
        print("Телефонна книга порожня.")
    else:
        print("Контакти:")
        for name, phone_number in phone_book.items():
            print(f"{name}: {phone_number}")

# Пошук контакту за ім'ям та виведення його детальної інформації
def show_contact():
    name = input("Введіть ім'я контакту, який хочете переглянути: ")
    if name in phone_book:
        print(f"Ім'я: {name}")
        print(f"Номер телефону: {phone_book[name]}")
    else:
        print("Контакт не знайдено.")

# Кількість записів
def show_stats():
    print(f"У телефонній книзі {len(phone_book)} запис(ів).")

# Команди
while True:
    print("Щоб додати конттакт, введіть 'додати'.")
    print("Щоб видалити контакт, введіть 'видалити'.")
    print("Щоб вивести список контактів, введіть 'список'.")
    print("Щоб переглянути контакт, введіть 'переглянути'.")
    print("Щоб вийти з програми, введіть 'вийти'.")
    print("Щоб переглянути кількість контактів у книзі, введіть 'кількість'.")

    command = input("Введіть команду: ").lower()

    if command == "додати":
        add_contact()
    elif command == "кількість":
        show_stats()
    elif command == "видалити":
        delete_contact()
    elif command == "список":
        list_contacts()
    elif command == "переглянути":
        show_contact()
    elif command == "вийти":
        save_data()
        break
    else:
        print("Неправильна команда. Введіть команду зі списку.")
