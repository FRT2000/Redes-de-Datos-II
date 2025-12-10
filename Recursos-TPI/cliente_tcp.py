import socket
import sys
import time

# Uso: python3 cliente_tcp.py <IP> <PUERTO> <MENSAJE>
if len(sys.argv) < 3:
    print("Uso: python3 cliente_tcp.py <IP> <PUERTO> [MENSAJE]")
    sys.exit(1)

IP = sys.argv[1]
PORT = int(sys.argv[2])
MSG = sys.argv[3] if len(sys.argv) > 3 else "Hola TCP"

try:
    # 1. Crear socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print(f"Intentando conectar a {IP}:{PORT}...")
    # 2. Conectar (Esto dispara el 3-way Handshake: SYN -> SYN/ACK -> ACK)
    sock.connect((IP, PORT))
    print("Estado: ESTABLISHED (Conexión establecida)")

    # 3. Enviar datos (PUSH)
    print(f"Enviando: {MSG}")
    sock.sendall(MSG.encode())

    # 4. Recibir respuesta
    sock.settimeout(2) # Timeout para no bloquearnos en Discard
    try:
        data = sock.recv(1024)
        if data:
            print(f"Recibido: {data.decode()}")
        else:
            print("El servidor no envió nada (Comportamiento normal de Discard).")
    except socket.timeout:
        print("Timeout: El servidor no respondió (Comportamiento normal de Discard).")

    # 5. Cerrar (Esto dispara el cierre: FIN -> ACK ...)
    print("Cerrando conexión...")
    sock.close()

except Exception as e:
    print(f"Error: {e}")