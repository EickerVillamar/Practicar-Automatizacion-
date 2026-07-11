historial = []

def guardar_operacion(nombre,resultado):
    historial.append({
        "nombre" : nombre,
        "resultado" : resultado 
    })
    
def obtener_historial():
    return historial