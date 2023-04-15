class ContextManager:
    def __init__(self):
        pass

    def __enter__(self):
        print("==========")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"An error occurred: {exc_val}")
        print("==========")
        return True

my_list = ["hi", "my", "name", "is", "sasha"]

with ContextManager():
    upper_list = list(map(str.upper, my_list))
    print(upper_list)
    1/0
