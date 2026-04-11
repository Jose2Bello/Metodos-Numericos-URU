# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:17:13 2026

@author: joseb
"""

import numpy as np

h = 0.5

T_iniciales = np.array([41.33826974, 41.30910479, 41.22192633])
T_finales = np.array([136.6945744, 137.1537977, 137.5865342])

var_inicial_oh = (T_iniciales[1] - T_iniciales[0]) / h
var_inicial_oh2 = (-3*T_iniciales[0] + 4*T_iniciales[1] - T_iniciales[2]) / (2*h)


var_final_oh = (T_finales[-1] - T_finales[-2]) / h
var_final_oh2 = (3*T_finales[-1] - 4*T_finales[-2] + T_finales[-3]) / (2*h)

print(f"t=0  O(h):   {var_inicial_oh:.4f}".replace('.', ','))
print(f"t=0  O(h^2): {var_inicial_oh2:.4f}".replace('.', ','))
print(f"t=100 O(h):   {var_final_oh:.4f}".replace('.', ','))
print(f"t=100 O(h^2): {var_final_oh2:.4f}".replace('.', ','))



h = 0.5

P_t10 = np.array([6.808634626, 6.722603837, 6.810812469, 7.066221757, 7.471397209])


P_t40 = np.array([10.5602449, 10.73878637, 10.74548899, 10.57838165, 10.24629988])

def calcular_centrales(puntos, h):
    
    oh2 = (puntos[3] - puntos[1]) / (2 * h)
  
    oh4 = (-puntos[4] + 8*puntos[3] - 8*puntos[1] + puntos[0]) / (12 * h)
    return oh2, oh4

res10 = calcular_centrales(P_t10, h)
res40 = calcular_centrales(P_t40, h)

print(f"t=10 -> O(h^2): {res10[0]:.4f}, O(h^4): {res10[1]:.4f}")
print(f"t=40 -> O(h^2): {res40[0]:.4f}, O(h^4): {res40[1]:.4f}")