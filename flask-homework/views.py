from flask import abort, request, redirect, render_template, url_for, session
import random
import jsonify
from app import app
from models import User, Book, Purchase


# 1. Створити функції для обробки таких запитів:
# - GET /users – має повертати рандомний список імен (будь-яку кількість)
# - GET /books – має повертати рандомний список книжок (будь-яку кількість) у вигляді html списку

# 7. (необов'язкове виконання) Модифікувати функції обробники /users та /books із першого завдання таким чином,
# щоб вони повертали точну кількість значень на основі query param
# count: /users?count=20 має повернути 20 значень. Якщо параметр не передано — кількість має бути рандомною.

@app.route('/users')
def get_users():
    names = ['Sasha', 'Vasya', 'Katya', 'Ivan', 'Vova']
    count = int(request.args.get('count', random.randint(1, len(names))))
    random_names = random.sample(names, count)
    username = session.get('username')
    if username:
        greeting = f'Hello, {username}!'
    else:
        return redirect(url_for('login'))
    return render_template('users/users.html', users=random_names, greeting=greeting)

@app.route('/books')
def get_books():
    books = ['katerina', 'kobzar', 'gaydamaky', 'kavkaz', 'zapovit']
    count = int(request.args.get('count', random.randint(1, len(books))))
    random_books = random.sample(books, count)
    username = session.get('username')
    if username:
        greeting = f'Hello, {username}!'
    else:
        return redirect(url_for('login'))
    return render_template('books/books.html', books=random_books, greeting=greeting)


# 2. Створити функції-обробники запитів на GET  /users та GET /books, що мають приймати url-параметри (/users/1, /books/kobzar):
# - Для /users – id, що може бути тільки числовим значенням. Якщо значення id ділиться на 2 - повертати текст із цим значенням. Якщо не ділиться – повертати статус 404 Not Found
# - Для /books – title, текстове значення. Трансформувати першу літеру title у велику, а всі інші у маленькі (за допомогою одного із методів str), повернути трансформоване значення у якості відповіді

@app.route('/users/<int:user_id>')
def get_user(user_id):
    username = session.get('username')
    if username:
        greeting = f'Hello, {username}!'
    else:
        return redirect(url_for('login'))
    if user_id % 2 == 0:
        return render_template('users/users_id.html', user_id=user_id, greeting=greeting)
    else:
        abort(404)

@app.route('/books/<string:title>')
def get_book(title):
    transformed_title = title.capitalize()
    username = session.get('username')
    if username:
        greeting = f'Hello, {username}!'
    else:
        return redirect(url_for('login'))
    return render_template('books/books_id.html', book_title=transformed_title, greeting=greeting)

# 3. Створити функцію для обробки запитів GET /params – має повертати HTML таблицю, в якій будуть міститися ключі та значення query parameters.
# Наприклад, при запиті GET /params?name=Test&age=1, на сторінці має відобразитися:
#
# parameter | value
#
# name         | Test
#
# age            | 1

@app.route('/params')
def get_params():
    params = request.args
    username = session.get('username')
    if username:
        greeting = f'Hello, {username}!'
    else:
        return redirect(url_for('login'))
    return render_template('params/params.html', params=params, greeting=greeting)




# 4. Створити функцію для обробки запитів GET, POST /login – при запиті GET має
# повертати HTML форму (method=POST, action=/login), що має містити поля username, password та кнопку submit.
# При запиті POST має перевіряти чи містяться в даних запиту username та password:
# - Якщо запит містить ці дані, потрібно перенаправити користувача на сторінку /users.
# - Якщо ні – потрібно повернути помилку 400 із інформацією про відсутні дані.

# 8. (необов'язкове виконання) До функції обробника POST /login додати валідацію username та password:
# - Username не менше 5 символів
# - Password має містити мінімум 1 цифру і 1 велику літеру, має бути не менше ніж 8 символів



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login/login.html')

    elif request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']

            if len(username) < 5 or len(password) < 8:
                error_message = 'Username or password does not meet the requirements'
                return render_template('login/login.html', error_message=error_message)

            has_digit = any(char.isdigit() for char in password)
            has_uppercase = any(char.isupper() for char in password)

            if not (has_digit and has_uppercase):
                error_message = 'Password should contain at least 1 digit and 1 uppercase letter'
                return render_template('login/login.html', error_message=error_message)

            session['username'] = username

            return redirect(url_for('get_users'))
        username = session.get('username')
        if username:
            return redirect(url_for('get_users'))
        return render_template('login/login.html')


# 5. (необов'язкове виконання) Створити кастомні обробники помилок 404 та 500,
# що мають повертати кастомний html код для відображення.


@app.errorhandler(404)
def page_not_found(error):
    return 'Oops, you got it wrong.', 404

@app.errorhandler(500)
def internal_server_error(error):
    return 'Oops, internal server error.', 500

# 6. (необов'язкове виконання) Створити обробник запиту GET /, що
# має повертати html код із посиланнями на сторінки /login, /users, /books, /params


@app.route('/home')
def index():
    username = session.get('username')

    if username:
        greeting = f'Hello, {username}!'
    else:
        return redirect(url_for('login'))

    return render_template('home/home.html', greeting=greeting)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/purchases')
def get_purchases():
    purchases = ['1', '2', '3', '4', '5']
    count = int(request.args.get('count', random.randint(1, len(purchases))))
    random_purchases = random.sample(purchases, count)
    username = session.get('username')
    if username:
        greeting = f'Hello, {username}!'
    else:
        return redirect(url_for('login'))
    return render_template('purchases/purchases.html', purchases=random_purchases, greeting=greeting)

# task 5/35

@app.route('/users/json')
def get_users_json():
    users = User.query.all()
    user_list = [{'id': user.id, 'name': user.name} for user in users]
    return jsonify(users=user_list)



@app.route('/users/<int:user_id>/json')
def get_user_json(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(id=user.id, name=user.name)
    else:
        abort(404)



@app.route('/books/json')
def get_books_json():
    books = Book.query.all()
    book_list = [{'id': book.id, 'title': book.title} for book in books]
    return jsonify(books=book_list)



@app.route('/books/<int:book_id>/json')
def get_book_json(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(id=book.id, title=book.title)
    else:
        abort(404)



@app.route('/purchases/json')
def get_purchases_json():
    purchases = Purchase.query.all()
    purchase_list = [{'id': purchase.id, 'name': purchase.name} for purchase in purchases]
    return jsonify(purchases=purchase_list)



@app.route('/purchases/<int:purchase_id>/json')
def get_purchase_json(purchase_id):
    purchase = Purchase.query.get(purchase_id)
    if purchase:
        return jsonify(id=purchase.id, name=purchase.name)
    else:
        abort(404)