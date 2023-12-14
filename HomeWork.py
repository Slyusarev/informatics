'''
Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2). 
Найти и напечатать координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный.
Вычисления оформить в виде процедуры.
'''
'''
x1 = int(input("Координата x1: "))
x2 = int(input("Координата x2: "))
y1 = int(input("Координата y1: "))
y2 = int(input("Координата y2: "))
z1 = int(input("Координата z1: "))
z2 = int(input("Координата z2: "))

def function_1(x1,x2,y1,y2,z1,z2):
    a = abs(x2) / abs(x1)
    b = abs(y2) / abs(y1)
    c = abs(z2) / abs(z1)
    if min(a,b,c) == a: print ("X", "(", x1,";" ,x2, ")")
    if min(a,b,c) == b: print("Y", "(", y1, ";" ,y2, ")")
    else: print ("Z", "(", z1, ";", z2, ")")
    
print(function_1(x1,x2,y1,y2,z1,z2))
'''


''' 
2.Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет собой палиндром, 
т. е. читается одинаково слева направо и справа налево. 
'''

'''
def is_prime(number): #Другая версия проверки простоты числа 
    number = int(number)
    if number % 2 == 0 or number == 1:
        return False
    gr = int(number**0.5)
    for i in range(3, gr, 2):
        if number % i == 0:
            return False
        
    return True
'''

'''
n = int(input("Введите число n: "))

def division(x):
    my_set = set()
    for i in range(1,x+1):
        if x % i == 0:
            my_set.add(x/i)
    return (my_set)

for i in range(n):
    a = bin(i)[2::]
    if a == a[::-1] and len(division(i)) == 2:
        print(i)
'''
'''
Задана окружность (x-a)^2 + (y-b)^2 = r^2 и точки P(p1, p2), F(f1, f2), L(l1, l2). 
Выяснить и вывести на экран, сколько точек и какие лежить внутри окружности. Проверку сформировать в виде процедуры.
'''
'''
a = int(input("Смещение x "))
b = int(input("Смещение y "))
x = int(input("Координата x "))
y = int(input("Координата y "))
#(x-a)^2 + (y-b)^2 = r^2
k = 0
p1 = int(input("Координата p1 "))
p2 = int(input("Координата p2 "))
f1 = int(input("Координата f1 "))
f2 = int(input("Координата f2 "))
l1 = int(input("Координата l1 "))
l2 = int(input("Координата l2 "))

r = (((x - a)**2)+((y-b)**2))**0.5
long_p = ((p1)**2 + (p2)**2)**0.5
long_f = ((f1)**2 + (f2)**2)**0.5
long_l = ((l1)**2 + (l2)**2)**0.5
point_name_p = "p"
point_name_f = "f"
point_name_l = "l"


def circle(r,long, point_name):
    if r >= long:
        global k
        k += 1
        print("Точка", point_name, "лежит")
print(circle(r,long_p, point_name_p),circle(r,long_f, point_name_f),circle(r,long_l, point_name_l), "Кол-во точек:", k)
'''
