"""
Aplica la Transformada de Fourier a una señal de audio y muestra su espectro.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def analizar_audio(archivo):
    tasa, datos = wavfile.read(archivo)
    transformada = np.fft.fft(datos)
    freqs = np.fft.fftfreq(len(transformada))

    plt.plot(freqs[:len(freqs)//2], abs(transformada[:len(transformada)//2]))
    plt.title("Espectro de Frecuencia")
    plt.show()

# analizar_audio('audio.wav')  # Descomentar si tienes un archivo de audio
