"""
Genera un fractal de Mandelbrot y lo visualiza.
"""
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i
    return max_iter

def generar_fractal(width, height, x_min, x_max, y_min, y_max, max_iter):
    img = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            x = x_min + (x_max - x_min) * j / width
            y = y_min + (y_max - y_min) * i / height
            c = complex(x, y)
            img[i, j] = mandelbrot(c, max_iter)
    return img

img = generar_fractal(800, 800, -2.0, 1.0, -1.5, 1.5, 256)
plt.imshow(img, cmap='hot', extent=(-2.0, 1.0, -1.5, 1.5))
plt.show()
