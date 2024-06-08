import numpy as np
import matplotlib.pyplot as plt


def fraunhofer_2rect(xz, yz, z, l, w, h, d):
    head_term = np.exp(1j * 2 * np.pi / (l) * z) * np.exp(1j * np.pi / (l * z) * (xz ** 2 + yz ** 2))
    tail_term = 4 * h * w * np.sinc(2 * xz / (l * z) * w) * np.cos(2 * np.pi * xz / (l * z) * d) * np.sinc(
        yz / (l * z) * h)

    return head_term * tail_term


w = 0.01e-3  # ширина отверстия [m]
h = 5e-3  # высота отверстия [m]
d = 5e-3  # расстояние между [m]
lam = 666e-9  # длина волны [m]
z = 1   # расстояние до экрана [m]
N = 1000

xlim = ((2 * d + w + 20 * d) / 2)
ylim = (h / 4)

x, y = np.linspace(-xlim, xlim, N), np.linspace(-ylim, ylim, N)
xz, yz = np.meshgrid(x, y)

I = np.abs(fraunhofer_2rect(xz, yz, z, lam, w, h, d)) ** 2
Ix = np.abs(fraunhofer_2rect(x, 0, z, lam, w, h, d)) ** 2
Iy = np.abs(fraunhofer_2rect(0, y, z, lam, w, h, d)) ** 2

In = I / np.max(I)
Inx = Ix / np.max(Ix)
Iny = Iy / np.max(Iy)

widths = [5, 1]
heights = [1, 1.5]

fig = plt.figure(figsize=(16, 7))
fig.suptitle("Diffraction Fraunhofer at $z={}$ m".format(z), fontsize=20)

gs = fig.add_gridspec(ncols=2, nrows=2,
                      width_ratios=widths,
                      height_ratios=heights,
                      wspace=0.05,
                      hspace=0.10)

ax_top = fig.add_subplot(gs[0, 0])
ax_central = fig.add_subplot(gs[1, 0])

ax_top.set_title("$x_z$ axis")
ax_top.set_ylabel("$|u_z(x_z,0)|^2$")
ax_top.axes.xaxis.set_ticks([])

ax_central.set_xlabel("$x_z$ (m)", fontsize=14)
ax_central.set_ylabel("$y_z$ (m)", fontsize=14)

ax_top.plot(x, Inx)
ax_central.contourf(xz, yz, In, levels=100, cmap='inferno', vmin=0, vmax=1)

plt.show()
