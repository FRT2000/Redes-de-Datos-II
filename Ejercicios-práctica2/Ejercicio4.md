# Ejercicio 4

## ¿Cuál es la función de la máscara de red? 
La máscara de red es un número binario de 32 bits (en IPv4) que indica qué parte de la dirección IP corresponde a la red y qué parte a los hosts.

Por ejemplo:

IP:      192.168.1.10

Máscara: 255.255.255.0

En binario:

IP:      11000000.10101000.00000001.00001010

Máscara: 11111111.11111111.11111111.00000000

Los unos (1) en la máscara representan los bits de la red.

Los ceros (0) representan los bits de host.

---

## ¿Qué otra notación alternativa se puede utilizar?
La notación CIDR (Classless Inter-Domain Routing) indica cuántos bits de la dirección IP corresponden a la porción de red usando una barra "/".

### Ejemplos según la clase de red

| Clase | Ejemplo de IP | Máscara tradicional | Notación CIDR   |
| ----- | ------------- | ------------------- | --------------- |
| A     | 10.0.0.1      | 255.0.0.0           | 10.0.0.1/8      |
| B     | 172.16.5.10   | 255.255.0.0         | 172.16.5.10/16  |
| C     | 192.168.1.20  | 255.255.255.0       | 192.168.1.20/24 |

---

## ¿Cuál se utiliza en IPv6 y por qué?
En IPv6, la máscara se indica solo con notación CIDR, por ejemplo:

2001:0db8:85a3::8a2e:0370:7334/64

IPv6 no utiliza la notación decimal de 32 bits porque las direcciones son de 128 bits, mucho más largas y complejas.

Usar CIDR simplifica la escritura y lectura de las subredes en IPv6.