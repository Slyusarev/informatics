
'''
1.Построить график (размер графика должен быть достаточным, чтобы визуально увидеть особенности изучаемых функций), график каждой функции должен быть одного цвета для одного значения α и β.
Подписать оси и заголовок
Создать легенду
Сохранить изображение в svg файл
'''
'''
import numpy as np
import matplotlib.pyplot as plt
import os

value = [(1, 1), (2, 1), (1, 2)]

x_val = np.linspace(-2, 2, 1300) + 0.5
x_val = x_val[x_val != 0]

def f(x, a, b):
    return (x**b + a**b) / x**b

plt.figure(figsize=(10, 8))

for a, b in value:
y_val = f(x_val, a, b)
plt.scatter(x_val, y_val, label=f'alpha={a}, beta={b}', s=1)

plt.axhline(0, color='red', linewidth=1.5)
plt.axvline(0, color='red', linewidth=1.5)

plt.ylim(-8, 8)
plt.legend()
plt.show()

directory = os.getcwd()
plt.savefig(directory + '/dpp.svg')
'''
'''
Задание 3.
Построить в общих осях графики для x<0.
На том же графике сделать 1 врезку, демонстрирующую поведение графиков при удалении x от 0 к −∞.
Необходимо продемонстрировать возможность (или невозможность) пересечений и стремление функций. 
Так же нанесите на графики прямую f(x) = 0.
Цвет линий на врезках и основном графике должен быть одинаковым для одних и тех же значений α и β.
'''
'''
import numpy as np
import matplotlib.pyplot as plt
import os

x_negative = np.linspace(-8, -0.1, 1000)
x_negative_for_inf = np.linspace(-1000, -996, 1000)

plt.figure(figsize=(14, 7))

for alpha, beta in value:
    f_values = f(x_negative, alpha, beta)
    plt.scatter(x_negative, f_values, s=5, label=f'α={alpha}, β={beta}')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графики функций при различных значения α и β')

plt.axhline(0, color='black', linewidth=1.5)
plt.axvline(0, color='black', linewidth=1.5)

plt.ylim(-8, 10)
plt.xlim(-8, 1)

plt.legend()
plt.grid(True)

inset_axes = plt.axes([0.3, 0.58, 0.4, 0.25])

for alpha, beta in value:
    f_values = f(x_negative_for_inf, alpha, beta)
    inset_axes.scatter(x_negative_for_inf, f_values, s=3, label=f'α={alpha}, β={beta}')

inset_axes.set_title('Стремление функции к бесконечности')

inset_axes.axhline(0, color='black', linewidth=1.5)
inset_axes.axvline(0, color='black', linewidth=1.5)

inset_axes.set_ylim(0.99, 1.01)
inset_axes.set_xlim(-1000, -996)

inset_axes.grid(True)

plt.show()

plt.savefig(directory + '/dpp3.svg')
'''

'''
Задание 4.
Построить в общих осях графики для:
α=1,β=0.5
α=1,β=−0.5
α=1,β=−1.5
Сделайте выводы о поведении графиков, включая возрастание/убывание и выпуклость/вогнутость

В результате выполнения предыдущей задачи, вы вероятно заметите, 
что все графики с α=1 проходят через общую точку (1, 2).
Постройте в одном ряду 3 графика, чтобы убедиться в выводах, сделанных по результатам предыдущей задачи.
Каждый график будет содержать 4 кривые. 2 общих:
α=1,β=0 
α=1,β=−1
И по 2 уникальных для каждого графика:
α=1,β=0.5 и
α=1,β=0.8
α=1,β=−0.5 и
α=1,β=−0.8
α=1,β=−1.5 и
α=1,β=−2.5
Не забудьте добавить легенду на каждый график. 
Для этого может потребоваться вызвать метод legend() для каждого объекта осей.
'''
'''
import numpy as np
import matplotlib.pyplot as plt
import os
x = np.linspace(0.01, 2, 2000)


value = [
    [(1, 0.5), (1, 0.8)],
    [(1, -0.5), (1, -0.8)],
    [(1, -1.5), (1, -2.5)]
]

plt.figure(figsize=(15, 5))

for i, value_set in enumerate(value):
    plt.subplot(1, 3, i + 1)

    plt.scatter(x, f(x, 1, 0), s=3, label='α=1,β=0')
    plt.scatter(x, f(x, 1, -1), s=3, label='α=1,β=-1')

    for alpha, beta in value_set:
        plt.scatter(x, f(x, alpha, beta), s=3, label=f'α={alpha},β={beta}')

    plt.legend()
    plt.ylim(1, 3)

plt.tight_layout()
plt.suptitle('Графики при различных α и β. Пересечение в (1, 2).')
plt.show()

plt.savefig(directory + '/dpp4.svg')
'''