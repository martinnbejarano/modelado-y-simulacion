import sympy as sp

def evaluar_funcion(expr, x_valor, precision=8):
    """
    Evalúa una función f(x) en un valor específico de x.
    
    Parámetros:
        expr: Función a evaluar como string o expresión de sympy
        x_valor (float): Valor de x donde evaluar la función
        precision (int): Número de decimales para redondear el resultado
        
    Retorna:
        float: El resultado de evaluar f(x_valor)
    """
    try:
        x = sp.Symbol('x')
        # Verificar si la entrada es un string y convertirla si es necesario
        if isinstance(expr, str):
            expr = sp.sympify(expr)
        # Sustituir x por el valor numérico y evaluar
        resultado = expr.subs(x, x_valor).evalf(precision)
        return float(resultado)
    except Exception as e:
        print(f"Error al evaluar la función: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    x = sp.Symbol('x')
    
    # Función a evaluar como expresión sympy
    f_x = x**3 -  (3*sp.pi/2) * x**2  + (sp.pi**2 / 2) * x
    
    # Valor de x
    valor_x = 2.477696
    
    # Evaluar la función
    resultado = evaluar_funcion(f_x, valor_x)
    
    # Mostrar resultado
    print(f"f(x) = log(x - 1) + cos(x - 1)")
    print(f"f({valor_x}) = {resultado}")