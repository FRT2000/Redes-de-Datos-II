# Ejercicio 20

## ¿A qué dirección L2 (Layer 2 - Enlace de Datos) se envían los mensajes ARP Request? 
- Un ARP Request es una pregunta a toda la red local. Se envía en broadcast a nivel de enlace de datos.
- Dirección destino en Ethernet:
    - FF:FF:FF:FF:FF:FF -> Dirección MAC de broadcast.

---

## ¿Y los ARP Reply?
- Un ARP Reply es la respuesta de un host específico al que hizo la consulta.
- Se envía en unicast directamente a la dirección MAC del emisor que originó el ARP Request.