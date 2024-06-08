import numpy as np
from matplotlib.colors import LinearSegmentedColormap


class Graphique():
    def Intensite(self, canvas, figure, slider1, slider2, slider3, slider4, combobox):
        N = slider1
        a = slider2/100
        l = slider3*50
        d = slider4/20
        points = combobox

        figure.clear()

        ax1 = figure.add_subplot(111)

        if points == 1:
            def Inter(t):
                return np.sin(N*np.pi*d*np.sin(np.arctan(t))*1000000/l)**2/(np.sin(np.pi*d*np.sin(np.arctan(t))*1000000/l)**2)

            def Diff(t):
                return np.sin(np.pi*a*np.sin(np.arctan(t))*1000000/l)**2/((np.pi*a*np.sin(np.arctan(t))*1000000/l)**2)

            t = np.linspace(-0.03, 0.03, 5000)

            ax1.axis([-0.03, 0.03, 0, Inter(0.00000001) + 0.5])
            ax1.grid(False)

            if l <= 500:
                couleur = 'b'
            elif l <= 600:
                couleur = 'g'
            elif l <= 700:
                couleur = 'r'
            ax1.plot(t, Diff(t)*Inter(t), couleur)
        else:
            largeur = 0.1

            cdictr = {'red':
                        ((0.0, 0.0, 0.0),
                        (largeur, 1.0, 1.0),
                        (1.0, 1.0, 1.0)),
                    'green':
                        ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0)),
                    'blue':
                        ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0))}

            cdictb= {'red':
                        ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0)),
                    'green':
                        ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0)),
                    'blue':
                        ((0.0, 0.0, 0.0),
                        (largeur, 1.0, 1.0),
                        (1.0, 1.0, 1.0))}

            cdictg= {'red':
                        ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0)),
                    'green':
                        ((0.0, 0.0, 0.0),
                        (largeur, 1.0, 1.0),
                        (1.0, 1.0, 1.0)),
                    'blue':
                        ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0))}

            red1 = LinearSegmentedColormap('red1', cdictr)
            blue1 = LinearSegmentedColormap('blue1', cdictb)
            green1 = LinearSegmentedColormap('green1', cdictg)

            ax1.set_yticks([])

            xs = np.linspace(-0.03,0.03,1000)
            ys = np.linspace(-0.03,0.03,200)

            alpha = 3000000

            ax1.set_xlabel('$y$ (m)')

            if l <= 500:
                couleur = blue1
            elif l <= 600:
                couleur = green1
            elif l <= 700:
                couleur = red1

            X, Y = np.meshgrid(xs, ys)
            Z = (np.sin(np.pi*a*np.sin(np.arctan(X))*1e+6/l)**2/((np.pi*a*np.sin(np.arctan(X))*1e+6/l)**2)
                 * np.sin(N*np.pi*d*np.sin(np.arctan(X))*1e+6/l)**2/(np.sin(np.pi*d*np.sin(np.arctan(X))*1e+6/l) ** 2)
                 * np.exp(-alpha*Y ** 2))

            ax1.pcolormesh(X, Y, Z, cmap=couleur, shading='auto')

        canvas.draw()
