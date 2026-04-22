---
title: "Análisis de costo de ciclo de vida: sistemas de presurización"
autor: "José Juarez"
version: "22/04/26"
---


<!-- *** GUIDE START *** -->


### Introducción

Esta tarea intenta responder lo mejor posible la pregunta: ¿Conviene un sistema de presurización moderno?

Se hace en grupos de 2 alumnos usando una planilla de cálculo. Todos los costos se ponen en dólares para evitar computar el efecto de la inflación variable en la Argentina.

<br>

### Enunciado

Una instalación necesita un sistema de presurización. Se deben comparar dos opciones:

**a)** **Sistema tradicional:** bomba centrífuga (presostado y tanque hidroneumático) funcionando a velocidad fija
**b)** **Sistema moderno:** bomba con variador de frecuencia

El objetivo es determinar **cuál conviene económicamente a lo largo del tiempo**.

Para esto:

**1. Buscar información real:**

* Precio de la energía eléctrica ($/kWh) en su zona. [Link a una factura del 2025](https://i.postimg.cc/PrmTyjKT/tec-problema-factura-luz-2025.jpg).
* Potencia típica de una bomba (pueden asumir un valor si no encuentran uno exacto)
* Diferencia de costo inicial entre ambos sistemas


**2. Armar una planilla de cálculo que incluya:**

* Consumo eléctrico estimado de cada sistema
* Horas de uso por día (supuestas, pero justificadas)
* Consumo mensual y anual
* Costo anual de energía


**3. Calcular el costo del ciclo de vida (mínimo 5 o 10 años):**

Para cada sistema incluir:

* Costo inicial
* Costo total de energía consumida
* (Opcional) mantenimiento estimado

**4. Comparar:**

* ¿Cuál sistema resulta más barato a largo plazo?
* ¿En cuántos años se recupera la inversión del sistema moderno? (si corresponde)


**5. Entrega**

**a) Digital (planilla):**

* Mostrar la planilla que debe estar ordenada y con fórmulas (no solo resultados)

**b) En papel (resumen):**

Una hoja con:

* Datos principales utilizados
* Resultados finales
* Conclusión justificada (qué sistema conviene y por qué)


**Aclaración**

* Todos los valores deben estar **justificados** (no inventados sin explicación)
* Se evaluará más el **proceso y la lógica** que el número final


<br><br>


### Estructura de la planilla de cálculo

A continuación se pasa un formato para las tablas de la planilla de cálculo. 


<div class="grey3 size80">

#### Datos de entrada (comunes)

| Concepto             | Valor | Unidad |
| -------------------- | ----- | ------ |
| Precio energía       |       | $/kWh  |
| Horas de uso por día |       | h/día  |
| Días por mes         | 30    | días   |
| Años de análisis     | 10    | años   |


#### Sistema tradicional (sin variador)

| Concepto                | Valor                                 |
| ----------------------- | ------------------------------------- |
| Potencia                |                                       |
| Consumo diario (kWh)    | =Potencia × Horas                     |
| Consumo mensual (kWh)   | =Diario × 30                          |
| Consumo anual (kWh)     | =Mensual × 12                         |
| Costo anual ($)         | =Anual × Precio energía               |
| Costo inicial ($)       |                                       |
| Costo total 10 años ($) | =Costo inicial + (Costo anual × años) |


#### Sistema moderno (con variador)

(igual estructura, pero con menor consumo)

| Concepto                | Valor |
| ----------------------- | ----- |
| Potencia equivalente    |       |
| Consumo diario (kWh)    |       |
| Consumo mensual (kWh)   |       |
| Consumo anual (kWh)     |       |
| Costo anual ($)         |       |
| Costo inicial ($)       |       |
| Costo total 10 años ($) |       |


#### Comparación final

| Concepto                      | Valor                                     |
| ----------------------------- | ----------------------------------------- |
| Diferencia de costo total     |                                           |
| Ahorro anual con variador     |                                           |
| Tiempo de recuperación (años) | = Diferencia costo inicial / ahorro anual |

</div>

* Pueden asumir datos, pero deben escribir de dónde salen
* Si el sistema moderno consume menos, eso tiene que reflejarse en los cálculos (ej: 20–40% menos)



<!-- *** GUIDE END *** -->


<!-- *** GUIDE AUXILIARY TEMPLATES *** -->


<div hidden>


<!-- Learning objectives very briefly -->
<span class="grey3 size85">.</span>

<!-- Image -->
<br>
   <center>![](){width=400px}</center>
   <center>
      <span class="grey3 size70">. </span>
      <span class="grey3 size50">Fuente: </span>
   </center>
<br>

<!-- Videos: change XXX to the video-id and put time (seconds) -->
<!-- Yotube with start point -->
👉 [Mira este momento clave en el video](https://www.youtube.com/watch?v=XXX&t=123s)
🎬 [Un fragmento que vale la pena ver](https://www.youtube.com/watch?v=XXX&t=123s)
🔎 [Este detalle del video te va a interesar](https://www.youtube.com/watch?v=XXX&t=123s)
⚡ [Dale play a esta parte y fijate qué pasa](https://www.youtube.com/watch?v=XXX&t=123s)
<!-- Youtubetrimmer with start and end point -->
👉 [Mirá este momento puntual del video](https://youtubetrimmer.com/view/?v=XXX&start=120&end=150&loop=0)
🎬 [Este fragmento explica justo lo que necesitamos](https://youtubetrimmer.com/view/?v=XXX&start=120&end=150&loop=0)
⚡ [Dale play a esta parte y sacá tus conclusiones](https://youtubetrimmer.com/view/?v=XXX&start=120&end=150&loop=0)
🔎 [Fijate qué pasa en este momento](https://youtubetrimmer.com/view/?v=XXX&start=120&end=150&loop=0)

<!-- Visible story or anecdote -->
<span class="grey3 size85">...</span>

<!-- Sections -->
<br><span class="grey3 size70">🔁 Repaso:</span>
<br><span class="grey3 size70">🛠️ Trabajo:</span>
<br><span class="grey3 size70">📘 Teoría:</span>
<br><span class="grey3 size70">✅ Autoevaluación:</span>
<br><span class="grey3 size70">📝 Práctica:</span>
**1.**  **:**
**2.** **:** 

<!-- Solutions -->
<div class="grey3 size70">.</div>


</div>


<!-- Guide style definitions -->
<style>
/* Colors */
.grey1 {color: #b3b3b3;} /* my light-grey */
.grey2 {color: #999999;} /* my middle-grey */
.grey3 {color: #808080;} /* my dark-grey */
.blue1 {color: #6495ed;} /* nvim blue */
.blue2 {color: #276cdf;} /* Andrew Ng Blue */
.sky1 {color: #7dbed8;} /* nvim sky */
.sky2 {color: #27a2db;}   /* my sky */
.green {color: #81b524;} /* my green */
.red1 {color: #ec5469;} /* my coral-red */
.red2 {color: #f44336;} /* my red */
.rose {color: #ec9998:} /* nvim rose */
.gold {color: #df9d43;} /* Andrew Ng gold */
.orange1 {color: #fda556;} /* nvim orange */
.orange2 {color: #ff9505;} /*Andrew Ng orange */
.purple1 {color: #ff40ff;} /* Andrew Ng purple */
.purple2 {color: #d164d7;} /* Andrew Ng purple */
/* Font Size */
.size90 {font-size: 0.9em;}
.size85 {font-size: 0.85em;}
.size80 {font-size: 0.8em;}
.size70 {font-size: 0.7em;}
.size60 {font-size: 0.6em;}
.size50 {font-size: 0.5em;}
/* Document General Font Size */
body {font-size: 1.3em;}
/* =========================
   IMPRESIÓN A4 – GUÍAS
   ========================= */
@media print {

  @page {
    size: A4;
    margin: 1.2cm;
  }

  body {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 10.5pt;
    line-height: 1.35;
    color: #000;

    column-fill: auto; /* Llena una columna y después la otra*/
    column-count: 2;
    column-gap: 1cm;
  }

  h1 {
    font-size: 14pt;
    margin: 0 0 6pt 0;
  }

  h2 {
    font-size: 12pt;
    margin: 8pt 0 4pt 0;
  }

  h3 {
    font-size: 11pt;
    margin: 6pt 0 3pt 0;
  }

  h1, h2, h3 {
    break-after: avoid;
    break-inside: avoid;
  }

  p {
    margin: 0 0 4pt 0;
    text-align: justify;
    break-inside: avoid;
  }

  ul, ol {
    margin: 0 0 4pt 12pt;
    padding: 0;
  }

  li {
    margin-bottom: 2pt;
  }

  code, pre {
    font-family: "Courier New", Courier, monospace;
    font-size: 9.5pt;
    background: #f2f2f2;
    padding: 1px 3px;
    border-radius: 2px;
  }

  pre {
    padding: 6pt;
    overflow: hidden;
    break-inside: avoid;
  }

  img {
    max-width: 100%;
    height: auto;
    break-inside: avoid;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 9.5pt;
  }

  th, td {
    border: 1px solid #000;
    padding: 3pt;
  }

  nav, footer, .no-print {
    display: none;
  }
}
</style>
<!-- Remember: Use <span> inline and <div> with several lines --->
