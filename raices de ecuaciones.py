import numpy as np
import os

# =================================================================
# 1. DEFINICIÓN DE FUNCIONES Y DERIVADAS
# =================================================================

# Caso 1: Dilatación
def f1(x): return x**3 - 9*x - 110
def df1(x): return 3*x**2 - 9

# Caso 2: Refrigeración
def f2(t): return 34 + (95 - 34) * np.exp(-0.079 * t) - 47
def df2(t): return (61) * (-0.079) * np.exp(-0.079 * t)

# Caso 3: Reactancia
def f3(x): return x**2 - 4.98 * np.log(x + 1) - 5
def df3(x): return 2*x - (4.98 / (x + 1))

# Caso 4: Resistencia
def f4(R): return R * np.exp(0.1 * R) - 3.32
def df4(R): return np.exp(0.1 * R) + R * (0.1 * np.exp(0.1 * R))

# =================================================================
# 2. MÉTODOS NUMÉRICOS
# =================================================================

TOLERANCIA = 1e-5

def metodo_biseccion(func, a, b, max_iter):
    if func(a) * func(b) >= 0:
        print("\n[!] Error: f(a) y f(b) deben tener signos opuestos.")
        return None
    xr, xr_old, i = 0.0, a, 0
    print(f"\n{'Iter':<5} {'a':<10} {'b':<10} {'xr':<10} {'Error %':<10}")
    while i < max_iter:
        xr = (a + b) / 2
        ea = abs((xr - xr_old) / xr) * 100 if xr != 0 else 0
        print(f"{i+1:<5} {a:<10.5f} {b:<10.5f} {xr:<10.5f} {ea:<10.5f}%")
        if ea < TOLERANCIA and i > 0: break
        if func(a) * func(xr) < 0: b = xr
        else: a = xr
        xr_old, i = xr, i + 1
    return xr

def metodo_falsa_posicion(func, a, b, max_iter):
    if func(a) * func(b) >= 0:
        print("\n[!] Error: f(a) y f(b) deben tener signos opuestos.")
        return None
    xr, xr_old, i = 0.0, a, 0
    print(f"\n{'Iter':<5} {'a':<10} {'b':<10} {'xr':<10} {'Error %':<10}")
    while i < max_iter:
        xr = b - (func(b) * (a - b)) / (func(a) - func(b))
        ea = abs((xr - xr_old) / xr) * 100 if xr != 0 else 0
        print(f"{i+1:<5} {a:<10.5f} {b:<10.5f} {xr:<10.5f} {ea:<10.5f}%")
        if ea < TOLERANCIA and i > 0: break
        if func(a) * func(xr) < 0: b = xr
        else: a = xr
        xr_old, i = xr, i + 1
    return xr

def metodo_newton_raphson(func, dfunc, x0, max_iter):
    xi, i = x0, 0
    print(f"\n{'Iter':<5} {'xi_next':<15} {'Error %':<15}")
    while i < max_iter:
        dfx = dfunc(xi)
        if dfx == 0: return None
        xi_next = xi - (func(xi) / dfx)
        ea = abs((xi_next - xi) / xi_next) * 100 if xi_next != 0 else 0
        print(f"{i+1:<5} {xi_next:<15.8f} {ea:<15.8f}%")
        if ea < TOLERANCIA: break
        xi, i = xi_next, i + 1
    return xi

def metodo_secante(func, x0, x1, max_iter):
    i = 0
    print(f"\n{'Iter':<5} {'xi+1':<15} {'Error %':<15}")
    while i < max_iter:
        f0, f1 = func(x0), func(x1)
        if f1 - f0 == 0: return None
        x_next = x1 - (f1 * (x1 - x0)) / (f1 - f0)
        ea = abs((x_next - x1) / x_next) * 100 if x_next != 0 else 0
        print(f"{i+1:<5} {x_next:<15.8f} {ea:<15.8f}%")
        if ea < TOLERANCIA: break
        x0, x1, i = x1, x_next, i + 1
    return x1

# =================================================================
# 3. INTERFAZ DE USUARIO (MENÚ ACTUALIZADO)
# =================================================================

def menu():
    while True:
        print("\n" + "="*45)
        print("   SISTEMA DE CÁLCULO: CASOS DE INGENIERÍA   ")
        print(f"        Tolerancia: {TOLERANCIA}")
        print("="*45)
        print("1. Caso 1: Dilatación (Bisección)")
        print("2. Caso 2: Refrigeración (Falsa Posición)")
        print("3. Caso 3: Reactancia (Newton-Raphson)")
        print("4. Caso 4: Resistencia (Secante)")
        print("5. Salir")
        
        opcion = input("\nSeleccione el caso a resolver: ")
        if opcion == '5': break
            
        try:
            m_iter = int(input("Máximo de iteraciones (Enter para 100): ") or 100)
            
            if opcion == '1':
                # Sugerido: a=1, b=10
                res = metodo_biseccion(f1, 1, 10, m_iter)
            elif opcion == '2':
                # Sugerido: a=0, b=100
                res = metodo_falsa_posicion(f2, 0, 100, m_iter)
            elif opcion == '3':
                # Sugerido: x0=2
                res = metodo_newton_raphson(f3, df3, 2, m_iter)
            elif opcion == '4':
                # Sugerido: x0=1, x1=1.5
                res = metodo_secante(f4, 1, 1.5, m_iter)
            else: 
                print("Opción no válida.")
                continue

            if res is not None: 
                print(f"\n--> RESULTADO FINAL: {res:.8f}")
            else: 
                print("\n[!] El método no convergió.")
        except Exception as e: 
            print(f"\n[!] Error: {e}")
        
        input("\nPresione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    menu()