def numbers(n):
    if n < 0:
        return None
    print(n)
    numbers(n - 1)


n = int(input("Enter your number: "))
numbers(n)
