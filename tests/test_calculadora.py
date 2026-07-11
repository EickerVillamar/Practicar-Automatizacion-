from src.calculadora import sumar,restar

def test_sumar_dos_numeros():
    resultado = sumar(2,3)
    assert resultado == 5
    
def test_restar_dos_numeros():
    resultado = restar(8,6)
    assert resultado == 2
    

    