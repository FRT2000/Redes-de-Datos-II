# Ejercicio 21

## Los mensajes ARP, ¿son re-enviados por los routers? Justifique.
Los mensajes ARP no son reenviados por los routers.

- ARP es un protocolo de resolución de direcciones dentro de una red local (LAN).
- Un router separa dominios de broadcast, es decir, no reenvía tramas de broadcast (como un ARP Request) hacia otras redes.
- Cada interfaz del router pertenece a una red distinta, con su propio espacio de direcciones IP y MAC.
- Por lo tanto:
    - Si un host en la red A necesita llegar a un host en la red B, no va a enviar un ARP para la IP del host remoto.
    - Solo resuelve por ARP la dirección MAC del router (gateway) en su red local.
    - Luego el router, en la red de destino, hará su propio ARP para averiguar la MAC del host final.
