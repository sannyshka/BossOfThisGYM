from flask import abort, request, redirect
import random


from app import app



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
    return ', '.join(random_names)

@app.route('/books')
def get_books():
    books = ['katerina', 'kobzar', 'gaydamaky', 'kavkaz', 'zapovit']
    count = int(request.args.get('count', random.randint(1, len(books))))
    random_books = random.sample(books, count)

    html_list = '<ul>'
    for book in random_books:
        html_list += '<li>' + book + '</li>'
    html_list += '</ul>'

    return html_list

# 2. Створити функції-обробники запитів на GET  /users та GET /books, що мають приймати url-параметри (/users/1, /books/kobzar):
# - Для /users – id, що може бути тільки числовим значенням. Якщо значення id ділиться на 2 - повертати текст із цим значенням. Якщо не ділиться – повертати статус 404 Not Found
# - Для /books – title, текстове значення. Трансформувати першу літеру title у велику, а всі інші у маленькі (за допомогою одного із методів str), повернути трансформоване значення у якості відповіді

@app.route('/users/<int:user_id>')
def get_user(user_id):
    if user_id % 2 == 0:
        return str(user_id)
    else:
        abort(404)

@app.route('/books/<string:title>')
def get_book(title):
    transformed_title = title.capitalize()
    return transformed_title

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
    table_html = '<table>\n<tr><th>parameter</th><th>value</th></tr>\n'

    for key, value in params.items():
        table_html += f'<tr><td>{key}</td><td>{value}</td></tr>\n'

    table_html += '</table>'

    return table_html

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
        form = '''
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <input type="submit" value="Log in">
        </form>
        '''
        return form

    elif request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']

            if len(username) < 5 or len(password) < 8:
                abort(400, 'Username or password does not meet the requirements')

            has_digit = any(char.isdigit() for char in password)
            has_uppercase = any(char.isupper() for char in password)

            if not (has_digit and has_uppercase):
                abort(400, 'Password should contain at least 1 digit and 1 uppercase letter')

            return redirect('/users')
        else:
            abort(400, 'Missing username or password')


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
    return '''
        <html>
        <body>
            <h1>Welcome to the Homepage!</h1>
            <ul>
                <li><a href="/login">Login</a></li>
                <li><a href="/users">Users</a></li>
                <li><a href="/books">Books</a></li>
                <li><a href="/params">Params</a></li>
            </ul>
        </body>
        </html>
    '''
