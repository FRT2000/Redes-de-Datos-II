# Ejercicio 11

## Dado el diagrama de intercambio de segmentos de la figura 2 y suponiendo que se aplica el mecanismo de ARQ Go-Back-N numerando por bytes, responder:

## ¿Cuál es el ancho de banda digital (throughput) que se está obteniendo?

En el diagrama, la etiqueta "0.005s bandwidth" señala el tiempo que tarda el transmisor (Tx) en enviar un único segmento completo (el bloque azul inclinado). 

**Datos:**
- Tamaño del segmento: 512 bytes.
- Tiempo de transmisión (Tx): 0.005 segundos.

![Ejercicio 11 Inciso a](/Recursos-practica4/Ejercicio11-inciso-a.png)

## ¿Cuál debería ser el valor óptimo del T1 (RTO, Timer de retransmisión) suponiendo que el delay se mantiene constante? 

El RTO (Retransmission TimeOut) debe ser siempre ligeramente superior al RTT (Round Trip Time) para evitar retransmisiones innecesarias, pero lo suficientemente bajo para no perder tiempo si un paquete se pierde.

Calculamos el RTT sumando los tiempos del gráfico:
- Tiempo de Transmisión (Tx): 0.005s (tiempo para "sacar" el paquete).
- Delay de Ida: 0.010s (tiempo en viajar de Tx a Rx).
- Delay de Vuelta : 0.010s (asumiendo simetría, tiempo en viajar de Rx a Tx).
- Se asume que el tiempo de procesamiento y transmisión del ACK es despreciable (0 bytes indicado en el gráfico).

Cálculo del RTT:

![Ejercicio 11 Inciso b](/Recursos-practica4/Ejercicio11-inciso-b.png)

Si el delay es constante, el valor óptimo de T1 debería ser exactamente 0.025 segundos (25 ms) o apenas superior. Cualquier valor menor causaría retransmisiones duplicadas (el timer vencería antes de que llegue el ACK).

## ¿Cómo se soluciona cuando el delay no es constante?

Si el delay no es constante, se utiliza el algoritmo de estimación de RTT basado en el Teorema de Chebyshev. Se calcula un promedio ponderado (Avg RTT) y una desviación (Desv), fijando el RTO con la fórmula: Timeout = Average RTT + 4 x Desv. Esto adapta el timer a las condiciones cambiantes de la red.

## ¿Cuál sería un tamaño de ventana óptimo?

Para aprovechar al máximo el canal de comunicación, el tamaño de la ventana (la cantidad de datos transferidos sin esperar confirmación) debe ser igual al Producto Ancho de Banda - Retardo (BDP).

**Cálculo:**
- Ancho de banda: 102400 Bytes/s (calculado en el inciso a).
- RTT (Retardo ida y vuelta): 0.025 segundos (calculado en el inciso b).

![Ejercicio 11 Inciso c 1](/Recursos-practica4/Ejercicio11-inciso-c-1.png)

Podemos expresarlo en segmentos sabiendo que cada uno es de 512 bytes:

![Ejercicio 11 Inciso c 2](/Recursos-practica4/Ejercicio11-inciso-c-2.png)

## ¿Cuántos bytes lograron transferirse de forma efectiva?

"Efectivo" significa datos útiles que se queda el receptor (sin contar duplicados descartados).
- Del primer envío: Llegaron bien el Paquete 1 y el 2. (512 + 512 = 1024 bytes).
- Del segundo envío: Las retransmisiones son duplicados (se descarta), pero el tercer paquete es información nueva y útil. (51 bytes).

**Total Efectivo** = 512 + 512 + 51 = 1075 Bytes

## Suponiendo que el primer ACK se pierde, completar los valores indicados con signos de interrogación.

| Flecha / Ubicación | Campo | Valor | Explicación |
| :--- | :--- | :--- | :--- |
| **2da Azul (Envío Original)** | `#seq` | **1514** | Continúa donde terminó el anterior (1002 + 512). |
| | *(ACK)* | *4103* | (Implícito: Confirma al receptor). |
| **1ra Roja (Estrella/Perdida)** | `#seq` | **4103** | El receptor no envía datos, mantiene su secuencia. |
| | `ACK` | **1514** | Recibió el primer paquete (1002-1513), pide 1514. |
| **2da Roja (Retrasada)** | `#seq` | **4103** | El receptor sigue sin enviar datos. |
| | `ACK` | **2026** | Recibió el segundo paquete (1514-2025), pide 2026. |
| **3ra Azul (Retransmisión 1)** | `#seq` | **1002** | Go-Back-N: Vuelve al inicio de la ventana perdida. |
| | `ACK` | **4103** | Confirma que el receptor sigue en 4103. |
| **4ta Azul (Retransmisión 2)** | `#seq` | **1514** | Secuencia siguiente. |
| | `ACK` | **4103** | Sigue confirmando 4103. |
| **5ta Azul (Paquete Nuevo)** | `#seq` | **2026** | Datos nuevos. Empieza donde terminó el 2do paquete. |
| | `ACK` | **4103** | Sigue confirmando 4103. |
| **3ra Roja (Final)** | `#seq` | **4103** | El receptor sigue quieto en su secuencia. |
| | `ACK` | **2077** | Confirma hasta el último byte nuevo (2026 + 51 = 2077). |
