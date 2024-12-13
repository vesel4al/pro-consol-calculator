from math import sqrt,cos,sin,tan,pow,fabs,factorial
def themes_and_prints():
    print("Привет!Это проффесиональный консольный калькулятор!Выбери функцию:")
    print()
    print("1)Сложение чисел")
    print("2)Вычитание чисел")
    print("3)Деление чисел")
    print("4)Целочисленное деление")
    print("5)Остаток от деления")
    print("6)Умножение чисел")
    print("7)Возведение в степень")
    print("8)Модуль числа")
    print("9)Корень из числа")
    print("10)Факториал из числа")
    print("11)Вычисление синуса из числа")
    print("12)Вычисление косинуса из числа")
    print("13)Вычисление тангенса из числа")
def sum_of_numbers():
    sofn_1 =float(input("Чему равно 1 число?"))
    sofn_2 =float(input("Чему равно 2 число?"))
    sum_of_numbers =sofn_1 + sofn_2
    print(f"Сумма чисел {sofn_1} и {sofn_2 } равна {sum_of_numbers}")
    input()
def subtraction_of_numbers():
    sofn_1 = float(input("Чему равно 1 число?"))
    sofn_2 = float(input("Чему равно 2 число?"))
    subtraction_of_numbers =sofn_1 - sofn_2
    print(f"Разность чисел {sofn_1} и {sofn_2} равна {subtraction_of_numbers}")
    input()
def division_of_numbers():
    dofn_1 = float(input("Чему равно 1 число?"))
    dofn_2 = float(input("Чему равно 2 число?"))
    division_of_numbers =dofn_1 / dofn_2
    print(f"Деление числа {dofn_1} на число {dofn_2} число равно {division_of_numbers}")
    input()
def full_division_of_numbers():
    fdofn_1 = float(input("Чему равно 1 число?"))
    fdofn_2 = float(input("Чему равно 2 число?"))
    full_division_of_numbers =dofn_1 // dofn_2
    print(f"Деленое нацело числа {fdofn_1} на число {fdofn_2} равно {full_division_of_numbers}")
    input()
def remainder_of_division():
    rod_1 = float(input("Чему равно 1 число?"))
    rod_2 = float(input("Чему равно 2 число?"))
    remainder_of_division =rod_1 % rod_2
    print(f"Остаток от деления числа {rod_1} на {rod_2} равен {remainder_of_division}")
    input()
def multiplication_of_numbers():
    mof_1 = float(input("Чему равно 1 число?"))
    mof_2 = float(input("Чему равно 2 число?"))
    multiplication_of_numbers =mof_1 * mof_2
    print(f"Результат умножения числа {mof_1} на число {mof_2} равен {multiplication_of_numbers}")
    input()
def exponentiation_of_numbers():
    eon_1 = float(input("Чему равно 1 число?"))
    eon_2 = float(input("Чему равна степень,в которую ты хочешь возвести число?"))
    exponentiation_of_numbers =pow(eon_1,eon_2)
    print(f"Число {eon_1} в степени {eon_2} равно {exponentiation_of_numbers}")
    input()
def modul_of_numbers():
    mon_1 =float(input("Чему равно число,модуль которого ты хочешь получить?"))
    modul_of_numbers =fabs(mon_1)
    print(f"Модуль числа {mon_1} равен {modul_of_numbers}")
    input()
def root_of_number():
    rof_1 =float(input("Чему равно число,корень которого тебе нужен"))
    root_of_number =sqrt(rof_1)
    print(f"Корень из числа {rof_1} равен {root_of_number}")
    input()
def factorial_of_number():
    fon_1 =float(input("Чему равно число,факториал которого тебе нужен"))
    factorial_of_number =factorial(fon_1)
    print(f"Факориал из числа {fon_1} равен {factorial_of_number}")
    input()
def sine_of_number():
    son_1 =float(input("Чему равно число,синус которого тебе нужен"))
    sine_of_number =sin(son_1)
    print(f"синус из числа {son_1} равен {sine_of_number}")
    input()
def cosine_of_number():
    con_1 = float(input("Чему равно число,косинус которого тебе нужен"))
    cosine_of_number =cos(con_1)
    print(f"косинус из числа {con_1} равен {cosine_of_number}")
    input()
def tangent_of_number():
    ton_1 = float(input("Чему равно число,тангенс которого тебе нужен"))
    tangent_of_number =tan(ton_1)
    print(f"Тангенс из числа {ton_1} равен {tangent_of_number}")
    input()
themes_and_prints()
theme = int(input("На какой теме ты остановился?"))
if theme ==1:
    sum_of_numbers()
elif theme ==2:
    subtraction_of_numbers()
elif theme ==3:
    division_of_numbers()
elif theme ==4:
    full_division_of_numbers()
elif theme ==5:
    remainder_of_division()
elif theme ==6:
    multiplication_of_numbers()
elif theme ==7:
    exponentiation_of_numbers()
elif theme ==8:
    modul_of_numbers()
elif theme ==9:
    root_of_number()
elif theme ==10:
    factorial_of_number()
elif theme ==11:
    sine_of_number()
elif theme ==12:
    cosine_of_number()
elif theme ==13:
    tangent_of_number()
else:
    print(f"Опперации {theme} не найдено")
    input()






