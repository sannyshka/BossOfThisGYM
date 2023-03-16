age = input("Скільки тобі років?:")
if age.isdigit():
    print("Це число")
    if int(age) % 2 == 0:
        print("Парне")
    else:
        print("Непарне")
elif age.isalpha():
    print("Це слово")
    print(f"В рядку {len(age)} символів")
