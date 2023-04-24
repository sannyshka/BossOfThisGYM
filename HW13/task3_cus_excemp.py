import datetime

error_log = open('errors.txt', 'a')

class CustomException(Exception):
    def __init__(self, message):
        current_time = datetime.datetime.now()
        error_log.write(f'{current_time}: {message}\n')
        super().__init__(message)

try:
    raise CustomException("Помилка виконання програми.")
except CustomException as e:
    print("Помилка:", e)

error_log.close()
