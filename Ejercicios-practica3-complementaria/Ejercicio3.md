# Ejercicio 3

## Para el diagrama de la figura 1 indicar para la red C y D. 

### ¿Qué equipo podría cumplir rol de servidor de DHCP para ambas redes, qué configuración podría tener ?

Lo más sencillo sería el router que une ambas redes (Red C y Red D).

Para que funcione, se debería configurar en el router dos pools de DHCP distintos, uno para cada interfaz/subred:

- Pool para Red C:
    - Network: 10.10.3.0
    - Máscara: 255.255.255.0 (/24)
    - Default Gateway: 10.10.3.1 (Asumiendo IP del router en esa interfaz).

- Pool para Red D:
    - Network: 192.168.0.0
    - Máscara: 255.255.255.0 (/24)
    - Default Gateway: 192.168.0.1 (Asumiendo IP del router en esa interfaz).

Al estar conectado directamente a ambas, el router recibe Broadcasts de los clientes de ambos lados y les asigna la IP correspondiente.

### ¿Podría estar el servidor DHCP en el equipo con la IP 10.10.3.10 ? Indique que consideraciones habría que hacer para que funcione como tal.

Si. Un servidor DHCP puede ser un dispositivo dedicado (como un servidor Linux/Windows o ese equipo 10.10.3.10) ubicado en cualquier parte de la red.

Se debe admitir DHCP Relay Agent (Agente de Retransmisión). Para que el servidor en 10.10.3.10 pueda dar IPs a la Red D, se debe configurar un DHCP Relay en la interfaz del router que conecta con la Red D.

En el Servidor (10.10.3.10): Debe tener configurados los dos ámbitos (Scopes/Pools), uno para la 10.10.3.0 y otro para la 192.168.0.0, aunque él no pertenezca a esa red.   