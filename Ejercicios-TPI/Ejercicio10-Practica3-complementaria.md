# Ejercicio 10 de la Práctica 3 complementaria

## Al ejercicio presentado en la práctica 3 agregar una red con 40 hosts detrás del router n15. La misma debe soportar IPv6 e IPv4. Para IPv6 activar en el router los RA y entregar RDNSS. Capturar tráfico y analizar. Comparar con los mensajes DHCP. Comparar la funcionalidad del SLAAC con los RA y DHCPv6. Alternativo: activar DHCPv6 en la red.

### Red n15 de 40 hosts

Recordando las direcciones disponibles del Ejercicio 13 de la práctica 3:

`46.90.16.0` hasta `46.90.19.143` quedan libres para seguir subneteando.

46.90.19.143 -> Red de la cual partimos.

0010 1110.0101 1010.0001 0011.1000 1111 -> red expresada en bits

0010 1110.0101 1010.0001 0011.10|**00 0000**| -> Colocamos en cero los bits que necesitamos para hosts.

0010 1110.0101 1010.0001 0|**011.10**|00 0000 -> Bits tomados para subred.

La nueva máscara de subred será /26

46.90.19.128/26 -> La red choca con las direcciones que hemos asignado con los enlaces punto a punto

Entonces elijos el próximo bloque de direcciones disponible

0010 1110.0101 1010.0001 0|**011.01**|00 0000 -> Próxima red disponible para los 40 hosts.

46.90.19.64/26 -> **Dirección IP asignada para la red n15**

Finalmente las direcciones: `46.90.16.0` hasta `46.90.19.63` quedan libres para seguir subneteando.

### Direcciones IPv6 asignadas con el bloque asignado 2001:db81::/32

**Asignación para la Red de n15: 2001:db81:000B:0001::/64**

