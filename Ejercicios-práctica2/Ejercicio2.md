# Ejercicio 2

## ¿Qué entiende por ambas gráficas (fuente: presentaciones IETF)?

Las dos gráficas muestran la arquitectura de Internet representada como un **reloj de arena**, donde el protocolo IP ocupa el papel central (cuello de botella) al interconectar las aplicaciones superiores con las tecnologías de red inferiores.

### 📌 Gráfico de la izquierda (IPv4 ↔ IPv6)
- El cuello de botella aparece dividido entre **IPv4** e **IPv6**.  
- Representa la **etapa de transición**, donde ambos protocolos conviven en Internet (dual stack).  
- Las aplicaciones (correo, web, telefonía, etc.) y los protocolos de transporte (TCP, UDP, HTTP, SMTP, etc.) funcionan indiferentemente sobre IPv4 o IPv6.  
- Las capas inferiores (Ethernet, PPP, fibra, radio, etc.) tampoco dependen de la versión de IP utilizada.  

---

### 📌 Gráfico de la derecha (IP unificado)
- Aquí el cuello de botella se muestra con un único **IP**, sin diferenciar versiones.  
- Representa la **visión a largo plazo**: estandarizar Internet sobre un solo protocolo de red (idealmente IPv6).  
- Esto refuerza el concepto de independencia:  
  - Las aplicaciones superiores no dependen de la versión de IP.  
  - Las tecnologías de transmisión inferiores tampoco lo hacen.  