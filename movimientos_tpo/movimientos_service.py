import json
import os
RUTA_JSON = "data/movimientos.json"

def cargar_movimientos(): 
    if not os.path.exists(RUTA_JSON):
        return []
    with open(RUTA_JSON, "r") as archivo:
        return json.load(archivo)
    
def guardar_movimientos(movimientos):
    with open(RUTA_JSON, "w") as archivo:
        json.dump(movimientos, archivo, indent=4)

def registrar_movimiento(id_producto, tipo, cantidad, fecha):
    """
    Registra un movimiento (Ingreso o Egreso).
    tipo: 'Ingreso' o 'Egreso' 
    fecha: formato 'YYYY-MM-DD'
    """
    movimientos = cargar_movimientos()
    
    nuevo_id = len(movimientos) + 1
    
    nuevo_movimiento = {
        "id_movimiento": nuevo_id,
        "id_producto": id_producto,
        "tipo": tipo,          # 'Ingreso' o 'Egreso' 
        "cantidad": cantidad,
        "fecha": fecha
    }
    
    movimientos.append(nuevo_movimiento)
    guardar_movimientos(movimientos)
    print(f"¡Movimiento de {tipo} registrado con éxito!")
    
    def listar_movimientos_por_fecha(fecha_buscada):
    """Lista los movimientos ocurridos en una fecha específica """
    movimientos = cargar_movimientos()
    filtrados = [m for m in movimientos if m['fecha'] == fecha_buscada]
    return filtrados

def calcular_ingreso_por_mes(mes, anio):
    """Calcula cuánto stock o cantidad ingresó en un determinado mes """
    movimientos = cargar_movimientos()
    total_ingresado = 0
    
    for m in movimientos:
        if m['tipo'].lower() == 'ingreso':
            partes_fecha = m['fecha'].split('-')
            if partes_fecha[0] == str(anio) and partes_fecha[1] == str(mes).zfill(2):
                total_ingresado += m['cantidad']
                
    return total_ingresado