import socket
import sys

# --- CONFIGURACIÓN ---
# IP del servidor (n9).
IP_SERVIDOR = "46.90.19.194" 
PUERTO = 7  # Puerto estándar del protocolo ECHO

# --- CREACIÓN DEL SOCKET ---
# socket.AF_INET = IPv4
# socket.SOCK_DGRAM = UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Configuramos un timeout de 2 segundos.
# Como UDP no avisa si falla, colocamos un timeout para que el programa
# no se quedue esperando para siempre si el paquete se pierde.
sock.settimeout(2)

mensaje = "Hola, soy el nodo " + socket.gethostname()

try:
    print(f"Enviando datos a {IP_SERVIDOR}:{PUERTO}...")
    
    # --- ENVIAR (SendTo) ---
    # Lanzamos el paquete (sendto)
    # indicando destino en el momento.
    sock.sendto(mensaje.encode(), (IP_SERVIDOR, PUERTO))

    # --- RECIBIR (RecvFrom) ---
    # Esperamos la respuesta.
    # buffer_size = 1024 bytes
    datos, direccion_servidor = sock.recvfrom(1024)
    
    print(f"¡Éxito! Recibí eco desde {direccion_servidor}: {datos.decode()}")

except socket.timeout:
    print("Error: Se agotó el tiempo de espera. El paquete se perdió o el puerto está cerrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    print("Cerrando socket.")
    sock.close()