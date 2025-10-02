# Ejercicio 26

##  Indique si las siguientes direcciones son de link-local, global-address, multicast, etc.
- fe80::1/64
    - Prefijo fe80::/10 → Dirección **Link-local**.
- 3ffe:4543:2:100:4398::1/64
    - Prefijo 3ffe::/16 → era espacio para 6bone (red experimental de pruebas, hoy obsoleta).
    - Actualmente dirección **global unicast** (experimental, ya no en uso).
- ::
    - Dirección **sin especificar**.
- ::1
    - Dirección **loopback**.
- ff02::2
    - Prefijo ff00::/8 → Dirección **multicast**.
    - El 02 en el scope indica link-local multicast.
    - " ::2 " es el grupo de todos los routers en la LAN.
- 2818:edbc:43e1::8721:122
    - Empieza con 2 → pertenece al rango 2000::/3.
    - Dirección **global unicast** (dirección pública en Internet).
- ff02::9
    - Prefijo ff00::/8 → Dirección **multicast**.
    - El 02 en el scope indica link-local multicast.
    - " ::9 " es el grupo reservado para Routing Information Protocol (RIP routers).