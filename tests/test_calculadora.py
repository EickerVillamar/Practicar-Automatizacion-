from src.calculadora import sumar,restar, multiplicar, dividir

def test_sumar_dos_numeros():
    # Preparar
    a = 2
    b = 3
    # Ejecutar
    resultado = sumar(a, b)
    # Comprobar
    assert resultado == 5

def test_sumar_valores_negativos():
    a = -5
    b = -6
    
    resultado = sumar(a,b)
    
    assert resultado == -11
    
def test_sumar_con_ceros():
    a = 10
    b = 0
    resultado = sumar(a,b)
    assert resultado == 10


def test_restar_dos_numeros():
    resultado = restar(8,6)
    assert resultado == 2
    
def test_multiplicar():
    resultado = multiplicar(5,5)
    assert resultado == 25 
    
def test_dividir():
    resultado = dividir(8,0)
    assert resultado == "No es posible dividir para cero"
    

    