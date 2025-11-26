# Ejercicio 12

## El host A desea establecer una sesión TCP con el host B. A selecciona un ISN de 50430, MSS de 1400 bytes y un tamaño de ventana de 64KB; B, por su parte, tiene un ISN de 68900, MSS de 1000 bytes y un tamaño de ventana de 32KB. Responder:

## ¿Cómo sería el intercambio de mensajes para establecer la sesión?

Se utiliza el Saludo de 3 vías (3-Way Handshake). 
- El MSS (Maximum Segment Size) es una opción que se envía solo en los segmentos SYN e indica cuánto puede recibir quien lo envía.
- El número de ACK es el número de secuencia recibido + 1 (consumo del flag SYN)

**Datos:**
- Host A: ISN = 50430, MSS = 1400, Win = 64KB.
- Host B: ISN = 68900, MSS = 1000, Win = 32KB.

**Diagrama del Intercambio:**
- A -> B (SYN):
    - A inicia la conexión. Anuncia sus parámetros.
    - Flags: SYN
    - Seq: 50430
    - MSS: 1400 (A dice: "Puedo recibir segmentos de hasta 1400 bytes").
    - Window: 65536 (64KB, asumiendo 64 x 1024 bytes).
- B -> A (SYN, ACK):
    - B confirma recepción y propone sus parámetros.
    - Flags: SYN, ACK
    - Seq: 68900
    - Ack: 50431 (50430 + 1).
    - MSS: 1000 (B dice: "Solo puedo recibir segmentos de hasta 1000 bytes").
    - Window: 32768 (32KB, asumiendo 32 x 1024 bytes).
- A -> B (ACK):
    - A confirma la conexión de B. La sesión queda establecida.
    - Flags: ACK
    - Seq: 50431
    - Ack: 68901 (68900 + 1).
    - Window: 65536.

## ¿Cuántos segmentos de tamaño máximo le puede enviar A a B sin esperar un ACK? ¿Y B a A? (Considere primero que no se aplica control de congestión tradicional y luego aplicándolo).

Primero debemos definir qué tamaño de segmento (MSS) usará cada uno al transmitir.
- Cuando A envía a B: Debe respetar el MSS que B anunció -> 1000 bytes.
- Cuando B envía a A: Debe respetar el MSS que A anunció -> 1400 bytes.

Ahora analizamos los dos escenarios pedidos:

**Escenario 1: Sin Control de Congestión (Solo Control de Flujo)**

La única limitación es la Ventana del Receptor (rwnd) que el otro extremo anunció.

La fórmula es: 

![Escenario 1](/Recursos-practica4/Ejercicio12-inciso-b-esc1.png)

- A enviando a B:
    - Ventana de B (lo que B puede guardar): 32 KB (32768 bytes).
    - Tamaño del paquete (MSS de B): 1000 bytes.
    - Cálculo: 32768 / 1000 = 32.7.
    - Respuesta: A puede enviar 32 segmentos completos de 1000 bytes antes de llenar el buffer de B.
- B enviando a A:
    - Ventana de A (lo que A puede guardar): 64 KB (65536 bytes).
    - Tamaño del paquete (MSS de A): 1400 bytes.
    - Cálculo: 65536 / 1400 ~ 46.8.
    - Respuesta: B puede enviar 46 segmentos completos de 1400 bytes antes de llenar el buffer de A.


**Escenario 2: Aplicando Control de Congestión Tradicional (Slow Start)**

Entra en juego la Ventana de Congestión (cwnd).

La transmisión efectiva está limitada por:

![Escenario 2](/Recursos-practica4/Ejercicio12-inciso-b-esc2.png)

Cuando una conexión recién comienza (o se reinicia), se aplica el algoritmo de Slow Start (Arranque Lento):
- La ventana de congestión (cwnd) se inicializa en el valor mínimo, que tradicionalmente es 1 MSS (un solo segmento).

Por lo tanto, no importa cuán grande sea la ventana del receptor (32KB o 64KB), la red "desconfía" y empieza de a poco:
- A enviando a B:
    - cwnd inicial = 1 MSS.
    - Solo puede enviar 1 segmento (de 1000 bytes). Debe esperar el ACK de ese segmento para aumentar su ventana a 2, luego a 4, etc.
- B enviando a A:
    - cwnd inicial = 1 MSS.
    - Solo puede enviar 1 segmento (de 1400 bytes).