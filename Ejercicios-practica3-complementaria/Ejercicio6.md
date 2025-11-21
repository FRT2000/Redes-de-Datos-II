# Ejercicio 6

## Analizando la captura 04-dhcp.pcap comparar el/los mensajes de Offer con los vistos en las capturas anteriores. ¿Qué diferencia tienen?

A diferencia de las capturas anteriores donde la oferta era estática, aquí el servidor ofrece direcciones IP distintas (.209 y .210) en mensajes Offer consecutivos para el mismo cliente (mismo Transaction ID).

La captura inicia con un DHCP Release de la IP .208. Los Offers posteriores respetan esa liberación y no vuelven a ofrecer la IP recién liberada, sino que asignan las siguientes disponibles en el pool.

Se observa que el servidor envía múltiples Offers porque el cliente retransmite múltiples Discovers, indicando una posible pérdida de paquetes o lentitud en el cliente para procesar la primera oferta.