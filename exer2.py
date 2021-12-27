#Дано n є N . Побудувати алгоритм для встановлення того, чи утворюють цифри зростаючу послідовність.
num1 = int(input("Введіть першу цифру :"))
num2 = int(input("Введіть другу цифру :"))
num3 = int(input("Введіть третю цифру :"))

if num1 <= num2:
    if num2 <= num3:
        print("Sequence increases!")
else:
    print("Sequence decreases!")