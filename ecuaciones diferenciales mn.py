import numpy as np

# --- PARÁMETROS DE LA EVALUACIÓN ---
k = 0.0434
T_amb = 39.6
Q = 1.33
T0 = 130.2
h = 0.5
t_final = 40
n = int(t_final / h)

# --- DEFINICIÓN DE LA FUNCIÓN ---
# dT/dt = f(t, T)
def f(t, T):
    return -k * (T - T_amb) + Q

# --- MÉTODO DE EULER ---
t = np.zeros(n + 1)
T = np.zeros(n + 1)
t[0], T[0] = 0, T0

for i in range(n):
    T[i+1] = T[i] + h * f(t[i], T[i])
    t[i+1] = t[i] + h

# --- SALIDA DE RESULTADOS ---
print(f"{'Tiempo (t)':<12} | {'Temperatura (T)':<15}")
print("-" * 30)

# Filtrar solo los valores solicitados en la imagen
puntos_evaluacion = [10.0, 20.0, 30.0, 40.0]

for i in range(len(t)):
    # Usamos round para manejar la precisión de punto flotante en la comparación
    if round(t[i], 1) in puntos_evaluacion:
        print(f"{t[i]:<12.1f} | {T[i]:<15.4f}")