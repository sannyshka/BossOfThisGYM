import time

def log_time(func):
    def wrapper(n):
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        print(f"Function {func.__name__} was called at {time.ctime(start_time)} with n = {n} and took {end_time - start_time:.6f} seconds to complete.")
        return result
    return wrapper

@log_time
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1))
