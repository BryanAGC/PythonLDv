"""
Dibuja el conjunto de Mandelbrot utilizando Python y Matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generar_fractal(xmin, xmax, ymin, ymax, ancho, alto, max_iter):
    imagen = np.zeros((alto, ancho))
    for i, y in enumerate(np.linspace(ymin, ymax, alto)):
        for j, x in enumerate(np.linspace(xmin, xmax, ancho)):
            imagen[i, j] = mandelbrot(complex(x, y), max_iter)
    return imagen

imagen = generar_fractal(-2, 1, -1.5, 1.5, 400, 400, 100)
plt.imshow(imagen, cmap="inferno", extent=(-2, 1, -1.5, 1.5))
plt.colorbar()
plt.title("Conjunto de Mandelbrot")
plt.show()
