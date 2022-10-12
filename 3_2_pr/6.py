# Занятие 6. Цикл while

# Задача «Список квадратов»
# Условие
# По данному целому числу N распечатайте все квадраты натуральных чисел,
# не превосходящие N, в порядке возрастания.
def t1():
    n = int(input())
    i = 1
    while i**2 <= n:
        print(i**2)
        i += 1


# Задача «Минимальный делитель»
# Условие
# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель,
# отличный от 1.
def t2():
    n = int(input())
    d = 2
    while n % d != 0:
        d += 1
    print(d)


# Задача «Степень двойки»
# Условие
# По данному натуральному числу N найдите наибольшую целую степень двойки,
# не превосходящую N. Выведите показатель степени и саму степень.
# Операцией возведения в степень пользоваться нельзя!
def t3():
    n = int(input())
    p, a = 0, 1  # p - power, a - amount
    rp, ra = 0, 1
    while a <= n:
        rp = p
        ra = a
        a = 1
        p += 1
        for _ in range(p):
            a *= 2
    print(rp, ra)
