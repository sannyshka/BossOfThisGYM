# max
numbers = (3, 1, 2, 4, 5)
max_element = max(numbers)
print("Найбільший елемент в масиві:", max_element)


# max key=len
def print_name():
    pip = ["Шевцов", "Олександр", "Валерійович"]
    max_string = max(pip, key=len)
    print("Найдовше слово в реченні:", max_string)

print_name()

# Лямбда
my_list = (3, 1, 2, 4, 5)
max_value = (lambda x: max(x))(my_list)
print("Найбільший елемент в масиві:", max_value)




def args_function(a, b, c=3, d=4):
     print(a, b, c, d)
