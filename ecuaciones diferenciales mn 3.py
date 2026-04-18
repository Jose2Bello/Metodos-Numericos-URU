# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:09:14 2026

@author: joseb
"""

import numpy as np

# --- PARÁMETROS DEL TANQUE ---
K = 0.692
P = 0.33
y0 = 20.0
h = 0.25
t_final = 20.0
n = int(t_final / h)

# --- DEFINICIÓN DE LA FUNCIÓN ---
# dy/dt = f(t, y)
def f(t, y):
    return -K * np.sqrt(y) + P

# --- MÉTODO DE EULER ---
t = np.zeros(n + 1)
y = np.zeros(n + 1)
t[0], y[0] = 0, y0

for i in range(n):
    y[i+1] = y[i] + h * f(t[i], y[i])
    t[i+1] = t[i] + h

# --- SALIDA DE RESULTADOS ---
print(f"{'Tiempo (t)':<12} | {'Nivel (y)':<15}")
print("-" * 30)

puntos_evaluacion = [5.0, 10.0, 15.0, 20.0]

for i in range(len(t)):
    if round(t[i], 2) in puntos_evaluacion:
        print(f"{t[i]:<12.1f} | {y[i]:<15.4f}")