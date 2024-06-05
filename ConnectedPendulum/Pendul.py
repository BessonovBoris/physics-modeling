import numpy as np
from numpy import sin, cos
from scipy.integrate import solve_ivp


class Pendulum:
    def __init__(self, angle_1, angle_2, g, l, m, k, stop_force, dist_between_pendulum):
        self.angles = [[angle_1, 0.0], [angle_2, 0.0]]  # угол, скорость, угол2, скорость2

        self.dist_between_pendulum = dist_between_pendulum

        self.g = g
        self.L = l
        self.m = m
        self.K = k
        self.stop_force = stop_force

        self.elapsed_time = 0
        self.graph_data_1 = [[], [], []]    # время, угол, скорость
        self.graph_data_2 = [[], [], []]

    def get_angle(self):
        return self.angles[0][0], self.angles[1][0]

    def get_velocity(self):
        return self.angles[0][1], self.angles[1][1]

    def equations(self, t, angles):
        self.graph_data_1[0].append(self.elapsed_time)
        self.graph_data_1[1].append(np.degrees(angles[0]))
        self.graph_data_1[2].append(angles[1])

        self.graph_data_2[0].append(self.elapsed_time)
        self.graph_data_2[1].append(np.degrees(angles[2]))
        self.graph_data_2[2].append(angles[3])

        dtheta1_dt = angles[1]
        domega1_dt = (- (self.g / self.L) * angles[0] - self.stop_force * angles[1]
                      - (self.K / self.m) * (angles[0] - angles[2]))
        dtheta2_dt = angles[3]
        domega2_dt = (- (self.g / self.L) * angles[2] - self.stop_force * angles[3]
                      + (self.K / self.m) * (angles[0] - angles[2]))

        return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]

    def update(self, dt):
        state = [self.get_angle()[0], self.get_velocity()[0],
                 self.get_angle()[1], self.get_velocity()[1]]

        solution = solve_ivp(self.equations, [0, dt], state, t_eval=[0, dt])

        # print()
        # print(state)
        # print(solution.t)
        # print(solution.y)

        self.angles = [[solution.y[0][1], solution.y[1][1]],
                       [solution.y[2][1], solution.y[3][1]]]

        self.elapsed_time += dt

    def position(self):
        # print(self.get_angle())

        x_1 = np.cumsum([-self.dist_between_pendulum / 2, self.L * sin(self.get_angle()[0])])
        y_1 = np.cumsum([0, - self.L * cos(self.get_angle()[0])])

        x_2 = np.cumsum([self.dist_between_pendulum / 2, self.L * sin(self.get_angle()[1])])
        y_2 = np.cumsum([0, - self.L * cos(self.get_angle()[1])])

        return [x_1, y_1], [x_2, y_2]
