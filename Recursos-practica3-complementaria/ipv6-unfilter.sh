#!/bin/sh
 
# Si los datagramas IPv6 no parecen llegar de un nodo a otro posiblemente
# edte filtado con ip6tables. Se puede desfiltrar ejecutando
 
sudo ip6tables -P FORWARD ACCEPT

 
