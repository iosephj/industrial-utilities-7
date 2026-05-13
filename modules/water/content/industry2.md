---
title: "Diseño de instalaciones de agua industrial (2)"
autor: "José Juarez"
version: "29/04/26"
---


<!-- Image -->
<br>
   <center>![](https://imgs.search.brave.com/v22U3KggmJwWL_ZwcNchvzbM0hy9z5XiJVRgnN4-9ZA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9lc2Fp/bi5jb20vd3AtY29u/dGVudC91cGxvYWRz/LzIwMjQvMTIvSDIt/Q29tZS1zaS1jYWxj/b2xhbm8tbGUtcGVy/ZGl0ZS1kaS1jYXJp/Y28tZGVpLXR1Ymkt/MTAyNHg0NjEuanBn){width=400px}</center>
   <center>
      <span class="grey3 size70">Pérdida de carga</span>
      <span class="grey3 size50">Fuente: esain.com</span>
   </center>
<br>



<!-- *** GUIDE START *** -->

### 1. Introducción

Quedan considerar los últimos pasos de diseño de una instalación de agua industrial. Estos serían básicamente calcular y verificar la pérdida de carga y seleccionar la bomba.


<br>


### 2. Repaso de pérdida de carga

Cuando el agua circula por una cañería pierde energía debido al rozamiento.

Esta pérdida de energía provoca una disminución de presión a lo largo de la instalación.

Las pérdidas dependen de:

* longitud de la cañería
* caudal
* diámetro
* material del caño
* accesorios

#### Tipos:

Las pérdidas no solo se producen por el rozamiento del agua con el caño sino también por la turbulencias localizadas que generan los accesorios. 

- **[Pérdida por fricción](https://engcourses-uofa.ca/wp-content/uploads/eng130C8_1.jpg)**: Ocurre en tramos rectos de tubería debido al rozamiento entre el fluido y las paredes.

- **[Pérdida localizada](https://grupohidraulica.com/wp-content/uploads/2024/05/image-14.png)**: Ocurre en los accesorios, cambios de dirección o sección, generando turbulencias.


<br>


### 3. Fórmula de Hazen-Williams

Para estimar pérdidas de carga por fricción (primer tipo) en instalaciones de agua puede utilizarse la fórmula de Hazen-Williams:

$h_f = 10.67\frac{LQ^{1.852}}{C^{1.852}D^{4.87}}$

Donde:

* (h_f): pérdida de carga (m.c.a.)
* (L): longitud de cañería (m)
* (Q): caudal m³/s
* (D): diámetro interno (m)
* (C): coeficiente del material


#### Valores típicos de (C)

| Material         | C   |
| ---------------- | --- |
| PVC / PEAD       | 150 |
| Acero nuevo      | 120 |
| Acero envejecido | 100 |


<br>


### 4. Pérdidas localizadas

Los accesorios también producen pérdidas:

* codos
* válvulas
* tees

Para simplificar, se puede considerar:

> pérdidas localizadas ≈ 20% de las pérdidas por fricción.


<br>


### 5. Ejemplo básico

Una instalación tiene una tubería de PVC de 2 pulgadas de diámetro interno (0.0525 m), con 100 metros de longitud. Circula un caudal de 2 l/s (0.002 m³/s). La instalación tiene 2 codos de 90° y una válvula de compuerta. Se desea saber cuánta presión se pierde.

**Paso 1: Calcular velocidad del agua**

Tener en mente la fórmula que vimos: **Caudal = Area * Velocidad**

```
A = (π * D²) / 4 = (π * 0.0525²) / 4 ≈ 0.002165 m²
v = Q / A = 0.002 / 0.002165 ≈ 0.924 m/s
```

**Paso 2: Calcular pérdida por fricción (Hazen-Williams)**

Usamos `C = 150`:

```
hf = 10.67 * (100 / (150^1.85 * 0.0525^4.87)) * 0.002^1.85 ≈ 1.07 m
```

**Paso 3: Calcular pérdidas localizadas**

```
hl = 0.15 * hf = 0.15 * 1.07 m ≈ 0.16 m
```

**Paso 4: Pérdida total**

```
h_total = hf + hl = 1.07 + 0.16 = 1.23 mca
```

<div hidden>
Prefiero poner el ejemplo del 2025 que está revisado en los cálculos, este no tuve tiempo.

Una instalación posee:

* 25 m de cañería PVC
* diámetro interno: 32 mm
* caudal: 0,001 m³/s
* (C = 150)

#### Cálculo

Aplicando Hazen-Williams:

$h_f = 10.67\frac{LQ^{1.852}}{C^{1.852}D^{4.87}}$

Resultado aproximado:

[
h_f \approx 1,5 \text{ m.c.a.}
]

Pérdidas localizadas:

[
0,2 \times 1,5 = 0,3 \text{ m.c.a.}
]

Pérdida total:

[
1,5 + 0,3 = 1,8 \text{ m.c.a.}
]

</div>


<br>


### 6. Selección de bombas

La bomba debe proporcionar:

* el caudal requerido
* la presión suficiente para:

  * vencer pérdidas
  * alimentar correctamente el sistema

Por lo tanto la presión requerida por la bomba depende de:

* altura geométrica
* pérdidas de carga
* presión de trabajo necesaria (por ejemplo la presión que requiere un aspersor de riego para trabajar bien)

Dependiendo el uso puede ser conveniente considerar el uso de un variador de frecuencia para controlar la bomba. Este permite modificar la velocidad de la bomba según la demanda.

Ventajas:

* ahorro de energía
* presión más estable
* menor desgaste

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
.orange2 {color: #ff9505;} /* Andrew Ng orange */
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
/* Bullet "1." see as "1)" */
ol {list-style-type: decimal;}
ol li::marker {content: counter(list-item) ") ";}
/* Two columns */
.two-columns {
  column-count: 2; /* Number of columns */
  column-gap: 20px;
}
/* Indent the example */
.example {margin-left: 20px;}

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
