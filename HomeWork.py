                
a = float(input())
b = float(input())
c = float(input())

d = (b ** 2 - (4 * a * c))

if d > 0: print ((((-b) + d**0.5)/(2*a)) , (((-b) - d**0.5)/(2*a)))
if d == 0 and (a != 0 and b != 0 and c != 0): print( (-b) / (2*a), "1 корень")
if a == 0 and b == 0 and c == 0: print("корней бесконечно много")
if d < 0: print("корней нет")
'''

'''
1.Написать программу, которая будет делить введенные пользователем два вещественных числа
и выводить результат на экран, сообщая об ошибке в случае деления на ноль
'''
'''
a = float(input("Введите первое чилсо: "))
b = float(input("Введите второе число: "))
if b != 0: 
    print(a / b)
else: print("Ошибка, на ноль делить нельзя")
'''

'''
Рассчитать стоимость покупки с учетом скидки в 35%, которая предоставляется покупателю, если сумма покупки превышает 20 у.е. 
Сумму покупки ввести с клавиатуры, а результаты округлить до сотых (копейки, центы и т.д.). 
Вывести на экран итоговую стоимость и размер предоставленной скидки.
'''
'''
stoimost = float(input("Стоимость товара: "))

if stoimost > 20:
    print(round((stoimost) - (stoimost / 100 * 35), 2), ((stoimost / 100 * 35)))
else:
    print (stoimost, "0")
'''

'''
3. Напишите скрипт, который по введенному пользователем числу от 1 до 12, будет выводить на экран сообщение в виде названия месяца и времени года. 
Если пользователь введет недопустимое число, программа должна выдавать сообщение об ошибке.
'''
'''
a = int(input("Введите номер месяца: "))

b = [f'' "Январь - зима", "Февраль - зима", "Март - весна", "Апрель - весна", "Май - весна", "Июнь - лето", "Июль - лето", "Август - лето",
f'' "Сентябрь - осень", "Октябрь - осень", "Ноябрь - осень", "Декабрь - зима"]
if a >= 1 and a <= 12: print(b[a-1])
else: print (" Ошибка. Такого месяца не существует")
