# Ejercicio 7

## Fragmentación: dada la configuración de la figura 3 donde entre n1 y n2 se tiene un MTU=1500 y entre n2 y n3 un MTU=400. Se asume que los frames de link layer requieren 18 bytes de overhead y los datagramas IPv4 20 bytes. Por 1000 bytes de datos que envía n1 a n3, ¿cuántos bytes en total, incluyendo el overhead, se van a transmitir entre n2 y n3?

## Transmisión de datos de n1 a n2

### Datos a considerar
- Longitud total del datagrama original = 1000 Bytes.
- Longitud de cabecera IPv4 = 20 Bytes.
- Overhead frames de link layer entre nodos = 18 Bytes.
- MTU de la red = 1500 Bytes.

### Calcular el total de Bytes a transmitir en el enlace
- Longitud total de la trama: (Bytes de datos útiles) + (Bytes de cabecera IPv4) + (Bytes overhead entre nodos)
- Cálculo de la longitud total: 1000 Bytes + 20 Bytes + 18 Bytes = 1038 Bytes
- Como el MTU de la red es de 1500 Bytes, el paquete viaja sin fragmentar hasta n2.

## Transmisión de datos de n2 a n3

### Datos a considerar
- Longitud total del datagrama original = 1000 Bytes.
- Longitud de cabecera IPv4 = 20 Bytes.
- Overhead frames de link layer entre nodos = 18 Bytes.
- MTU de la red = 400 Bytes.

#### Paso 1
Calcular cuántos datos útiles debemos enviar (Payload).

- El ejercicio nos dice que la cantidad de datos útiles a enviar es de 1000 Bytes.

#### Paso 2
Calcular Payload máximo por cada fragmento respetando el MTU y la regla de 8 Bytes.

- Payload máximo descontando la cabecera: 400 Bytes (MTU) - 20 Bytes (Cabecera) - 18 Bytes (overhead entre nodos) = 362 Bytes
- Verificar regla de los 8 Bytes para desplazamiento (Offset): 362 / 8 = 45.25 -> No es múltiplo de 8
- Para obtener el Payload real que enviaremos, buscamos el múltiplo de 8 más cercano a 180: 45 x 8 = 360 Bytes

#### Paso 3
Calcular el número de fragmentos

- Fragmentos totales que se enviarán: 1000 (Datos útiles) / 360 (datos por fragmento) = 2.77
- Como el resultado no fue un número entero, redondeamos hacia arriba para obtener la cantidad total de fragmentos, lo que resulta en: 3 fragmentos.
- Se enviarán 2 fragmentos completos y 1 parcial.

#### Paso 4
Calcular el desplazamiento (Offset)

- Offset = payload / 8 = 360 / 8 = 45 -> Debemos realizar 45 desplazamientos por cada fragmento.

#### Paso 5
Armar los datagramas

| # Fragmento | Payload (Datos) | Longitud Total (Paquete) | Bit MF | Bit DF | Offset (Valor) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 360 bytes | 360 bytes + 20 bytes + 18 bytes = 398 bytes | 1 | 0 | 0 |
| 2 | 360 bytes | 360 bytes + 20 bytes + 18 bytes = 398 bytes | 1 | 0 | 45 |
| 3 (último) | 360 bytes | 280 bytes + 20 bytes + 18 bytes = 318 bytes | 0 | 0 | 90 |

Si sumamos la cantidad de Bytes transmitidas en cada paquete obtenemos: 1114 Bytes transmitidos de n2 a n3.

## ¿Qué sucedería si los mensajes se envían con el bit de DF = 1?

- El paquete original de 1038 bytes llegaría a n2 sin problemas.
- n2 intentaría enviarlo por el enlace a n3.
- n2 determinaría que el paquete es más grande que el tamaño máximo permitido en ese enlace. Al ser un router, n2 revisaría los bits de fragmentación. Al ver el bit DF=1, se da cuenta de que tiene prohibido fragmentar el paquete.
- n2 descarta el paquete y la comunicación falla.