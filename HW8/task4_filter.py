my_list = [1, 2, 3, "a", "b", "c"]
number_list = list(filter(lambda x: isinstance(x, (int)), my_list))
print(number_list)
