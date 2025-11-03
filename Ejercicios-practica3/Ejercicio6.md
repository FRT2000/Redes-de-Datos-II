# Ejercicio 6

## Fragmentación: se deben enviar un datagrama IPv4 de 1100B con un encabezado sin opciones a través de un link que soporta solo datagramas de 200B. Determine el offset y los bits de fragmentación de cada datagrama. Calcule el overhead (porcentaje de datos de cabecera sobre los datos totales) sobre una solución con MTU = 1500. ¿Es necesario hacer padding a nivel Ethernet en el último fragmento?

### Datos a considerar
- Longitud total del datagrama original incluyendo la cabecera = 1100 Bytes.
- Longitud mínima de cabecera IPv4 = 20 Bytes.
- MTU de la red = 200 Bytes.

#### Paso 1
Calcular cuántos datos útiles debemos enviar (Payload).

- 1100 Bytes (Total) - 20 Bytes (Cabecera) = 1080 Bytes

#### Paso 2
Calcular Payload máximo por cada fragmento respetando el MTU y la regla de 8 Bytes.

- Payload máximo descontando la cabecera: 200 Bytes (MTU) - 20 Bytes (Cabecera) = 180 Bytes
- Verificar regla de los 8 Bytes para desplazamiento (Offset): 180 / 8 = 22.5 -> No es múltiplo de 8
- Para obtener el Payload real que enviaremos, buscamos el múltiplo de 8 más cercano a 180: 22 x 8 = 176 Bytes

#### Paso 3
Calcular el número de fragmentos

- Fragmentos totales que se enviarán: 1080 (Datos útiles) / 176 (datos por fragmento) = 6.136
- Como el resultado no fue un número entero, redondeamos hacia arriba para obtener la cantidad total de fragmentos, lo que resulta en: 7 fragmentos.
- Se enviarán 6 fragmentos completos y 1 parcial.

#### Paso 4
Calcular el desplazamiento (Offset)

- Offset = payload / 8 = 176 / 8 = 22 -> Debemos realizar 22 desplazamientos por cada fragmento.

#### Paso 5
Armar los datagramas

| # Fragmento | Payload (Datos) | Longitud Total (Paquete) | Bit MF | Bit DF | Offset (Valor) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 176 bytes | 176 bytes + 20 bytes = 196 bytes | 1 | 0 | 0 |
| 2 | 176 bytes | 176 bytes + 20 bytes = 196 bytes | 1 | 0 | 22 |
| 3 | 176 bytes | 176 bytes + 20 bytes = 196 bytes | 1 | 0 | 44 |
| 4 | 176 bytes | 176 bytes + 20 bytes = 196 bytes | 1 | 0 | 66 |
| 5 | 176 bytes | 176 bytes + 20 bytes = 196 bytes | 1 | 0 | 88 |
| 6 | 176 bytes | 176 bytes + 20 bytes = 196 bytes | 1 | 0 | 110 |
| 7 (Último) | 24 bytes | 24 bytes + 20 bytes = 44 bytes | 0 | 0 |  132 |

---

### Cálculo de overhead con MTU = 1500
En este caso como el tamaño total del datagrama que se desea enviar (1100 Bytes) es menor que el MTU (1500 Bytes), no se produce fragmentación. El paquete se envía de una sola vez.

- Overhead: (Total de cabeceras) / (Total de datos)
- Total de cabeceras: 20 Bytes
- Total de datos: 1080 Bytes
- Cálculo de Overhead: 20 / 1080 = 0.0185 -> Expresado en porcentaje = 1.85% de Overhead

### Padding a nivel de Ethernet
- El tamaño mínimo de una trama Ethernet es de 64 bytes.
- El payload mínimo de Ethernet (los datos que transporta, es decir, el paquete IP) es de 46 bytes. (Esto es 64 bytes - 18 bytes de cabeceras Ethernet). 
- El último fragmento (Fragmento 7) tiene una longitud total de 44 bytes (24 de datos + 20 de cabecera). Como el paquete IP de 44 bytes es menor que el payload mínimo requerido de 46 bytes, es necesario hacer padding. Se agregarán 2 bytes de relleno (Padding) al paquete IP para que el payload de la trama alcance los 46 bytes mínimos, y así la trama total mida 64 bytes.