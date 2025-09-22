# Ejercicio 16

## Describa qué es y para qué sirve ICMP. 
- ICMP = Internet Control Message Protocol (Protocolo de Mensajes de Control de Internet).
- Trabaja junto con IP (es parte de la capa de red en el modelo TCP/IP).
- No transporta datos de usuario, sino mensajes de diagnóstico, error y control.
- Lo usan los routers, switches y hosts para comunicarse sobre problemas de entrega de paquetes o para hacer pruebas de conectividad.

---

## ¿Qué hacen los comandos ping(8) y traceroute(1)? (tracert en Windows).
### ping(8)

- Envía paquetes ICMP Echo Request a una dirección destino.
- Si la máquina está activa y accesible, responde con ICMP Echo Reply.
- Sirve para probar conectividad de red (si un host responde, la red hasta allí funciona).

### traceroute(11) (tracert en Windows)
- Muestra el camino (los routers intermedios) que siguen los paquetes hasta un destino.
- Funciona enviando paquetes con el campo TTL (Time To Live) reducido.
    - Cuando un router decrementa el TTL a 0, responde con un mensaje ICMP Time Exceeded.
- traceroute repite este proceso aumentando el TTL, así descubre hop por hop los routers del camino.

---

## Indique el tipo y el código ICMP de un ping. Indique el tipo y el código ICMP de la respuesta de un ping. Indique el tipo y el código ICMP del cual se vale el comando traceroute para funcionar.

| Acción                             | Tipo | Código | Explicación                                 |
| ---------------------------------- | ---- | ------ | ------------------------------------------- |
| **Ping (Echo Request)**            | 8    | 0      | Solicitud de eco                            |
| **Respuesta de ping (Echo Reply)** | 0    | 0      | Respuesta de eco                            |
| **Traceroute (Time Exceeded)**     | 11   | 0      | Tiempo excedido en tránsito (TTL llegó a 0) |

---

## Estos comandos, ¿funcionan igual en Linux y en Windows? ¿En qué se diferencian si es que lo hacen? Hint: usar un “capturador” de tráfico como wireshark/tshark o tcpdump.
- Ping:
    - En Linux → ping manda paquetes ICMP directamente.
    - En Windows → ping también usa ICMP, pero los parámetros (ej. cantidad de paquetes, tamaño) difieren en la sintaxis del comando.
- Traceroute / Tracert:
    - En Linux → traceroute usa UDP por defecto, enviando datagramas a un puerto alto (33434+). Cuando llega al destino, devuelve un ICMP Port Unreachable.
    - Se puede forzar con traceroute -I para que use ICMP Echo Request.
    - En Windows → tracert usa directamente ICMP Echo Request (tipo 8).
    - Si realizamos capturas con Wireshark/tshark, observamos que Windows manda ICMP y Linux manda UDP (a menos que se coloque la opción -I).