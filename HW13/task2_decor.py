import time

def log_to_file(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_path, "a") as f:
                timestamp = time.time()
                func_name = func.__name__
                f.write(f"Function '{func_name}' was called at {time.ctime(timestamp)}\n")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

log_file_path = "./function_calls.log"


with open(log_file_path, "a") as f:
    f.write("")


def log_time(log_file_path):
    pass

@log_to_file(log_file_path)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(2))
