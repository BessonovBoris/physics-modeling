import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def gaussian(sigma, mu, x):
    '''Отображаемая фукнция'''
    return (1.0 / (sigma * np.sqrt(2.0 * np.pi)) *
            np.exp(-((x - mu) ** 2) / (2 * sigma * sigma)))


def updateGraph():
    '''!!! Функция для обновления графика'''
    # Будем использовать sigma и mu, установленные с помощью слайдеров
    global slider_sigma
    global slider_mu
    global graph_axes

    # Используем атрибут val, чтобы получить значение слайдеров
    sigma = slider_sigma.val
    mu = slider_mu.val
    x = np.linspace(-5.0, 5.0, 300)
    y = gaussian(sigma, mu, x)

    graph_axes.clear()
    graph_axes.plot(x, y)
    plt.draw()


def onChangeValue(value: np.float64):
    '''!!! Обработчик события изменения значений слайдеров'''
    updateGraph()


if __name__ == '__main__':
    # Начальные параметры графиков
    current_sigma = 0.2
    current_mu = 0.0

    # Создадим окно с графиком
    fig, graph_axes = plt.subplots()
    graph_axes.grid()

    # Выделим область, которую будет занимать график
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

    # Создадим слайдер для задания sigma
    axes_slider_sigma = plt.axes([0.05, 0.25, 0.85, 0.04])
    slider_sigma = Slider(axes_slider_sigma,
                          label='σ',
                          valmin=0.1,
                          valmax=1.0,
                          valinit=0.5,
                          valfmt='%1.2f')

    # Создадим слайдер для задания mu
    axes_slider_mu = plt.axes([0.05, 0.17, 0.85, 0.04])
    slider_mu = Slider(axes_slider_mu,
                       label='μ',
                       valmin=-4.0,
                       valmax=4.0,
                       valinit=0.0,
                       valfmt='%1.2f')

    # !!! Подпишемся на события при изменении значения слайдеров.
    slider_sigma.on_changed(onChangeValue)
    slider_mu.on_changed(onChangeValue)

    updateGraph()
    plt.show()