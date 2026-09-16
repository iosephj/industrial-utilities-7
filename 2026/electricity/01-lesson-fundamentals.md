---
title: "Algunos fundamentos de electricidad"
autor: "José Juarez"
version: "16/09/26"
---

<!-- *** GUIDE START *** -->


**Aquí verás que** en las instalaciones reales no alcanza con conocer las fórmulas; hay que comprender qué determina el comportamiento del sistema y qué significa cada magnitud física.


## 1. Tensión, corriente y resistencia: quién determina qué

<div hidden>Esta es una de las cuestiones que más vale la pena profundizar.</div>

En un circuito real, la corriente depende de la tensión disponible y de las características de la carga y del circuito completo.

**Tensión disponible** es la diferencia de potencial que la fuente puede mantener entre sus bornes **en esas condiciones de carga**.

Para una resistencia ideal:

$I=\frac{V}{R}$

Pero un motor no es una resistencia constante. Su corriente depende, entre otras cosas, de su velocidad, su carga mecánica y la resistencia de sus bobinados.

La fuente establece las condiciones de alimentación, pero la carga determina la corriente que toma, en interacción con la impedancia interna de la fuente y las conexiones.

Por otro lado, una fuente de 5 V y 10 A no obliga a que circule 10 A. Significa que puede entregar hasta esa corriente bajo sus condiciones especificadas.


## 2. ¿Por qué cae la tensión del supercapacitor?

Nos referimos a un supercapacitor de 1 F cargado a 5 V que se conecta con una resistencia en serie de 10 ohms a un motor dc tipo 130 (tipo de juguete).

Modelo conceptual: capacitor, resistencia interna y motor. La resistencia interna provoca una caída de tensión cuando circula corriente.

Un capacitor ideal cargado a 5 V no mantiene necesariamente 5 V en sus terminales cuando se conecta a una carga real. En el supercapacitor intervienen:

* Su resistencia serie equivalente (ESR).
* La resistencia de los cables y contactos.
* La resistencia y el comportamiento del motor.
* La corriente elevada que puede requerir el arranque.

Una aproximación útil es:

Vmotor=Vcapacitor−IRinternaV_{\text{motor}}=V_{\text{capacitor}}-I R_{\text{interna}}Vmotor=Vcapacitor−IRinterna

Esto permite comprender que pocos voltios no garantizan una corriente pequeña. Si la resistencia total es baja, la corriente puede ser elevada.




### 4. Potencia: qué significa realmente 1 W


## Potencia

La potencia es la rapidez con la que se transfiere o transforma energía.

P=EtP=\frac{E}{t}P=tE

Un equipo de 1 W transforma o transfiere energía a razón de 1 joule por segundo, en las condiciones en las que se especifica esa potencia.

No significa necesariamente que toda esa energía se convierta en calor.

### Ejemplos

![Resistor rated at 100 ohms on black](https://images.openai.com/static-rsc-4/qNwNDFhpo9nmlDH1YYZvQJe12ZDsNhlc3VtUEWO9XzNcrfXHmNEjFboDIaUnL_rFc4a-NTpDLfrdknybBBtgO40YSP2Yrw-eWiVj_y4ZdnbZOCroBCYamUj8OAJMeqWYnQBdE-FpOZnImOOtLrAF9pEZEN6nEQioRJLt1-SapNFm1F2ylMpLPopTx1jiIQMS?purpose=inline)

Resistencia

La energía eléctrica se transforma principalmente en calor.

![DC Motor which is very unique made of plastic body with fan blade attached to its shaft](https://images.openai.com/static-rsc-4/m1eLVOuLH_1PK3O_HgKrS7jhgyc4eYdgrxr9A19Bk3aXpJhIU7TGFtoEMQwd62sGK8ZLXHfZtZe1Ea28GzUkRNF8qPIewGg3SzH8LFVzGmj_AOhlXWErmP7gjXN2m9u26zSsgSmbzGudqqzDKKyf_1ojCokeGR3cVn8idWkw1c3VTBltjbF82oMTMTrgk2h6?purpose=inline)

Motor eléctrico

La energía se transforma en movimiento, calor y otras pérdidas.

El efecto Joule es un mecanismo de transformación de energía eléctrica en calor, pero no es la definición de potencia.

Para una resistencia:

P=VI=I2R=V2RP=VI=I^2R=\frac{V^2}{R}P=VI=I2R=RV2

### Actividad práctica

Con una resistencia de potencia y una fuente regulable:

1. Calcular la potencia con una tensión determinada.

2. Medir la corriente.

3. Verificar la potencia con P=VIP=VIP=VI.

4. Observar el calentamiento, sin exceder la potencia nominal de la resistencia.









### 1. Combustión

<!-- Image -->
<br>
   <center>![](gas/combustion-triangle.png){width=400px}</center>
<br>

La **combustión** es una reacción química entre un combustible y un comburente (generalmente el oxígeno del aire) que libera energía en forma de calor y, muchas veces, luz.

Para que ocurra una combustión se necesitan tres elementos:

* Combustible.
* Oxígeno (comburente).
* Energía de activación (calor, chispa, llama, etc.).

Estos tres elementos forman el llamado **triángulo del fuego**.

<br>

### 2. Productos de la combustión

<!-- Image -->
<br>
   <center>![](gas/combustion-flame-colors.png){width=400px}</center>
<br>




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
