from src.historial import guardar_operacion
def sumar(a,b) : return a + b
def restar(a,b) : return a - b
def multiplicar(a,b) : return a *b 
def dividir(a,b):
    if b==0:
       return "No es posible dividir para cero"
    return a/b

def sumar_y_guardar(a, b):
    resultado = sumar(a, b)
    guardar_operacion("suma", resultado)
    return resultado


print(sumar(5,5))

print(dividir(8,1))