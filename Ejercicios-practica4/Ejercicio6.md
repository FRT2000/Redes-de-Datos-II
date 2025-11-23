# Ejercicio 6

## Un proceso desde 10.0.0.10 inicia una conexión TCP, por ejemplo mediante el comando telnet, hacia un servidor 192.168.1.10. Al mismo tiempo otro proceso desde 10.0.0.10 inicia otra conexión TCP hacia el mismo servicio. Ambas conexiones se establecen.

## Indicar direcciones y números de puerto origen y destino de la primera conexión.

Cuando un cliente inicia una conexión, el Sistema Operativo le asigna un puerto efímero (source port) libre. El puerto destino es el puerto estándar del servicio ("Well-known port").
- Dirección IP Origen: 10.0.0.10
- Puerto Origen: 1038.
- Dirección IP Destino: 192.168.1.10
- Puerto Destino: 23 (Telnet es el puerto 23 por defecto).

## Indicar direcciones y números de puerto origen y destino para la segunda conexión.

Aunque la IP origen y la IP destino son las mismas, el Puerto Origen debe cambiar para que la tupla de identificación (Socket) sea única.
- Dirección IP Origen: 10.0.0.10
- Puerto Origen: 1039 (Debe ser distinto al anterior).
- Dirección IP Destino: 192.168.1.10
- Puerto Destino: 23

## Si genera una nueva conexión desde 10.0.0.11 hacia el mismo servicio, indicar direcciones y números de puerto origen y destino utilizados.

Al venir de una IP diferente, el puerto origen podría repetirse con respecto a las conexiones del host anterior, ya que la combinación IP:Puerto será única globalmente.
- Dirección IP Origen: 10.0.0.11
- Puerto Origen: 1038 (Puede ser cualquiera asignado por su SO).
- Dirección IP Destino: 192.168.1.10
- Puerto Destino: 23

Una conexión TCP se identifica por la quíntupla: (Protocolo, IP_Local, Puerto_Local, IP_Remota, Puerto_Remoto). Mientras un valor cambie, la conexión es distinta.

## Indicar la cantidad de segmentos TCP transmitidos en total.

Asumiendo que el enunciado se refiere al establecimiento (Handshake) de las 3 conexiones mencionadas: 
- Cada conexión TCP requiere un saludo de 3 vías (3-Way Handshake).
    - SYN
    - SYN, ACK
    - ACK
- Cálculo: 3 conexiones x 3 segmentos = 9 segmentos.

## Indicar los “flags” que se verán en los segmentos TCP transmitidos.

Durante el ciclo de vida descrito (establecimiento y supuesta transferencia/cierre), se verán los siguientes flags (bits de control):
- SYN (Synchronize): Para iniciar la conexión (sincronizar números de secuencia).
- ACK (Acknowledgment): Para confirmar la recepción de segmentos (presente en casi todos los paquetes después del SYN inicial).
- PSH (Push): Generalmente usado cuando se envían datos (el "1 byte" mencionado) para que pasen rápido a la aplicación, aunque es opcional.
- FIN (Finish): Para solicitar el cierre de la conexión.

## Indicar cantidad de segmentos TCP totales (inicio, datos y cierre) en caso que solo dos conexiones transmiten 1 byte c/u y luego cierran las 3.

Escenario: 3 conexiones se establecen. Solo 2 transmiten datos (1 byte ida y vuelta, se asume "c/u" como cliente envía y servidor responde). Luego, las 3 se cierran.

Desglose por Conexión Activa (Conexiones 1 y 2):
- Establecimiento: 3 segmentos (SYN, SYN-ACK, ACK).
- Transferencia de Datos: 4 segmentos (caso estándar sin piggybacking o delayed ACK):
    - Cliente -> Servidor: Datos (1B) + PSH, ACK
    - Servidor -> Cliente: ACK
    - Servidor -> Cliente: Datos (1B) + PSH, ACK
    - Cliente -> Servidor: ACK
- Cierre: 4 segmentos (FIN, ACK, ACK, FIN, ACK, ACK)
    - Total conexión activa: 3 + 4 + 4 = 11 segmentos.
    
Desglose por Conexión Inactiva (Conexión 3):
- Establecimiento: 3 segmentos.
- Transferencia: 0 segmentos.
- Cierre: 4 segmentos.Total conexión inactiva: 3 + 0 + 4 = 7 segmentos.

Total General: (11 x 2) + 7 = 29 segmentos TCP.

## Indicar la cantidad de datagramas transmitidos en caso de que las transferencias se realicen utilizando UDP.

UDP es un protocolo sin conexión.
- No hay Handshake (0 datagramas).
- No hay Cierre/Teardown (0 datagramas).
- Solo hay envío de datos.

Si 2 conexiones transmiten 1 byte c/u (ida y vuelta):
- Conexión 1: 1 datagrama (ida) + 1 datagrama (vuelta) = 2.
- Conexión 2: 1 datagrama (ida) + 1 datagrama (vuelta) = 2.
- Conexión 3: 0 datagramas (no transmite).

Total: 4 datagramas UDP.

## Hacer una simulación de los escenarios, con nc (netcat) o telnet.

Se realizó la siguiente topología y el uso de wireshark para la visualización de los escenarios.

![Topología inciso h](/Recursos-practica4/Ejercicio6-Inciso-h.png)

A continuación los comandos utilizados en cada dispositivo:

**Server** -> Usamos dos terminales para escuchar en el puerto 23 y visualizar las conexiones establecidas. 
- `nc -l -p 23 -v -k -n` -> en Terminal 1
- `netstat -tanp | grep :23` -> en Terminal 2

**PC1** -> Usamos dos terminales para generar dos conexiones con la misma IP pero diferente puerto en el servidor.
- `nc 192.168.1.10 23` -> Terminal 1 (Proceso A)
- `nc 192.168.1.10 23` -> Terminal 2 (Proceso B)

**PC2** -> Usamos solamente una terminal, ya que solo estableceremos conexión.
- `nc 192.168.1.10 23`