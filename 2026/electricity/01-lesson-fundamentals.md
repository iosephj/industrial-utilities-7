---
title: "Algunos fundamentos de electricidad"
autor: "José Juarez"
version: "16/09/26"
---

<!-- *** GUIDE START *** -->


::: note
En estas breves notas se intenta orientarte para que más allá de las fórmulas comprendas mejor que cosas determinan el comportamiento de un sistema. Pregunta lo que tengas dudas.
:::


## 1. Tensión, corriente y resistencia

La **tensión eléctrica** es una diferencia de potencial entre dos puntos. La **corriente eléctrica** es el movimiento de cargas eléctricas a través de un circuito.

En una resistencia óhmica se cumple:

$$
I=\frac{V}{R}
$$

Esto significa que, para una determinada tensión, cuanto menor sea la resistencia, mayor será la corriente.

En un circuito real, la corriente no la determina únicamente la fuente: depende de la **tensión disponible, la carga y las resistencias o impedancias presentes en todo el circuito**.

Una fuente de 5 V capaz de entregar 10 A **no obliga a que circulen 10 A**. Los 10 A representan la corriente máxima que la fuente puede entregar bajo determinadas condiciones.

### El caso del motor

Un motor no se comporta simplemente como una resistencia constante. Su corriente depende, entre otras cosas, de su velocidad y de la carga mecánica.

Cuando está detenido o arrancando, puede circular una corriente mucho mayor que durante su funcionamiento normal. Si permanece detenido durante demasiado tiempo, el calentamiento de los bobinados puede dañarlo.


## 2. El supercapacitor y la caída de tensión

Si un capacitor está cargado a 5 V, inicialmente tiene aproximadamente 5 V entre sus terminales. Al conectarlo a una carga comienza a descargarse, por lo que su tensión disminuye.

Además, los componentes reales tienen cierta resistencia interna. En un supercapacitor esta característica se expresa principalmente mediante su **ESR** (resistencia serie equivalente).

También contribuyen la resistencia de los cables, contactos y demás elementos del circuito.

Una aproximación sencilla es:

$$
V_{\text{motor}}=
V_{\text{capacitor}}-I R_{\text{interna}}
$$

Hay entonces dos fenómenos:

* La corriente produce una **caída de tensión** en las resistencias internas.
* El capacitor se **descarga**, por lo que su propia tensión va disminuyendo.

Por eso, aunque el capacitor haya comenzado cargado a 5 V, el motor puede recibir una tensión mucho menor.

Una tensión pequeña tampoco implica necesariamente una corriente pequeña: si la resistencia total del circuito es baja, la corriente puede ser elevada.


## 3. Potencia eléctrica

La potencia indica la **rapidez con la que se transfiere o transforma energía**:

$$
P=\frac{E}{t}
$$

Un watt equivale a un joule por segundo:

$$
1\text{ W}=1\text{ J/s}
$$

En un circuito eléctrico:

$$
P=VI
$$

Para una resistencia óhmica también podemos utilizar:

$$
P=I^2R
$$

o

$$
P=\frac{V^2}{R}
$$

La potencia no significa necesariamente calor. Depende de qué hace el dispositivo con la energía.

Una resistencia transforma principalmente la energía eléctrica en calor mediante el **efecto Joule**. Un motor transforma parte de la energía eléctrica en energía mecánica y otra parte en calor y otras pérdidas.


## 4. Potencia nominal y consumo real

Que un equipo indique **1 W** no significa necesariamente que consuma exactamente 1 W en cualquier situación.

La indicación puede corresponder a su potencia nominal, típica, máxima, de entrada o de salida, según el dispositivo y las especificaciones del fabricante.

La corriente real depende de las condiciones de funcionamiento y de las características del equipo.

Por ejemplo, si un dispositivo de 12 V consume efectivamente 1 W en determinadas condiciones:

$$
I=\frac{P}{V}
=\frac{1}{12}
\approx0,083\text{ A}
$$

Pero no podemos afirmar que esa corriente circulará siempre solamente porque el dispositivo tenga escrita la indicación «1 W».


## 5. De potencia a energía

La potencia indica **a qué velocidad** se utiliza o transforma la energía. La energía indica **cuánto se utilizó o transformó**.

Para una potencia constante:

$$
E=P\cdot t
$$

Por ejemplo:

$$
1000\text{ W}\cdot2\text{ h}=2000\text{ Wh}=2\text{ kWh}
$$

El **W** es una unidad de potencia.

El **Wh** y el **kWh** son unidades de energía.

Esto es fundamental para interpretar una factura eléctrica: la empresa factura principalmente la **energía consumida**, expresada habitualmente en kWh, aunque la factura también puede incluir cargos relacionados con la potencia contratada o demandada.


## 6. Electricidad y gas

Para comparar consumos energéticos no alcanza con comparar directamente los números de una factura.

Hay que considerar, entre otras cosas:

* La cantidad de energía suministrada.
* La unidad utilizada para facturar.
* El precio de esa energía.
* El rendimiento del equipo.
* La cantidad de energía que finalmente resulta útil.

Por ejemplo, un equipo eléctrico puede consumir cierta cantidad de energía eléctrica y convertir una parte en energía mecánica, térmica, luminosa, etc. Un equipo a gas recibe energía química y transforma una parte en energía térmica útil, con pérdidas.



<!-- *** GUIDE END *** -->



<!-- *** GUIDE AUXILIARY THINGS *** -->

<!--

● Sections: example, activity. solutions, figure, warning, note

::: example
### Ejemplo: Cálculo de derivadas
Aquí va el contenido de tu ejemplo. Puedes usar Markdown normal adentro.
:::


● Image:

::: figure
![](imagen.png){width=400px}

<small>Pie (Source)</small>
:::

[⌕](../../images/ ) 

● Videos:

 Change XXX to video-id and put time in seconds

 - Yotube with start point: [Mira este momento clave en el video](https://www.youtube.com/watch?v=XXX&t=123s)

 - Youtubetrimmer with start and end point: [Mirá este momento puntual del video](https://youtubetrimmer.com/view/?v=XXX&start=120&end=150&loop=0)

-->
