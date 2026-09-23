---
title: "Algunos fundamentos de electricidad"
autor: "José Juarez"
version: "16/09/26"
---

<!-- *** GUIDE START *** -->

<div hidden>La idea es que no sea un repaso de fórmulas, sino una revisión de fundamentos a partir de situaciones reales que ponen en crisis lo que creemos saber.</div>

::: note
No alcanza con conocer las fórmulas; hay que comprender qué determina el comportamiento del sistema y qué significa cada magnitud física. De esto se trata esta guía.
:::

### 1. El punto de partida: problemas que parecen sencillos

En este punto no se evalúa el conocimiento correcto. Es un punto de partida para después con más datos verificar y aprender que estaba correcto y que faltaba.

**Consigna:** Sin ayuda, simplemente con lo que sabes, escribí qué creés que sucede y por qué. No alcanza con mostrar una fórmula: hay que explicar el comportamiento del sistema.

**a)** Un capacitor y un motor dc tipo de juguete: Un supercapacitor de 1 F se carga a 5 V. Al conectarlo a un motor de corriente continua, la tensión cae mucho y el motor no arranca. ¿Cómo puede ocurrir si el capacitor estaba cargado a 5 V?

**b)** Una fuente de tensión: Una fuente de 5 V puede entregar mucha corriente, pero un motor conectado a ella no necesariamente consume toda esa corriente. ¿Quién determina cuánta corriente circula?

**c)** Un equipo de 1 W: Un dispositivo indica 1 W en su etiqueta. ¿Consume siempre 1 W? ¿Qué significa realmente esa potencia?

**d)** Electricidad y gas: Una instalación consume energía eléctrica y otra consume gas. ¿Cómo podemos comparar sus consumos y sus costos?


### 2. Experiencia práctica: tensión, corriente y resistencia

No todas las cargas se comportan igual en un circuito. Aquí medirás parámetros en un circuito cuya carga no es una resistencia pura. Consigue en el pañol lo que puedas conseguir allí, el resto puedes consultar al profesor.

**Consigna:** 

Usar una fuente regulable, una resistencia de 10 ohms (o parecida) y un motor DC tipo 130 (los de juguete). Conectar en serie resistencia y motor y poner la fuente a la tensión que te indique el profesor. 
* Medir la corriente con el motor frenado hasta detenerlo (si se puede realizar con seguridad para no romperlo).
* Medir la corriente con el motor girando sin carga.
* Observar cómo cambia la corriente cuando se modifica la tensión o se aplica una carga mecánica moderada (frena un poco el motor).
* ¿Por qué un motor puede consumir más corriente al arrancar que cuando ya está girando?
* ¿Quién o quienes determinan la corriente?
* Si la fuente es de 10 A ¿eso significa que que obligatoriamente circula 10A?


### 3. Análisis de un supercapacitor

En la actualidad se está explorando el uso de supercapacitores como fuente de almacenamiento de energía especialmente por su velocidad de carga.

El campo tiene aun varios desafíos, uno de ellos es que un capacitor real posee una resistencia serie equivalente (ESR). Cuando comienza a circular corriente, esta resistencia produce una caída de tensión. Por eso, aunque el capacitor haya sido cargado a 5 V, al conectarlo a una carga pueden ocurrir dos cosas:

- La tensión en los bornes del capacitor puede caer instantáneamente debido a la corriente que circula por su ESR.
- El capacitor comienza a descargarse, por lo que su tensión continúa disminuyendo con el tiempo.

También intervienen la resistencia de los cables y contactos y las características del motor, cuya corriente puede ser especialmente elevada durante el arranque.

**Consigna:**

Supón el circuito formado por un supercapacitor de 1 F cargado a 5 V que alimenta un motor DC tipo 130, en serie con una resistencia.

Al conectarlo a un motor 130 (que funciona entre 1,5 y 6 V o más) e motor no gira y la tensión medida cae rápidamente. En teoría el supercapacitor tiene energía suficiente para mover el motor durante varios segundos.

Dejando de lado la resistencia del bobinado, los cables y los contactos y suponiendo que al momento del arranque circula 0,15 A y el ESR del supercapacitor es de 30 ohms:

- ¿Cuánta tensión quedaría disponible para el motor?
- ¿Qué sucedería si la ESR fuera \(0,4\,\Omega\)?
- ¿Qué diferencia hay entre tener mucha capacidad y poder entregar mucha corriente?

### 4. Potencia

Resolver:

**a)** Calcular la potencia en una resistencia eléctrica de 100 ohms conectada a 5 V. Además calcular la corriente. ¿Toda la potencia se transforma en calor en este caso? 

**b)** ¿Qué diferencia hay entre que una resistencia disipe 1 W y que un motor consuma 1 W?

**c)** Una lámpara de 1 W diseñada para funcionar a una tensión determinada puede consumir aproximadamente esa potencia en sus condiciones nominales. ¿Cómo cambia su comportamiento si se varía la tensión? ¿Es correcto decir que la carga y su forma de funcionamiento determinan la corriente real?

**d)** Tengo una fuente de 12 V y un equipo de 1 W. ¿Puedo afirmar que circularán siempre 0,083 A?


### 5. De potencia a energía

Seleccionar dos equipos de la vida real con potencias en W muy similares, por ejemplo una estufa, una es eléctrica y la otra es a gas. En base a costos actuales de energía eléctrica y del gas (averiguar, conseguir una factura actual y llegar a un valor de costo por unidad de energía) determinar cual sería más económico. Investigar esto: ¿Se puede comparar directamente el precio de un kWh eléctrico con un kWh de gas?

<div hidden>
Calculen la energía correspondiente y después discutir:

* ¿Se puede comparar directamente el precio de un kWh eléctrico con un kWh de gas?
* ¿Qué parte de la energía se aprovecha realmente?
* ¿Qué información falta para comparar costos?

Tener en cuenta: Para una comparación económica real hay que considerar el poder calorífico del gas, la unidad de facturación, el rendimiento del equipo y las tarifas aplicables.
</div>



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
