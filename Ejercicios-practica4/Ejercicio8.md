# Ejercicio 8

## De acuerdo a la captura de la figura 1 indicar los valores de los campos que están difuminados (“blur”).

| Paquete (No.) | Campo / Columna | Valor Calculado |
| :---: | :--- | :--- |
| 1 | Info (Seq) | 3933822137 |
| 3 | Source | 172.20.1.1 |
| 3 | Destination | 172.20.1.100 |
| 3 | Info (Puertos) | 41749 > vce |
| 3 | Info (Flags) | [ACK] |
| 3 | Info (Seq) | 3933822138 |
| 3 | Info (Ack) | 1047471502 |

Porque el handshake TCP sigue:
- Cliente → Servidor: SYN
    - Seq = X
- Servidor → Cliente: SYN-ACK
    - Seq = Y
    - Ack = X + 1
- Cliente → Servidor: ACK
    - Seq = X + 1
    - Ack = Y + 1

Para este caso tenemos:
- X = 3933822137
- Y = 1047471501