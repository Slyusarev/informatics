'''
1. Дана строка. Подсчитать самую длинную последовательность подряд идущих букв «н». 
Преобразовать ее, заменив точками все восклицательные знаки.
'''
'''
a = str(input("Введите строку: "))
k=1
mxm = -10000000

for i in range(len(a)-1):
    if a[i] == a[i+1] == "н":
        k += 1
        dlin = max(mxm, k)
    if a[i] != a[i+1]:
        k = 1
a = a.replace("!", ".")
    
print(dlin,a)
'''

'''
2.Дана строка символов, среди которых есть одна открывающаяся и одна закрывающаяся скобки. 
Вывести на экран все символы, расположенные внутри этих скобок.
'''


'''
a = str(input("Введите строку: "))

for i in range(len(a)):
    if a[i] == "(":
        b = a[i+1:len(a)]
        print(b)
        for j in range(len(b)):
            if b[j] == ")":
                c = b[0 : j]
                print(c)
                '''


'''
3.Дана строка. Вывести все слова, начинающиеся на букву "а" и слова оканчивающиеся на букву "я".
'''

'''
 = str(input("Введите строку: "))
#a = list(map(a.split()))
my_set = set()
for i in range(0, len(a)):
    if a[i] == "а":
        b = a[i:len(a)]
        for j in range(len(b)):
            if b[j] == "я":
                c = b[0: j+1]
                my_set.add(c)
print(my_set)
'''
'''
a = str(input("Введите строку: "))
line = a.split()
end_line = []
for i in line:
    if i.lower()[0] == "а" and i.lower()[len(i)-1] == "я":
        end_line.append(i)
for i in end_line:
    print(i)
'''