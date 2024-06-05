import numpy as np
from matplotlib.pyplot import Axes
import matplotlib.pyplot as plt


class NewtonRings:
    def __init__(self,
                 r: float,           # радиус кривизны (м)
                 lam: float,         # длина волны (нм)
                 n_lens: float,      # показатель преломления линзы
                 n_plate: float,     # показатель преломления пластины
                 n_medium: float     # показатель преломления среды
                 ):
        self.r = r
        self.lam = lam
        self.n_lens = n_lens
        self.n_plate = n_plate
        self.n_medium = n_medium
        self.I0 = 0.5

    def delta_r(self,
                 r: np.ndarray,  # x-координаты точек на экране (м)
                ) -> np.ndarray:
        return np.power(r, 2) / 2 * (1/self.r)

    def call_intensity(self,
                 r: np.ndarray,  # x-координаты точек на экране (м)
                ) -> np.ndarray:
        """Вычисляет интенсивность изображения на экране"""
        return 4*self.I0*np.power(np.sin(np.pi*1*np.power(r,2) / (self.lam*self.r) + np.pi/2), 2)


class NRPlotter:
    def __init__(self, nr: NewtonRings, intensity_graph: Axes, image_light: Axes):
        self.newtonRing = nr
        self.precision = 100
        self.intensity_graph = intensity_graph
        self.image_light = image_light

    def plot_intensity(self):
        self.intensity_graph.clear()
        self.intensity_graph.set_title('Intensity')

        self.intensity_graph.set_xlabel('r [mm]')
        self.intensity_graph.set_ylabel('I')
        self.intensity_graph.grid()

        rs = np.linspace(0, 200, self.precision)
        data = self.newtonRing.call_intensity(rs)

        self.intensity_graph.plot(rs, data)

    def plot_image_light(self):
        self.image_light.clear()
        self.image_light.set_aspect('equal')

        # Радиусы колец
        count = 200
        r_dark = [np.sqrt(m * self.newtonRing.lam * self.newtonRing.r / self.newtonRing.n_medium) for m in range(1, count+1)]
        r_bright = [np.sqrt((m + 0.5) * self.newtonRing.lam * self.newtonRing.r / self.newtonRing.n_medium) for m in range(count)]

        for i in range(len(r_dark)-1, -1, -1):
            r = r_dark[i]
            while r > r_bright[i]:
                circle = plt.Circle((0, 0), r, color='black', fill=False)
                self.image_light.add_artist(circle)
                r -= 0.5

        r = 0
        while r < r_bright[0]:
            circle = plt.Circle((0, 0), r, color='black', fill=False)
            self.image_light.add_artist(circle)
            r += 0.5

        self.image_light.set_xlim(-95, 95)
        self.image_light.set_ylim(-95, 95)
        self.image_light.set_xlabel('x [mm]')
        self.image_light.set_ylabel('y [mm]')
        self.image_light.set_title('Кольца Ньютона')