import time

def log_time(times):
    def decorator(func):
        def wrapper(n):
            for i in range(times):
                start_time = time.time()
                result = func(n)
                end_time = time.time()
                print(f"Function {func.__name__} was called at {time.ctime(start_time)} with n = {n} and took {end_time - start_time:.6f} seconds to complete.")
            return result
        return wrapper
    return decorator

@log_time(times=5)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1))
