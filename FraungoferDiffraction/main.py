import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.animation as animation
from numpy import sin, cos
from scipy.integrate import solve_ivp
import NewtonRing


def on_change_value(value: np.float64):
    global plotter
    global newtonRing
    newtonRing.lam = lambda_param.val
    newtonRing.r = r_param.val

    plotter.plot_image_light()
    plotter.plot_intensity()


lambda_ = 500
"""Длина волны [nm]"""

L = 1
"""Расстояние до объекта"""

# окно для графиков
screen = plt.figure(figsize=(12, 8))
screen.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

# график зависимости интенсивности от координаты
intensity_graph = plt.subplot(1, 2, 1)
intensity_graph.set_title('Intensity')
intensity_graph.grid()

# Вывод колец
light_graph = plt.subplot(1, 2, 2)
light_graph.grid()

axes_lambda_param = plt.axes([0.05, 0.25, 0.85, 0.04])
lambda_param = Slider(axes_lambda_param,
                 label='lamda',
                 valmin=50,
                 valmax=800,
                 valinit=500,
                 valfmt='%1d')
lambda_param.on_changed(on_change_value)

axes_r_param = plt.axes([0.05, 0.17, 0.85, 0.04])
r_param = Slider(axes_r_param,
                 label='r',
                 valmin=0.0,
                 valmax=5.0,
                 valinit=2,
                 valfmt='%1.1f')
r_param.on_changed(on_change_value)



plt.show()
