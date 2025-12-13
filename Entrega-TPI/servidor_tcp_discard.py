import socket

IP = '0.0.0.0'
PORT = 9000

# SOCK_STREAM indica TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, PORT))
sock.listen(1) # Escuchar conexiones entrantes

print(f"--- Servidor TCP DISCARD escuchando en el puerto {PORT} ---")

while True:
    print("Esperando conexión...")
    conn, addr = sock.accept() # Aceptamos la conexión (Handshake completo)
    print(f"Conexión establecida desde: {addr}")
    
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                # Si recv devuelve vacío, el cliente cerró la conexión (FIN)
                break 
            print(f"Recibido (y descartado): {len(data)} bytes") 
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
        print(f"Conexión cerrada con {addr}")