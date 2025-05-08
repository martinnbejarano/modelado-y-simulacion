import sympy as sp
from evaluar import evaluar_funcion

def derivar_evaluar(expr, orden, x_valor, precision=8):
    """
    Deriva una función hasta un orden especificado y la evalúa en un valor x.
    
    Parámetros:
        expr: Función a derivar como string o expresión de sympy
        orden (int): Orden de la derivada (1 para primera derivada, 2 para segunda, etc.)
        x_valor (float): Valor de x donde evaluar la derivada
        precision (int): Número de decimales para redondear el resultado
        
    Retorna:
        float: El resultado de evaluar la derivada en x_valor
    """
    try:
        x = sp.Symbol('x')
        # Verificar si la entrada es un string y convertirla si es necesario
        if isinstance(expr, str):
            expr = sp.sympify(expr)
            
        # Calcular la derivada
        derivada = expr
        for i in range(orden):
            derivada = sp.diff(derivada, x)
            
        # Mostrar la expresión de la derivada
        print(f"Derivada de orden {orden}: {sp.pretty(derivada)}")
            
        # Evaluar la derivada en el punto x
        resultado = evaluar_funcion(derivada, x_valor, precision)
        return resultado
    except Exception as e:
        print(f"Error al derivar o evaluar la función: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    x = sp.Symbol('x')
    
    # Función a derivar y evaluar
    f_x = sp.sin(x) / (x + sp.log(x + 1))
    
    # Valor de x y orden de la derivada
    valor_x = 0.5
    orden_derivada = 4  # Segunda derivada
    
    # Derivar y evaluar
    resultado = derivar_evaluar(f_x, orden_derivada, valor_x)
    
    # Mostrar resultado
    print(f"\nf(x) = sin(x) * exp(x)")
    print(f"f^({orden_derivada})({valor_x}) = {resultado}")
    
