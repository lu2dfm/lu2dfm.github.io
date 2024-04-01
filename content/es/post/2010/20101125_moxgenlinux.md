---
title:  'Moxon en GNU/Linux'
date: 2010-11-25
categories:
  - "Radio"
  - "Antenas"
tags:
  - "Antena"
  - "Radio"
thumbnail: "post-images/pre2024/moxgen_model.jpg"
---


La moxon es una direccional simple de dos elementos, compacta, liviana y fácil
de construir. 

Se puede fabricar de muchas maneras.  [Hay un sitio
dedicado](http://www.moxonantennaproject.com) a estas antenas donde
pueden verse ejemplos de los mas diversos métodos constructivos.

Yo he estado modelando una moxon para 6 metros y comparando diferentes
relaciones entre las dimensiones.

Por lo que he visto el algoritmo desarrollado hace unos años por
[Cebik](http://www.cebik.com/) es aparentemente el óptimo, por lo menos
en cuanto a tres parámetros importantes: relación adelante-atrás (F/B),
impedancia del punto de alimentación y ancho de banda útil (ROE 2:1).  

La antena exhibe una ganancia moderada pero la relación adelante-atrás es
excelente (en los modelos va de 30 a 60 dB) para una antena de este tamaño y
solo dos elementos.  Andy Stwart, KB1OIQ, ha desarrollado y publicado una
versión para GNU/Linux del popular programa MoxGen, el cual es Software Libre
(lic. GNU v3 o superior).

El programa hace extremadamente fácil experimentar con la moxon ya que aparte
de mostrar en pantalla el croquis de la antena con las dimensiones calculadas
para una frecuencia y diámetro del conductor de los elementos (que debe ser
uniforme para toda la antenna) produce un plano en formato PDF de la antena *y
un archivo .NEC* para trabajar el modelo en un NEC2 (en GNU/Linux se puede usar
xnec2c, antennavis, qantenna).

En un rato se pueden probar varias
configuraciones, apilarlas, hacer versiones multibanda y bidireccionales
gracias a esta aplicación que elimina la necesidad de realizar cálculos.  Las
ecuaciones en que se basa MoxGen producen un resultado subóptimo en cuanto al
F/B cuando se usa un conductor de diámetro grande en relación al largo de onda
de la antena (hasta cierto punto. Con diámetros realmente *grandes*
empieza este parámetro no se desvía demasiado). En este caso el punto de mejor
relación F/B está un poco mas alto que la frecuencia de cálculo. Esto es debido
a que las ecuaciones originales de Cebik son aproximaciones regresivas sobre
modelos en NEC. Por ejemplo, diseñando para frecuencia de 51.1 MHz con diámetro
de conductor de 12.7 mm (1/2") el punto de mejor relación F/B está alrededor de
los 51.5 MHz. Cabe señalar que de todas maneras el modelo predice una
respetable relación F/B > 25dB en la frecuencia de diseño.
fl_moxgen se puede [descargar desde aquí](http://sourceforge.net/projects/flmoxgen/files/)
