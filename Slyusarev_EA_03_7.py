
# 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file 
# и выводить на печать построчно последние строки в количестве lines 
# (на всякий случай проверим, что задано положительное целое число). 
# Протестируем функцию на файле article.txt со следующим содержимым:
'''
n = int(input("Введите желаемое кол-во строк: "))
def read_last(lines, file):
    f = open(file, 'r', encoding='utf-8')
    a = f.readlines()
    long = len(a)
    if lines < 0 and lines > long:
        print("Некорректный запрос")
        return
    for line in a[0 : lines]:
        print(line, end='')
    return
#print( read_last(n, r'C:\Users\Cesarevitch\Desktop\inf\article.txt'))
'''


#2.Составьте программу - простейший редактор текстовых файлов. Алгоритм работы программы:
#Программа предлагает ввести имя будущего файла. Записывает его, присваивая расширение .txt.
#Программа предлагает записать строку в файл. При каждом нажатии кнопки ENTER происходит запись строки и переход на новую строчку.
#Если строка пустая или спец. символ - программа сохраняет файл.

'''
import os

filename = input("Введите имя файла: ")

filename = filename + ".txt"
file = open(filename, "w")
while True:
    line = input("Введите строку: ")
    if line == "":
        break
    file.write(line + "\n")
file.close()

print('Get current working directory : ', os.getcwd())
'''