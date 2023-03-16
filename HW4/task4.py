meat = input("Яке м'ясо краще використовувати для приготування шашлику? ")
match meat:
    case "Телятина":
        print("Смачно, але не те.")
        print(f"Ви ввели дані: {type(meat)}")
        print(f"В рядку {len(meat)} символів")
    case "Свинина":
        print("Це найкраще м'ясо для шашлику.")
        print(f"Ви ввели дані: {type(meat)}")
        print(f"В рядку {len(meat)} символів")
    case _:
        print("Ні")
        print(f"Ви ввели дані: {type(meat)}")
