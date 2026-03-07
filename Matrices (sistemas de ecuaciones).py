import numpy as np
from scipy.linalg import lu_factor, lu_solve

def resolver_sistemas_lu():
    # ==========================================
    # SISTEMA 1: Nodos Eléctricos
    # ==========================================
    A1 = np.array([
        [31,  3,  9,  1],
        [ 4, 31,  8,  4],
        [ 9,  1, 32,  5],
        [ 5,  3,  7, 25]
    ], dtype=float)
    b1 = np.array([171, 302, 316, 107], dtype=float)

    # Factorización LU: lu_factor devuelve (LU, pivote)
    lu1, piv1 = lu_factor(A1)
    # Resolución: Ly = b -> Ux = y
    V = lu_solve((lu1, piv1), b1)

    # ==========================================
    # SISTEMA 2: Red de Enfriamiento
    # ==========================================
    A2 = np.array([
        [21,  1,  1,  5],
        [ 5, 33,  4,  4],
        [ 4,  4, 35,  1],
        [ 2,  1,  1, 17]
    ], dtype=float)
    b2 = np.array([167, 166, 70, 135], dtype=float)

    # Factorización LU
    lu2, piv2 = lu_factor(A2)
    Q = lu_solve((lu2, piv2), b2)

    # ==========================================
    # SALIDA DE RESULTADOS (4 decimales)
    # ==========================================
    print("=== RESULTADOS VÍA DESCOMPOSICIÓN LU ===")
    print("\n[Sistema 1: Tensiones]")
    for i, val in enumerate(V):
        print(f"V{i+1} = {val:.4f}")

    print("\n[Sistema 2: Caudales]")
    for i, val in enumerate(Q):
        print(f"Q{i+1} = {val:.4f}")

if __name__ == "__main__":
    resolver_sistemas_lu()