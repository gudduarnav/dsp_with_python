#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Group and Phase delay with Python and Scipy in IIR Notch filter
Created on Wed Dec 18 19:40:16 2024

@author: arnav
"""

import numpy as np
from scipy.signal import iirnotch, freqz
import matplotlib.pyplot as plt

# Parameters
wo = 0.1  # Normalized notch frequency (omega_c / pi)
bw = 0.001  # Normalized 3 dB bandwidth

# Design the notch filter
b, a = iirnotch(wo * np.pi, bw * np.pi)

# Compute frequency response
w, h = freqz(b, a, worN=8000)

# Plot magnitude response
plt.figure()
plt.plot(w / np.pi, 20 * np.log10(abs(h)))
plt.title('Magnitude Response of the Notch Filter')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.xlim(0,1)
plt.grid()

# Plot group delay
angles = np.unwrap(np.angle(h))
group_delay = -np.diff(angles) / np.diff(w)

plt.figure()
plt.plot(w[:-1] / np.pi, group_delay)
plt.title('Group Delay of the Notch Filter')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Group Delay (samples)')
plt.xlim(0,1)
plt.grid()
plt.show()
