# Ejercicio 8

## Realizar un programa en el lenguaje de su preferencia, que reciba como parámetros el tamaño total del mensaje IPv4 de entrada, la longitud del header del mismo, el MTU de salida y el bit don’t fragment y muestre cómo resultaría la fragmentación del mismo. Por ejemplo un datagrama de 1100B con un header de 20B (mínimo) y un MTU de salida de 200:

### show_frag(1100,20,200,0)
### 1080 TotalDataSent= 176 packetPayloadLength= 176 OffsetBytes= 0 SentOffset= 0 DF=0 MF=1
### 904 TotalDataSent= 352 packetPayloadLength= 176 OffsetBytes= 176 SentOffset= 22 DF=0 MF=1
### 728 TotalDataSent= 528 packetPayloadLength= 176 OffsetBytes= 352 SentOffset= 44 DF=0 MF=1
### 552 TotalDataSent= 704 packetPayloadLength= 176 OffsetBytes= 528 SentOffset= 66 DF=0 MF=1
### 376 TotalDataSent= 880 packetPayloadLength= 176 OffsetBytes= 704 SentOffset= 88 DF=0 MF=1
### 200 TotalDataSent= 1056 packetPayloadLength= 176 OffsetBytes= 880 SentOffset= 110 DF=0 MF=1
### 24 TotalDataSent= 1080 packetPayloadLength= 24 OffsetBytes= 1056 SentOffset= 132 DF=0 MF=0
### Fragments=7 TotalBytesIN/OUT=1100/1220

Ejercicio realizado dentro del archivo "ejercicio8.py" dentro de la carpeta "Recursos-practica3".

[Ejercicio 8](/Recursos-practica3/ejercicio8.py)

Créditos al señor: **Bautista Iacobucci**