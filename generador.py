import random
import datetime
import json
import time
import os

# --- CONFIGURACIÓN ---
TIENDAS = [
    {"nombre": "SuperMercado Central", "direccion": "Av. Principal 123, Centro"},
    {"nombre": "MiniMarket Express", "direccion": "Calle Secundaria 456, Norte"},
    {"nombre": "Tienda 24/7", "direccion": "Boulevard Comercial 789, Sur"},
    {"nombre": "Abarrotes Don Pepe", "direccion": "Plaza Mayor 101, Este"},
    {"nombre": "Bodega La Esquina", "direccion": "Calle Flores 202, Oeste"},
]
CARPETA_SALIDA = "facturas_generadas"
INTERVALO_MINUTOS = 15

def crear_carpeta_si_no_existe(carpeta):
    """Crea el directorio de salida si no existe."""
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f"📁 Carpeta creada: {carpeta}")

def generar_factura_final():
    """
    Genera una factura con datos únicos y la guarda en la carpeta destino.
    """
    # 1. Datos Dinámicos
    id_factura = random.randint(100000, 999999)
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Seleccionar tienda aleatoria
    tienda = random.choice(TIENDAS)

    # Aleatorizamos si se puede devolver o no en cada venta
    admite_devolucion = random.choice([True, False])

    # 2. Estructura JSON
    datos_factura = {
        "id": id_factura,
        "encabezado": {
            "tienda": tienda["nombre"],
            "direccion": tienda["direccion"],
            "fecha_emision": fecha_actual
        },
        "condiciones": {
            "admite_devolucion": admite_devolucion,
            "texto_legal": "Devolución permitida en 15 días" if admite_devolucion else "Venta final, sin devoluciones"
        }
    }
    
    # 3. Guardado del archivo
    nombre_archivo = f"factura_{id_factura}.json"
    ruta_completa = os.path.join(CARPETA_SALIDA, nombre_archivo)
    
    try:
        with open(ruta_completa, "w", encoding="utf-8") as archivo:
            json.dump(datos_factura, archivo, indent=4, ensure_ascii=False)
        return nombre_archivo, fecha_actual
    except Exception as e:
        print(f"❌ Error al escribir archivo: {e}")
        return None, None

# --- BUCLE PRINCIPAL ---
if __name__ == "__main__":
    crear_carpeta_si_no_existe(CARPETA_SALIDA)
    
    segundos_espera = INTERVALO_MINUTOS * 60
    
    print(f"--- 🤖 INICIANDO SISTEMA DE FACTURACIÓN ---")
    print(f"📌 Tiendas disponibles: {len(TIENDAS)}")
    print(f"⏱️  Frecuencia: Una factura cada {INTERVALO_MINUTOS} minutos")
    print(f"📂 Guardando en: ./{CARPETA_SALIDA}/")
    print("🔴 Presiona CTRL + C para detener el programa.\n")

    try:
        while True:
            # Generar factura
            archivo, hora = generar_factura_final()
            
            if archivo:
                print(f"[{hora}] ✅ Factura creada: {archivo}")
            
            # Cuenta regresiva simple para feedback visual
            print(f"💤 Durmiendo... Próxima factura en {INTERVALO_MINUTOS} minutos.")
            time.sleep(segundos_espera)

    except KeyboardInterrupt:
        print("\n\n🛑 Ejecución detenida por el usuario. ¡Hasta pronto!") 