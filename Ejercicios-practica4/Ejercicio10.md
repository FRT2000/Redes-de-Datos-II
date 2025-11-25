# Ejercicio 10

## Dadas las salidas de los siguientes comandos ejecutados en el cliente y el servidor, responder:

## ¿Qué paquetes llegaron y cuáles parecen que se están perdiendo en la red?

El paquete **SYN** (origen cliente -> destino servidor) llegó correctamente. El servidor no estaría en estado **SYN_RECV** si no hubiera recibido ese primer paquete **SYN**.

El paquete **SYN-ACK** (origen servidor -> destino cliente) se está perdiendo en el camino de vuelta (o está siendo bloqueado por un firewall). El cliente sigue "clavado" en estado **SYN_SENT**. Si el cliente hubiera recibido el **SYN-ACK**, habría pasado inmediatamente al estado **ESTABLISHED** (y enviado el ACK final). Al no cambiar de estado, significa que nunca vio la respuesta del servidor4.

## ¿Cómo quedará el estado en ambos lados si no logra establecerse la conexión?

**Lado del Servidor (srv):**

- El servidor intentará retransmitir el paquete SYN-ACK algunas veces. Si no recibe el ACK final antes del timeout, el servidor abortará la conexión incompleta y eliminará el socket de la memoria (o mejor dicho, el TCB - Transmission Control Block).
- Estado Final: El socket específico de esa conexión desaparecerá. El proceso servidor seguirá en estado LISTEN (escuchando nuevas peticiones en el puerto 4500).

**Lado del Cliente (cli):**
- El cliente eventualmente se cansará de esperar el SYN-ACK (timeout de conexión). La aplicación (como telnet o nc) recibirá un error de "Connection Timed Out".
- Estado Final: La conexión pasará al estado CLOSED (Cerrado) y desaparecerá de la lista de netstat.