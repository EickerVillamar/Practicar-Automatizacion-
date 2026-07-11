from src.calculadora import sumar,restar, multiplicar, dividir

def test_sumar_dos_numeros():
    resultado = sumar(2,3)
    assert resultado == 5
    
def test_restar_dos_numeros():
    resultado = restar(8,6)
    assert resultado == 2
    
def test_multiplicar():
    resultado = multiplicar(5,5)
    assert resultado == 25 
    
def test_dividir():
    resultado = dividir(8,0)
    assert resultado == "No es posible dividir para cero"
    

    