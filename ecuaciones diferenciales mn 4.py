# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:11:09 2026

@author: joseb
"""

import numpy as np

# --- PARÁMETROS DEL CIRCUITO RLC ---
L = 1.33
R = 2.3
C = 0.266
V0 = 122.5
w = 56.6
q0 = 0.0
i0 = 0.0
h = 0.01
t_final = 0.2
n = int(t_final / h)

# --- SISTEMA DE ECUACIONES ---
# Y[0] = q (carga), Y[1] = i (corriente)
def f(t, Y):
    q, i = Y
    dqdt = i
    didt = (1/L) * (V0 * np.sin(w * t) - R * i - (1/C) * q)
    return np.array([dqdt, didt])

# --- RK4 PARA SISTEMAS ---
t = np.zeros(n + 1)
Y = np.zeros((n + 1, 2))  # Dos columnas: una para q y otra para i
Y[0] = [q0, i0]

for j in range(n):
    k1 = h * f(t[j], Y[j])
    k2 = h * f(t[j] + h/2, Y[j] + k1/2)
    k3 = h * f(t[j] + h/2, Y[j] + k2/2)
    k4 = h * f(t[j] + h, Y[j] + k3)
    
    Y[j+1] = Y[j] + (k1 + 2*k2 + 2*k3 + k4) / 6
    t[j+1] = t[j] + h

# --- SALIDA DE RESULTADOS ---
print(f"{'t':<6} | {'Carga q(t)':<12} | {'Corriente i(t)':<12}")
print("-" * 35)

puntos_evaluacion = [0.1, 0.2]
for j in range(len(t)):
    if round(t[j], 2) in puntos_evaluacion:
        print(f"{t[j]:<6.1f} | {Y[j,0]:<12.4f} | {Y[j,1]:<12.4f}")