from src.calculadora import dividir


def test_regresion_dividir_por_cero_no_rompe():
    resultado = dividir(10, 0)

    assert resultado == "No es posible dividir para cero"