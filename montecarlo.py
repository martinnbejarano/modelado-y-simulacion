import numpy as np

# Semilla para reproducibilidad
np.random.seed(0)

# Definir función
def f(x, y):
    return np.exp(x - y)

# Parámetros
a, b = 0, 2
c, d = 0, 2
n = 10000

# Generar muestras uniformes
x_samples = np.random.uniform(a, b, n)
y_samples = np.random.uniform(c, d, n)

# Evaluar función en puntos aleatorios
f_values = f(x_samples, y_samples)

# Estimar la integral
area = (b - a) * (d - c)
media = np.mean(f_values)
integral_estimada = area * media

# Estadísticas
var_muestral = np.var(f_values, ddof=1)  
std_dev = np.std(f_values, ddof=1)
std_error = std_dev / np.sqrt(n)
conf_int = (integral_estimada - 1.96 * std_error, integral_estimada + 1.96 * std_error)

# Resultados
print(f"Integral estimada: {integral_estimada}")
print(f"Media muestral: {media}")
print(f"Varianza muestral: {var_muestral}")
print(f"Desviación estándar muestral: {std_dev}")
print(f"Error estándar: {std_error}")
print(f"Intervalo de confianza 95%: {conf_int}")
