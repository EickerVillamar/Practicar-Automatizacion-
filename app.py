from src.calculadora import sumar_y_guardar
from src.historial import obtener_historial


def main():
    print("Aplicacion iniciada")

    resultado = sumar_y_guardar(2, 3)
    print(f"Resultado de la suma: {resultado}")

    historial = obtener_historial()
    print(f"Operaciones guardadas: {len(historial)}")

    print("Aplicacion finalizada")


if __name__ == "__main__":
    main()