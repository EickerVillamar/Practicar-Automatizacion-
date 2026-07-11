from src.calculadora import sumar, sumar_y_guardar
from src.historial import guardar_operacion, obtener_historial, historial


def test_sumar_y_guardar_en_historial():
    # Preparar
    historial.clear()

    # Ejecutar
    resultado = sumar(2, 3)
    guardar_operacion("suma", resultado)

    # Comprobar
    registros = obtener_historial()

    assert len(registros) == 1
    assert registros[0]["nombre"] == "suma"
    assert registros[0]["resultado"] == 5
    

def test_sumar_y_guardar_usando_funcion_integrada():
    # Preparar
    historial.clear()

    # Ejecutar
    resultado = sumar_y_guardar(4, 6)

    # Comprobar
    registros = obtener_historial()

    assert resultado == 10
    assert len(registros) == 1
    assert registros[0]["nombre"] == "suma"
    assert registros[0]["resultado"] == 10