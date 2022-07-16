# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Решение, которое нагуглила
# num = int (input('Введите число: '))
# def fact (num):
#     if (num ==1 or num == 0):
#         return 1
#     else:
#         return num * fact(num-1)
# print(fact(num))


num = int (input('Введите число: '))

def fact (x):
    mult = 1
    for i in range(1, x + 1):
        mult *= i
        print(mult, end=' ')

fact(num)