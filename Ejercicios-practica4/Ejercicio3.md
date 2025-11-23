# Ejercicio 3

## La PDU de la capa de transporte es nombrada de forma genérica segmento. Indique para los protocolos indicados en los puntos anteriores cómo se llaman específicamente las unidades de datos y realice un diagrama de su estructura.

### Nombres Específicos de las PDUs

- **TCP:** Se denomina Segmento (Segment).
- **UDP:** Se denomina Datagrama (Datagram).
- **QUIC:** Se denomina Paquete (Packet), el cual contiene Frames (Tramas) en su interior.

### Estructura y Diagramas

**TCP**

┌───────────────────────────────────────────────────────────┐
│                      SOURCE PORT (16)                     │
├───────────────────────────────────────────────────────────┤
│                      DESTINATION PORT (16)                │
├───────────────────────────────────────────────────────────┤
│                      SEQUENCE NUMBER (32)                 │
├───────────────────────────────────────────────────────────┤
│                   ACKNOWLEDGMENT NUMBER (32)              │
├───────────────┬───────────────┬───────────────────────────┤
│ DATA OFFSET   │   RESERVED    │       FLAGS               │
│     (4)       │     (6)       │       (6)                 │
├───────────────┴───────────────┴───────────────────────────┤
│                     WINDOW SIZE (16)                      │
├───────────────────────────────────────────────────────────┤
│                     CHECKSUM (16)                         │
├───────────────────────────────────────────────────────────┤
│                     URGENT POINTER (16)                   │
├───────────────────────────────────────────────────────────┤
│                     OPTIONS (variable)                    │
├───────────────────────────────────────────────────────────┤
│                     PAYLOAD / DATA                        │
└───────────────────────────────────────────────────────────┘


**UDP**

┌───────────────────────────────────────────────────────────┐
│                      SOURCE PORT (16)                     │
├───────────────────────────────────────────────────────────┤
│                      DESTINATION PORT (16)                │
├───────────────────────────────────────────────────────────┤
│                       LENGTH (16)                         │
├───────────────────────────────────────────────────────────┤
│                      CHECKSUM (16)                        │
├───────────────────────────────────────────────────────────┤
│                           DATA                            │
└───────────────────────────────────────────────────────────┘


