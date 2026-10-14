---
title: "Proyecto - Etapa 3"
autor: "José Juarez"
version: "06/10/26"
---

<!-- *** GUIDE START *** -->


## 1. Cálculo de la corriente de proyecto

La corriente de proyecto $I_B$ es el valor de corriente que se utiliza para dimensionar las secciones de los cables y seleccionar los calibres de las protecciones del circuito.

Para el caso específico de un **motor eléctrico trifásico**, la reglamentación **AEA 90364-7-771** establece una metodología precisa de cálculo que se divide en dos pasos como se pide en la actividad de abajo.

### Actividad

::: activity

Desarrollar esto en la carpeta de modo prolijo.

**a)** Cálcular la Corriente Nominal del Motor $I_n$

Antes de aplicar los factores de proyecto, se debe determinar la **corriente nominal de línea** que consumirá el motor a plena carga utilizando los datos de su placa de características (los datos que cada uno tiene):

* Potencia mecánica en el eje $P_{mec}$
* Tensión nominal de línea $U$
* Factor de potencia $\cos\phi$
* Rendimiento o eficiencia $\eta$

**Sugerencia:** Convertir potencia mecánica a potencia eléctrica consumida (Potencia activa) usando $\eta$. Luego calcular la corriente nominal.

<div hidden>
  Para un sistema trifásico equilibrado, la corriente nominal de línea se calcula mediante la fórmula:
  $I_n = \frac{P_{el}}{\sqrt{3} \cdot U \cdot \cos\phi}$
</div>

**b)** Determinar la Corriente de Proyecto $I_B$ según AEA 90364

Esta corriente se calcula para dimensionar los conductores. En el Anexo 771-H hay una tabla muy útil que muestra el proceso de diseño paso a paso. Pero no toca el caso de los motores. Para resolver este caso hay que ir a la sección 771.16 que trata sobre el dimensionaniento de la sección de los condutores. En concreto al final de la 771.16.

**Aclaración:** La corriente de proyecto no es una corriente física instantánea, sino un **valor de diseño estipulado por norma** para para garantizar un **margen térmico de seguridad** en el cable. Así se evita que los arranques repetitivos o las ligeras sobrecargas mecánicas de la cinta transportadora envejezcan prematuramente la aislación del conductor.

<div hidden>
Según la subcláusula **771.16.2.5**, cuando se dimensionan los conductores o cables de alimentación para **un solo motor**, la intensidad de corriente de proyecto no debe ser inferior al **125 % (factor 1,25)** de la intensidad nominal del motor.

¿Por qué exige la norma aplicar el factor del 125 % (1,25)?

1. **Margen térmico por sobrecarga de servicio:** Los motores pueden operar en condiciones de carga variable o sufrir ligeras sobrecargas mecánicas continuas durante su funcionamiento.
2. **Ciclos de arranque:** Evita el envejecimiento prematuro del aislamiento del cable debido al calentamiento acumulado producido por las elevadas corrientes durante los arranques repetitivos de la cinta transportadora.
3. **Flexibilidad normativa:** La norma aclara que el coeficiente 1,25 podrá reducirse si se conoce con precisión el **factor de servicio real** del motor, pero aclara explícitamente que nunca será inferior a 1.
</div>

:::

## 2. Elegir el conductor

La segunda fila de la tabla resumen del Anexo 771-H llamada "Elección del conductor a partir de su corriente máxima $Iz$" manda consultar la cláusula 771.19.3. El proceso pide aplicar factores de corrección (método de instalación, temperatura ambiente, agrupamiento de cables, tipo de aislamiento). Y luego elegir la sección cuyo "$I_z$ (intensidad admisible) ≥ $I_B$ (corriente de proyecto)" y además esté corregida por los diversos factores. Abajo verás como puedes completar esta actividad.

### Actividad

::: activity

Puedes elegir cualquiera de estos dos caminos.

**a)** Hacer todo el proceso de selección siguiendo paso a paso la norma llegando a la sección del cable y al $I_z$.

**b)** Si la aplicación de tu cinta transportadora no lo impide puedes usar directamente estos valores que se muestran abajo y que están basados en la experiencia industrial:

- Usar **cable flexible de cobre, aislación PVC o XLPE, 0,6/1 kV**.
- Tendido **en bandeja**. 
- Para motores 5–10 kW elegir la sección **3×2,5 mm²** y verificar la caída de tensión. Si no verifica elegir **3×4 mm²** y verificar nuevamente. Esto uele ser suficiente.
- $I_z$: para sección de **2,5 mm²** tomar $I_z=29A$ y para **4 mm²** tomar $Iz=38A$

:::

> Para aprobar esta etapa se presenta en papel esta parte de la memoria descriptiva, ordenada y prolijo. Se explica además oralmente lo escrito.


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
