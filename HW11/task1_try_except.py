phone_book = {}

# Додавання контакту
def add_contact():
    try:
        name = input("Введіть ім'я: ")
        phone_number = input("Введіть номер телефону: ")
        int(phone_number)
        phone_book[name] = phone_number
        print("Контакт додано.")
    except ValueError:
        print("Помилка вводу. Будь-ласка, введіть правильний номер телефону.")

# Видалення контакту
def delete_contact():
    name = input("Введіть ім'я контакту, який бажаєте видалити: ")
    try:
        del phone_book[name]
        print("Контакт видалено.")
    except KeyError:
        print(f"Контакт з ім'ям '{name}' не знайдено.")

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
    try:
        number = phone_book[name]
        print(f"Ім'я: {name}")
        print(f"Номер телефону: {number}")
    except KeyError:
        print(f"Контакт з ім'ям '{name}' не знайдено.")

# Кількість записів
def show_stats():
    print(f"У телефонній книзі {len(phone_book)} запис(ів).")

# Команди

while True:
    print("Щоб додати контакт, введіть 'додати'.")
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
        break
    else:
        print("Неправильна команда. Введіть команду зі списку.")