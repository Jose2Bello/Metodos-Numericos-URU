# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:07:26 2026

@author: joseb
"""

import numpy as np

# --- PARÁMETROS DEL REACTOR ---
k = 0.1341
C0 = 49.3
h = 0.2
t_final = 8.0
n = int(t_final / h)

# --- DEFINICIÓN DE LA FUNCIÓN ---
# dC/dt = f(t, C)
def f(t, C):
    return -k * (C**1.5)

# --- MÉTODO DE RUNGE-KUTTA 4 ---
t = np.zeros(n + 1)
C = np.zeros(n + 1)
t[0], C[0] = 0, C0

for i in range(n):
    k1 = h * f(t[i], C[i])
    k2 = h * f(t[i] + h/2, C[i] + k1/2)
    k3 = h * f(t[i] + h/2, C[i] + k2/2)
    k4 = h * f(t[i] + h, C[i] + k3)
    
    C[i+1] = C[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    t[i+1] = t[i] + h

# --- SALIDA DE RESULTADOS ---
print(f"{'Tiempo (t)':<12} | {'Concentración (C)':<15}")
print("-" * 35)

puntos_evaluacion = [2.0, 4.0, 6.0, 8.0]

for i in range(len(t)):
    if round(t[i], 1) in puntos_evaluacion:
        print(f"{t[i]:<12.1f} | {C[i]:<15.4f}")