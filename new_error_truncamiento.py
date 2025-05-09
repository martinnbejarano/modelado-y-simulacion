import sympy as sp
 
x=sp.Symbol('x')
 
#funcion
f=(1/sp.sqrt(2))*(x**(2*x))
 
#Parametros
a, b, n, x0= 0, 1, 4, 0.5
 
#Derivada enesima, ejemplo 2ta
fn1=sp.diff(f,x, 2)
#Derivada enesima, ejemplo 4ta
fn2=sp.diff(f,x, 4)
 
#evaluacion en un x=x0, ejemplo x=1
resultado1=fn1.evalf(subs={x:x0})
resultado2=fn2.evalf(subs={x:x0})
 
#errores de truncamiento
et1=-(b-a)**3/(12*n**2)*resultado1
et2=-(b-a)**5/(180*n**4)*resultado2
 
#print(f"deriva 2: {fn1}")
print(f"error de truncamiento trapecio : {et1}")
#print(f"deriva 4: {fn2}")
print(f"error de truncamiento Simpson : {et2}")