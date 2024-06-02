from Pendul import Pendulum
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation

FPS = 60
dist_between_pendulum = 3
g = 9.81
L = 2.0
m = 1.0
K = 0.5
stop_force = 0.05

theta1 = np.radians(30)
theta2 = np.radians(-30)


# Построение графиков
screen = plt.figure(figsize=(12, 8))


# График маятников
pendulum_graph = plt.subplot(1, 2, 1)

pendulum_graph.set_title('Маятники')
pendulum_graph.set_xlabel('x')
pendulum_graph.set_ylabel('y')
pendulum_graph.set_xlim([-4, 4])
pendulum_graph.set_ylim([-4, 4])
# pendulum_graph.legend()
pendulum_graph.grid()


# График углов
angle_graph = plt.subplot(2, 2, 2)

angle_graph.set_title('Angles')
angle_graph.set_xlabel('Время [с]')
angle_graph.set_ylabel('Угол [градусы]')
angle_graph.set_xlim([0, 20])
angle_graph.set_ylim([-90, 90])
# angle_graph.legend()
angle_graph.grid()

# График угловых скоростей
velocity_graph = plt.subplot(2, 2, 4)

velocity_graph.set_title('Velocity')
velocity_graph.set_xlabel('Время [с]')
velocity_graph.set_ylabel('Угловая скорость [рад/с]')
velocity_graph.set_xlim([0, 20])
velocity_graph.set_ylim([-10, 10])
# velocity_graph.legend()
velocity_graph.grid()

############
pendulums = Pendulum(theta1, theta2, g, L, m, K, stop_force, dist_between_pendulum)

############
# legend
line_1, = pendulum_graph.plot([], [], '-', lw=3, color=matplotlib.colors.TABLEAU_COLORS['tab:blue'])
line_2, = pendulum_graph.plot([], [], '-', lw=3, color=matplotlib.colors.TABLEAU_COLORS['tab:orange'])

line_alpha_1, = angle_graph.plot([], [], lw=2)
line_alpha_2, = angle_graph.plot([], [], lw=2)

line_velocity_1, = velocity_graph.plot([], [], lw=2)
line_velocity_2, = velocity_graph.plot([], [], lw=2)


def animate(i):
    pendulums.update(1/FPS)

    line_1.set_data(pendulums.position()[0])
    line_alpha_1.set_data(pendulums.graph_data_1[0], pendulums.graph_data_1[1])
    line_velocity_1.set_data(pendulums.graph_data_1[0], pendulums.graph_data_1[2])

    line_2.set_data(pendulums.position()[1])
    line_alpha_2.set_data(pendulums.graph_data_2[0], pendulums.graph_data_2[1])
    line_velocity_2.set_data(pendulums.graph_data_2[0], pendulums.graph_data_2[2])

    x_0 = pendulums.graph_data_1[0][-1]-20
    x_1 = pendulums.graph_data_1[0][-1]

    velocity_graph.set_xlim([x_0, x_1])

    angle_graph.set_xlim([x_0, x_1])

    return line_alpha_1, line_alpha_2, line_1, line_2, line_velocity_1, line_velocity_2


def init():
    line_alpha_1.set_data([], [])
    line_alpha_2.set_data([], [])

    line_1.set_data([], [])
    line_2.set_data([], [])

    line_velocity_1.set_data([], [])
    line_velocity_2.set_data([], [])

    return line_alpha_1, line_alpha_2, line_1, line_2, line_velocity_1, line_velocity_2


interval = 1/FPS

anim = animation.FuncAnimation(screen, animate, frames=200,
                               interval=interval, blit=True, init_func=init)

plt.tight_layout()
plt.show()
