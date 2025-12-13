import socket
import threading
import time

IP_DESTINO = "46.90.19.194" 
PUERTO = 7

def crear_conexion(id_cliente):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP_DESTINO, PUERTO))
        # Obtenemos el puerto local aleatorio asignado por el SO
        puerto_origen = s.getsockname()[1]
        print(f"[Cliente {id_cliente}] Conectado desde puerto local {puerto_origen} -> Manteniendo sesión...")
        
        # Mantenemos la conexión abierta 15 segundos para dar tiempo a ver el netstat
        time.sleep(15)
        
        s.close()
        print(f"[Cliente {id_cliente}] Cerrando conexión.")
    except Exception as e:
        print(f"Error en cliente {id_cliente}: {e}")

print("--- Iniciando prueba de conexiones simultáneas ---")
hilos = []

# Generamos 4 conexiones simultáneas desde este mismo nodo
for i in range(1, 5):
    t = threading.Thread(target=crear_conexion, args=(i,))
    hilos.append(t)
    t.start()

# Esperamos a que terminen
for t in hilos:
    t.join()