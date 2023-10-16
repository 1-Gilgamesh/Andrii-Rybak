while True:
    a = float ( input("Ведіть перше число: ") )
    b = float ( input("Ведіть друге число: ") )
    v = input("Ведіть символ необхіжної дії (+,-,*,/): ")
    if v == '+':
        print(str(a + b))
    elif v == '-': 
        print(str(a - b))
    elif v == '*':
        print(str(a * b))
    elif v == '//': 
        if b != 0:
            print(str(a // b))
        else: 
            print("Ділення на 0")
    else:
        print("Щось пішло не так. Спробуйте знову")    
