import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
import matplotlib
import matplotlib.animation as animation
from numpy import sin, cos
from scipy.integrate import solve_ivp


def line(x, a=1.0, b=0.0):
    return a*x + b


def update_graph(graph):
    global a_param
    global b_param

    a = a_param.val
    b = b_param.val

    x = np.linspace(-10, 10, 3)
    y = line(x, a, b)

    graph.set_data(x, y)
    plt.draw()


def on_change_value(value: np.float64):
    global line_1

    update_graph(line_1)


def func_on_change_graph(graph):
    return


N = 1
"""Кол-во щелей в а.е."""

d = 0.01  #
"""Ширина в мм"""

T = 0.1  #
"""Период"""

li = 1
"""Расстояние от щели до экрана в м"""

screem = plt.figure(figsize=(8, 4))
screem.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

# график зависимости интенсивности от координаты
intensity_graph = plt.subplot(1, 2, 1)
intensity_graph.set_title('Intensity')
intensity_graph.set_xlim([-10, 10])
intensity_graph.set_ylim([-10, 10])
intensity_graph.grid()

# Вывод цветого распеределения интенсивности на расстоянии li
light_graph = plt.subplot(1, 2, 2)
light_graph.grid()

axes_a_param = plt.axes([0.05, 0.25, 0.85, 0.04])
a_param = Slider(axes_a_param,
                 label='a',
                 valmin=-5.0,
                 valmax=5.0,
                 valinit=1,
                 valfmt='%1.1f')
a_param.on_changed(on_change_value)

axes_b_param = plt.axes([0.05, 0.17, 0.85, 0.04])
b_param = Slider(axes_b_param,
                 label='b',
                 valmin=-5.0,
                 valmax=5.0,
                 valinit=0,
                 valfmt='%1.1f')
b_param.on_changed(on_change_value)

line_1, = intensity_graph.plot([], [], lw=3)

plt.show()
