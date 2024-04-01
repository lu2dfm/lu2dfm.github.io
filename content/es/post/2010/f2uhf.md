---
title: PL-259 directo a RG-6
date: 2010-08-25
description: Adaptador fatto in casa
categories:
  - "Electrónica"
  - "Radio"
  - "Homebrew"
tags:
  - "Coaxil"
  - "Conector"

# Theme-Defined params
thumbnail: "post-images/pre2024/rg6uhf_terminado.jpg"
#lead: "Example lead - highlighted near the title" # Lead text
#lead: Volviendo a la actividad, nuevo sitio.
comments: false # Enable Disqus comments for specific page
authorbox: true # Enable authorbox for specific page
pager: true # Enable pager navigation (prev/next) for specific page
#toc: true # Enable Table of Contents for specific page
#mathjax: true # Enable MathJax for specific page
#sidebar: "right" # Enable sidebar (on the right side) per page
#widgets: # Enable sidebar widgets in given order per page
#  - "search"
#  - "recent"
#  - "taglist"

---


### Coaxil RG6 (CATV) directo a PL-259

Rev. 20120911 - agr. fotos
Rev. 20120124


Gracias a las empresas distribuidoras de CATV por estos lares, 
abunda el cable tipo RG6 de buena calidad, que usan para llegar desde el poste 
hasta los televisores de los usuarios. Típicamente es un foam de dos a cuatro
foils con buena camisa externa, algunos embebidos con gel hidrofóbico.

Los inconvenientes que presentan estos cables (salvando que son de 75 ohms) es
que el metal de la malla no es soldable y que no hay fácilmente disponibles
(léase baratos :) conectores PL-259, BNC o incluso adaptadores apropiados. Doy una
solución simple para este problema.

Materiales: un PL-259 para cable de 1/2", un barrilito F, un conector F para crimpear
en el RG6, soldador grande, herramientas comunes.

![partes](/post-images/pre2024/rg6uhf_partes.jpg "partes") 

Procedimiento: con mecha de 6mm vaciar el barrilito F de modo tal que quede liso en
el interior. Estañar una de las dos roscas del barrilito, o si es un barrilito con rosca 
continua (sin la "tuerca" hexagonal en el medio) estañar aproximadamente la mitad de la 
rosca. 

Estañar el interior y borde externo del PL-259. Introducir el barrilito F del lado
estañado en el interior del PL-259 (como si fuera el cable coaxil). Soldar bien.  

Cortar la camisa y mallas del RG6 a unos 6 o 7 cm de la punta dejando el foam y el conductor
interno. En algunos cables el foil que está pegado al foam no se puede sacar, no importa.  

Cortar el foam a unos 3 cm de la punta dejando solo el conductor interno expuesto.  

![prep](/post-images/pre2024/rg6uhf_preparado.jpg "preparado")


Crimpear el conector F en el RG6. Enroscar el F en el barrilito y verificar que hay 
suficiente foam para que llegue justo hasta el conductor central del PL-259. 

Si está bien, ajustar bien el conector F al barrilito y soldar el conductor
interior en la punta del PL-259.

![terminado](/post-images/pre2024/rg6uhf_terminado.jpg "terminado")




#### (Actualización 20120124)
Me han hecho algún comentario acerca de la inutilidad de estos cables. En mi opinión muchos
de estos cables de CATV que se consiguen *GRATIS* en cantidades importantes son
de buena calidad, resultan sumamente útiles en montones de aplicaciones, no son
peores que un coaxil común de 1/2" de 50 ohms del tipo 213 excepto en el manejo
de potencia y son muy superiores a los del tipo RG58 en todo aspecto.  


Dejo una comparación que tal vez contribuya a despejar alguna duda, usando
el [calculador de LT de VK1OD](http://vk1od.net/calc/tl/tllc.php).


#### RG213
| Parameters  |
|---------| ---------|
| Transmission Line | RG-213/U |
| Code | RG-213/U |
| Data source | DSE |
| Frequency | 100.000 MHz |
|Length|100.000 m |

| Results | | 
|---------| ---------|
|Zo|50.00-j0.09 &#937;|
|Velocity Factor, VF<sup>&nbsp;-2</sup>|0.660, 2.296|
|Length|18194.43 °, 50.540 &#955;, 100.000 m|
|Line Loss (matched)|6.981&nbsp;dB|
|Loss model source data frequency range|50.000 MHz - 1000.000 MHz|
|Correlation coefficient (r)|<font color="#ff0000">0.998211</font>|

----------

#### RG6
| Parameters |
|---------| ---------|
|Transmission Line|RG-6A/U|
|Code|RG-6A/U|
|Data source|DSE|
|Frequency|100.000 MHz|
|Length|100.000 m|

| Results |
|---------| ---------|
|Zo|75.00-j0.12 &#937;|
|Velocity Factor, VF<sup>&nbsp;-2</sup>|0.820, 1.487|
|Length|14644.30 °, 40.679 &#955;, 100.000 m|
|Line Loss (matched)|5.767&nbsp;dB|
|Loss model source data frequency range|100.000 MHz - 1000.000 MHz|
|Correlation coefficient (r)|<font color="#ff0000">0.996375</font>|


----------


#### Aún un poco desadaptado por su Zo: RG6 @50 ohms
| Parameters|| 
|---------| ---------|
|Transmission Line|RG-6A/U|
|Code|RG-6A/U|
|Data source|DSE|
|Frequency|100.000 MHz|
|Length|100.000 m|
|Zload|50.00+j0.00 &#937;|
|Yload|0.020000+j0.000000 S|

| Results |
|---------| ---------|
|Zo|75.00-j0.12 &#937;|
|Velocity Factor, VF<sup>&nbsp;-2</sup>|0.820, 1.487|
|Length|14644.30 °, 40.679 &#955;, 100.000 m|
|Line Loss (matched)|5.767&nbsp;dB|
|Line Loss|5.933&nbsp;dB|
|Efficiency|25.51 %|
|Zin|79.88+j6.49 &#937;|
|Yin|0.012436-j0.001010 S|
|VSWR(50)in|1.61|
|Loss model source data frequency range|100.000 MHz - 1000.000 MHz|
|Correlation coefficient (r)|<font color="#ff0000">0.996375</font>|


----------
