#1
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(-10, 10, 0.1)
# y = 6 * x - 2
#
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('График функции y = 6x - 2')
# plt.show()

#2
# import numpy as np
# import matplotlib.pyplot as plt
#
# def f1(x):
#     return 6*x**3 - 2*x + 8
#
# def f2(x):
#     return 3*x + 1
#
# x = np.linspace(-10, 10, 100)
# y1 = f1(x)
# y2 = f2(x)
#
# plt.figure(figsize=(10, 5))
# plt.plot(x, y1, label='F(x, y) = 6x**3 - 2x + 8')
# plt.plot(x, y2, label='F(x, y) = 3x + 1')
# plt.xlabel('x')
# plt.ylabel('F(x, y)')
# plt.title('Графики функций')
# plt.grid(True)
# plt.legend()
# plt.show()


#3
import matplotlib.pyplot as plt

labels = ['помидоры', 'огурцы', 'тыква', 'свекла', 'редис', 'картофель']
quantities = [100, 65, 12, 47, 89, 256]

plt.bar(labels, quantities)
plt.xlabel('Товары')
plt.ylabel('Количество')
plt.title('Столбчатая диаграмма товаров и их количества')
plt.show()