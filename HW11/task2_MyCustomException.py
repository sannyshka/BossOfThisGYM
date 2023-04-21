class MyCustomException(Exception):
    def __init__(self):
        super().__init__("Custom exception is occurred")


try:
    raise MyCustomException()
except MyCustomException as exc:
    print(f"Custom exception caught: {exc}")
