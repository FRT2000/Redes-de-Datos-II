# Ejercicio 5

## ¿En qué se diferencian los checksum de UDP, TCP, IPv4 e IPv6?

| Protocolo | Capa del Modelo | Alcance del Checksum (Qué protege) | Obligatoriedad | Detalle Clave |
| :--- | :--- | :--- | :--- | :--- |
| **TCP** | Transporte | Cabecera TCP + Datos + **Pseudocabecera** | **Siempre Obligatorio** | Es fundamental para garantizar la confiabilidad e integridad de los datos extremo a extremo. |
| **UDP** | Transporte | Cabecera UDP + Datos + **Pseudocabecera** | **Opcional** en IPv4<br>**Obligatorio** en IPv6 | Si el cálculo falla en destino, el datagrama se descarta silenciosamente sin avisar al emisor. |
| **IPv4** | Red | **Solo Cabecera IP** | **Obligatorio** | No protege los datos (payload). Se debe recalcular en cada router porque cambia el TTL. |
| **IPv6** | Red | **No existe** | **N/A** | Se eliminó para reducir la latencia de procesamiento en los routers; delega la integridad a TCP/UDP. |
