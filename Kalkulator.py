what = input("Выберете действие (+, -): ")
a = input("Введите первое число")
b = input("Введите второе число")
if what == "+":
    print(int(a) + int(b))
elif what == "-": 
    print(int(a) - int(b))
else:
    print("Wrong operation")

