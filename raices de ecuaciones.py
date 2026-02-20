import numpy as np
import os

# ZONA DE EDICIÓN DE FUNCIONES (MODIFICAR)


def f(x: float) -> float:
    return x**3 - 2*x - 5
    """ 
    Escribe aquí tu función f(x).
    Ejemplos:
    - Polinomio x^3 - 2x - 5  --> return x**3 - 2*x - 5
    - Exponencial e^-x - x    --> return np.exp(-x) - x
    - Trigonométrica sen(x)   --> return np.sin(x)
    """
    return np.exp(-x) - x  

def df(x: float) -> float:
    return 3*x**2 -2
    """ 
    Escribe aquí la DERIVADA f'(x) (Solo para Newton-Raphson).
    Ejemplo de e^-x - x:
    f'(x) = -e^-x - 1         --> return -np.exp(-x) - 1
    """
    return -np.exp(-x) - 1 


TOLERANCIA = 1e-5


def metodo_biseccion(func, a, b, max_iter):
    if func(a) * func(b) >= 0:
        print("\n[!] Error: f(a) y f(b) deben tener signos opuestos.")
        return None
    xr, xr_old, ea, i = 0.0, a, 100.0, 0
    print(f"\n{'Iter':<5} {'a':<10} {'b':<10} {'xr':<10} {'Error %':<10}")
    while ea >= TOLERANCIA and i < max_iter:
        xr = (a + b) / 2
        ea = abs((xr - xr_old) / xr) * 100 if xr != 0 else 0
        print(f"{i+1:<5} {a:<10.5f} {b:<10.5f} {xr:<10.5f} {ea:<10.5f}%")
        if func(a) * func(xr) < 0: b = xr
        else: a = xr
        xr_old, i = xr, i + 1
    return xr

def metodo_falsa_posicion(func, a, b, max_iter):
    if func(a) * func(b) >= 0:
        print("\n[!] Error: f(a) y f(b) deben tener signos opuestos.")
        return None
    xr, xr_old, ea, i = 0.0, a, 100.0, 0
    print(f"\n{'Iter':<5} {'a':<10} {'b':<10} {'xr':<10} {'Error %':<10}")
    while ea >= TOLERANCIA and i < max_iter:
        xr = b - (func(b) * (a - b)) / (func(a) - func(b))
        ea = abs((xr - xr_old) / xr) * 100 if xr != 0 else 0
        print(f"{i+1:<5} {a:<10.5f} {b:<10.5f} {xr:<10.5f} {ea:<10.5f}%")
        if func(a) * func(xr) < 0: b = xr
        else: a = xr
        xr_old, i = xr, i + 1
    return xr

def metodo_newton_raphson(func, dfunc, x0, max_iter):
    xi, ea, i = x0, 100.0, 0
    print(f"\n{'Iter':<5} {'xi_next':<15} {'Error %':<15}")
    while ea >= TOLERANCIA and i < max_iter:
        dfx = dfunc(xi)
        if dfx == 0: return None
        xi_next = xi - (func(xi) / dfx)
        ea = abs((xi_next - xi) / xi_next) * 100 if xi_next != 0 else 0
        print(f"{i+1:<5} {xi_next:<15.8f} {ea:<15.8f}%")
        xi, i = xi_next, i + 1
    return xi

def metodo_secante(func, x0, x1, max_iter):
    ea, i = 100.0, 0
    print(f"\n{'Iter':<5} {'xi+1':<15} {'Error %':<15}")
    while ea >= TOLERANCIA and i < max_iter:
        f0, f1 = func(x0), func(x1)
        if f1 - f0 == 0: return None
        x_next = x1 - (f1 * (x1 - x0)) / (f1 - f0)
        ea = abs((x_next - x1) / x_next) * 100 if x_next != 0 else 0
        print(f"{i+1:<5} {x_next:<15.8f} {ea:<15.8f}%")
        x0, x1, i = x1, x_next, i + 1
    return x1

# =================================================================
# 4. INTERFAZ DE USUARIO (MENÚ)
# =================================================================

def menu():
    while True:
        print("\n" + "="*45)
        print("   MÉTODOS NUMÉRICOS: RAÍCES DE ECUACIONES   ")
        print(f"       Tolerancia Actual: {TOLERANCIA}")
        print("="*45)
        print("1. Bisección")
        print("2. Falsa Posición")
        print("3. Newton-Raphson")
        print("4. Secante")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        if opcion == '5': break
            
        try:
            m_iter = int(input("Máximo de iteraciones (Enter para 100): ") or 100)
            if opcion == '1' or opcion == '2':
                a, b = float(input("Límite a: ")), float(input("Límite b: "))
                res = metodo_biseccion(f, a, b, m_iter) if opcion == '1' else metodo_falsa_posicion(f, a, b, m_iter)
            elif opcion == '3':
                x0 = float(input("Punto inicial (x0): "))
                res = metodo_newton_raphson(f, df, x0, m_iter)
            elif opcion == '4':
                x0, x1 = float(input("x0: ")), float(input("x1: "))
                res = metodo_secante(f, x0, x1, m_iter)
            else: continue

            if res is not None: print(f"\n--> RESULTADO: Raíz aproximada = {res:.8f}")
            else: print("\n[!] El método no convergió o hubo error matemático.")
        except Exception as e: print(f"\n[!] Error: {e}")
        
        input("\nPresione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":

    menu()
