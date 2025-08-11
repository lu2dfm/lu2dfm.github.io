---
categories:
- Software
date: 2015-04-20
description: 'Nota: Este proyecto no despertó interés. Xastir sigue funcionando bien.
  Si alguien está interesado sigo dispuesto a meterle algunas horas. pyaprs: otro
  clien...'
lead: Preanuncio del proyecto, alpha, beta. Notas.
tags:
- APRS
- Python
thumbnail: post-images/pre2024/pyaprs_0_cap0.jpg
title: pyaprs. Otro cliente ARPS mas
---


** Nota: Este proyecto no despertó interés. Xastir sigue funcionando bien.
Si alguien está interesado sigo dispuesto a meterle algunas horas.***

#### pyaprs: otro cliente APRS mas... 
##### Notas, alpha. 
Estos días me dió por reactivar el iGate de mi estación y el del club (que está
de QRT por destrucción del coaxil de bajada: se aceptan donaciones :)

Lo primero que hice fué abrir XASTIR y mirar un poco el tráfico cercano.
Inmediatamente, como siempre, empezó el tema mapas. Intenté nuevamente usar
OpenStreetMap, configuré el caché local, pero no hay caso: XASTIR no cachea los
tiles, y al mínimo movimiento del mapa (zoom, desplazamiento) empieza a
descargar los tiles de nuevo. No solo eso, algunas veces los descarga dos y
tres veces (según veo en el log de mi caché).

Aparte de ineficiente, XASTIR muestra su edad e idiosincrasia: la interfaz es
anticuada (MOTIF) y ciertas convenciones (por ej. el zoom) son poco intuitivas
para estos tiempos. 

En parte esto y en parte las ganas de escribir algo, me llevaron a tirar un
pre-demo de un nuevo cliente APRS, usando: python, Gtk y
[osmgpsmaps](https://nzjrs.github.io/osm-gps-map/)

El resultado preliminar se ve como muestra la imagen.

Como se ve no es nada complicado. Actualmente (vers. 0.0.1 - alpha) el programa es capaz de:
 - Mostrar los mapas :)
 - Mostrar los iconos de los objetos.
 - Mostrar tracks.
 - Comunicar con un server APRS-IS, recibiendo data de la red.
 - Transmitir beacon de la estación al server APRS-IS.
 - Transmitir beacon de objetos al server APRS-IS.
 - Leer boletines.
 - Leer mensajes.
  
Los próximos son: completar la funcionalidad básica, esencialmente falta enviar mensajes,
crear avisos y alarmas, y comunicar con el TNC. Con esto se completaría la rev. alpha.

Para una beta necesito agregar un editor de configuración y revisar el código
que filtra paquetes erróneos. Además, para comunicar con el server APRS-IS
estoy empleando alternativamente una librería propia con
[aprslib](https://pypi.python.org/pypi/aprslib/0.6.36) , que es alpha y está
incompleta. Así que el algún momento va a ser necesario decidir si completar
esta lib o avanzar con una propia. 

Como no ando con mucho tiempo es poco probable que una beta esté disponible
antes de agosto o septiembre. En ese punto lo voy a subir a github. El proyecto
va a ser GPL.

La idea no es proveer un sustituto de XASTIR, ya que este es muy completo y
tiene muchos años de desarrollo. La idea es un tener un cliente ágil (en cuanto
a la interfaz de usuario) y moderno para *nix utilizable en uso cotidiano no
demasiado exigente :). Con el tiempo veremos...

Si alguien está interesado en este desarrollo, contácteme directamente. Vendría
bien otro desarrollador, y como siempre, testers! 
