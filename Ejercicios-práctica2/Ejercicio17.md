# Ejercicio 17

## Indique qué funcionalidad difiere entre ICMP (sobre IPv4) e ICMPv6.

### ICMP en IPv4
- Funciones principales:
    - Diagnóstico (ping, traceroute).
    - Notificación de errores (Destination Unreachable, Time Exceeded, etc.).
    - Su papel es “secundario”. Esto significa que si se bloquea la recepción de paquetes ICMP por las configuraciones propias de la interfaz, la conectividad básica todavía puede funcionar.

### ICMP en IPv6
Además de diagnóstico y errores, en IPv6 ICMPv6 incorpora nuevas funcionalidades críticas para el funcionamiento del protocolo, ya que sin este protocolo la red no funcionaría a diferencia de IPv4:
- Descubrimiento de vecinos (Neighbor Discovery Protocol, NDP)
    - Sustituye a ARP de IPv4.
    - ICMPv6 maneja:
        - Resolución de direcciones IP ↔ MAC.
        - Detección de vecinos alcanzables.
        - Detección de direcciones duplicadas (DAD).
- Autoconfiguración de direcciones (SLAAC)
    - Los routers envían mensajes Router Advertisement (RA) (ICMPv6 Type 134).
    - Los hosts generan automáticamente su dirección IPv6 a partir de la red anunciada.
- Mensajes de Multicast Listener Discovery (MLD)
    - Equivalente al IGMP de IPv4.
    - Permite a los hosts comunicar a los routers que quieren recibir cierto tráfico multicast.