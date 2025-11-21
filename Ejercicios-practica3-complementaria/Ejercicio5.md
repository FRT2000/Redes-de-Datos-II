# Ejercicio 5

## Analizar la captura de 02-dhcp.pcap. Compare los mensajes DHCP Request que encuentra en la misma y con la captura anterior. ¿Qué diferencias tienen a qué situaciones las asocia?

En la captura 01-dhcp, el cliente no tenía IP ni preferencia, por lo que inició el proceso DORA completo (4 mensajes) empezando con un Discover.

En esta captura 02-dhcp, el cliente inicia directamente con un DHCP Request que incluye la Opción 50 (Requested IP Address) con el valor 200.1.1.208.

Se asocia al estado INIT-REBOOT. El cliente reinicia, recuerda su última dirección IP y solicita verificarla directamente para reutilizarla. Al solicitar una IP específica, se omiten los mensajes Discover y Offer, reduciendo el intercambio a solo 2 pasos: Request y ACK.