import random
import datetime
import json
import time
import os

# --- CONFIGURACIÓN ---
TIENDAS = [
    {"nombre": "SuperMercado Central", "direccion": "Calle Colón 25, Valencia"},
    {"nombre": "MiniMarket Express", "direccion": "Av. del Puerto 128, Valencia"},
    {"nombre": "Tienda 24/7", "direccion": "Gran Vía Marqués del Turia 56, Valencia"},
    {"nombre": "Ultramarinos Don José", "direccion": "Calle de la Paz 42, Valencia"},
    {"nombre": "Bodega La Esquina", "direccion": "Av. Blasco Ibáñez 73, Valencia"},
]
CARPETA_SALIDA = "facturas_generadas"
INTERVALO_MINUTOS = 10

def crear_carpeta_si_no_existe(carpeta):
    """Crea el directorio de salida si no existe."""
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f" Carpeta creada: {carpeta}")

def generar_factura_final():
    """
    Genera una factura con datos únicos y la guarda en la carpeta destino.
    """
    # 1. Datos Dinámicos
    id_factura = random.randint(100000, 999999)
    momento_compra = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Seleccionar tienda aleatoria
    tienda = random.choice(TIENDAS)

    # Precio aleatorio entre 1 y 500 euros
    precio = round(random.uniform(1.00, 500.00), 2)

    # 2. Estructura JSON
    datos_factura = {
        "id": id_factura,
        "tienda": tienda["nombre"],
        "direccion": tienda["direccion"],
        "precio": precio,
        "momento_compra": momento_compra
    }
    
    # 3. Guardado del archivo
    nombre_archivo = f"factura_{id_factura}.json"
    ruta_completa = os.path.join(CARPETA_SALIDA, nombre_archivo)
    
    try:
        with open(ruta_completa, "w", encoding="utf-8") as archivo:
            json.dump(datos_factura, archivo, indent=4, ensure_ascii=False)
        return nombre_archivo, momento_compra
    except Exception as e:
        print(f"Error al escribir archivo: {e}")
        return None, None

# --- BUCLE PRINCIPAL ---
if __name__ == "__main__":
    crear_carpeta_si_no_existe(CARPETA_SALIDA)
    
    segundos_espera = INTERVALO_MINUTOS * 60
    
    print(f"INICIANDO SISTEMA DE FACTURACIÓN AUTOMÁTICA")
    print(f"Tiendas disponibles: {len(TIENDAS)}")
    print(f"Frecuencia: Una factura cada {INTERVALO_MINUTOS} minutos")
    print(f"Guardando en: ./{CARPETA_SALIDA}/")
    print("Presiona CTRL + C para detener el programa.\n")

    try:
        while True:
            # Generar factura
            archivo, hora = generar_factura_final()
            
            if archivo:
                print(f"[{hora}] Factura creada: {archivo}")
            
            # Cuenta regresiva simple para feedback visual
            print(f"Esperando... Próxima factura en {INTERVALO_MINUTOS} minutos.")
            time.sleep(segundos_espera)

    except KeyboardInterrupt:
        print("\n\nEjecución detenida por el usuario. ¡Hasta pronto!") 