# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:37:43 2023

@author: 91749
"""

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a wave equation
def wave_equation(x):
    # Define the wave equation here
    frequency = 2  # Adjust the frequency of the wave
    amplitude = 1  # Adjust the amplitude of the wave
    return amplitude * np.sin(2 * np.pi * frequency * x)

# Step 2: Generate x values (spatial positions)
x_values = np.linspace(0, 1, 1000)

# Step 3: Calculate the original wave
original_wave = wave_equation(x_values)

# Step 4: Calculate the Fourier transform
fourier_transform = np.fft.fft(original_wave)

# Step 5: Calculate the spatial frequencies
spatial_frequencies = np.fft.fftfreq(len(x_values))

# Step 6: Plot the original wave and its Fourier transform
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(x_values, original_wave, label='Original Wave')
plt.xlabel('Spatial Position')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(spatial_frequencies, np.abs(fourier_transform), label='Fourier Transform')
plt.xlabel('Spatial Frequency')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
