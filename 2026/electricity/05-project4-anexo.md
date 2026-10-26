---
title: "Segunda inecuación en la protección contra sobrecargas"
autor: "José Juarez"
version: "25/10/26"
---

<!-- *** GUIDE START *** -->

Esta cuestión va al centro de por qué existen las normas de seguridad eléctrica. 

Para entenderlo de forma intuitiva, la clave está en que el guardamotor no sabe qué cable le conectaste. El guardamotor solo "mide" corriente y responde a su propia perilla, pero no tiene forma de saber si el cable que alimenta es fino o grueso.

La inecuación $(I_2 \le 1,45 \cdot I_Z)$ es una prueba matemática que hace el proyectista para verificar que la física del guardamotor y la física del cable no entren en conflicto.

### ¿Qué representa realmente cada lado de la inecuación?

Estamos comparando dos "límites térmicos de laboratorio" durante 1 hora:

- **Lado Izquierdo ($I_2$ — Límite del Guardamotor):**
   Es la corriente a la que el guardamotor **garantiza que va a disparar** en 1 hora. Por ejemplo para un guardamotor ajustado a $10,15\text{ A}$, esa corriente es $I_2 = 1,30 \cdot 10,15\text{ A} = \mathbf{13,20\text{ A}}$. Por debajo de 13,20 A, el guardamotor puede quedarse "pensando" y no saltar.

- **Lado Derecho ($1,45 \cdot I_Z$ — Límite de Sobrevivencia del Cable):**
   Es la corriente máxima que la aislación de PVC del cable puede soportar durante 1 hora sin que el plástico se derrita ni pierda sus propiedades aislantes.

Ejemplo:

::: example

Si un proyectista cometiera el error de conectar un **cable muy delgado** (por ejemplo, un cable con $I_Z = 8\text{ A}$ a un guardamotor ajustado a $10\text{ A}$:

* El guardamotor esperaría a llegar a $I_2 = 13 \text{ A}$ para cortar.
* Pero para ese cable delgado, su límite de sobrevivencia sería $1,45 \cdot 8\text{ A} = \mathbf{11,6\text{ A}}$.
* **El desastre:** Una corriente de $12\text{ A}$ estaría derritiendo el plástico del cable durante 1 hora y el guardamotor **nunca se enteraría ni dispararía**, porque para él $12\text{ A}$ está dentro de lo "soportable".

:::


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
