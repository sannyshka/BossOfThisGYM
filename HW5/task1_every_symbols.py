ukraine = input("Як сильно ви любите Україну? Скільки б разів дали по голові птн? ")

for symbol in ukraine:
    if symbol.isdigit():
        if int(symbol) % 2 == 0:
            print(f"Це число {symbol} є парним")
        else:
            print(f"Це число {symbol} не є парним")
    elif symbol.isalpha():
        if symbol.isupper():
            print(f"Ця буква {symbol} велика")
        else:
            print(f"Ця буква {symbol} маленька")
    else:
        print(f"Це символ {symbol}")
