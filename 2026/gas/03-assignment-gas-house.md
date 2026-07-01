---
title: "Algunas cuestiones de instalaciones domiciliarias"
autor: "José Juarez"
version: "24/06/26"
---



### Actividades

<div class="actividad">

**1)** Completa las equivalencias entre las siguientes unidades.

  * 1 \[J] = ... \[cal] = ... \[Kcal] = ... \[kWh]

**2)** **Cálculo de energía total:** Con los datos de una factura de gas (ver imagen proporcionada), calcular la energía total consumida en **kcal** usando el valor del PCI proporcionado por la factura. El poder calórifico de un gas depende de su composición y por lo tanto su valor puede tener pequeñas variaciones. Por ésto se usa el valor promedio, en este caso el que da la empresa de gas.

<!-- Image -->
<br>
   <center>![](gas/vivienda-factura.png){width=700px}</center>
<br>

**3)** Funcionamiento del tiro natural: Explicar brevemente por qué los gases en artefactos de tiro natural se evacuan sin asistencia mecánica.

**4)** Cálculo de consumo: Calcular cuántos m³/h consume la estufa de abajo. Use el PCI del gas natural.

<!-- Image -->
<br>
   <center>![](gas/vivienda_tiraje_estufa_balanceado_consumo.png){width=300px}</center>
<br>


**5)** Entras a tu casa y sientes olor a gas ¿Que haces?

</div>

> Para aprobar debes mostrar esta tarea al profesor y responder alguna pregunta que te haga


<!-- *** GUIDE END *** -->


<!-- *** GUIDE AUXILIARY TEMPLATES *** -->


<div hidden>

<!-- Image -->
<br>
   <center>{width=400px}</center>
   <center>
      <span class="grey3 size70">. </span>
      <span class="grey3 size50">Fuente: </span>
   </center>
<br>

<!-- Videos: change XXX to the video-id and put time (seconds) -->
<!-- Yotube with start point -->
👉 [Mira este momento clave en el video](https://www.youtube.com/watch?v=XXX&t=123s)
<!-- Youtubetrimmer with start and end point -->
👉 [Mirá este momento puntual del video](https://youtubetrimmer.com/view/?v=XXX&start=120&end=150&loop=0)
🎬 [Este fragmento explica justo lo que necesitamos](https://youtubetrimmer.com/view/?v=XXX&start=120&end=150&loop=0)
🔎 [Fijate qué pasa en este momento](https://youtubetrimmer.com/view/?v=XXX&start=120&end=150&loop=0)

</div>



<style>

/* =========================
   ESTILO GENERAL (PANTALLA)
   ========================= */

body {
    font-family: Arial, sans-serif;
    font-size: 1.3em;
    color: #222222;
    line-height: 1.4;
    /* max-width: 800px; /*800px es el largo facilitar lectura */
    margin: auto;
    padding: 1.5em;
}

/* Título principal de la guía */
h1 {
    color: #1F4E79; /* azul técnico */
    border-bottom: 1px solid #ccc;
    padding-bottom: 0.3em;
}

/* Secciones principales */
h3 {
    margin-top: 1.2em;
    margin-bottom: 0.4em;
    color: #222;
}

/* Subtítulos menores (si los usas) */
h4 {
    margin-top: 0.8em;
    margin-bottom: 0.3em;
    color: #222;
}

/* Lists */

ol {  /*Apaga el estilo automático y se toma el control */
    list-style: none;
    counter-reset: item;
    margin-left: 0;
    padding-left: 0.5em; /* 1em */
}

ol li {  /* Crea un numerado y formato propio con ") " */
    counter-increment: item;
}

ol li::before {
    content: counter(item) ") ";
    font-weight: bold;
}


/* =========================
   BLOQUES DE CONTENIDO
   ========================= */

/* Ejemplos: bloque visual con sangría */
.ejemplo {
    margin: 0.5em 0;
    padding-left: 0.5em; /* 1em */
    border-left: 2px solid #1F4E79;
}

/* Actividades: sin color, solo orden */
.actividad {
    margin: 0.5em 0;
    padding-left: 0.5em; /* 1em */
}

/* Soluciones: más discretas */
.soluciones {
    margin-top: 0.5em;
    font-size: 0.8em;
    /* color: #333333; /* Más oscuro */
    color: #808080; /* Más claro */
}

/* Pie de figura */
.pie {
    font-size: 0.7em;
    /* color: #333333; /* Más oscuro */
    color: #808080; /* Más claro */
}

/* Fuente */
.fuente {
    font-size: 0.5em;
    /* color: #333333; /* Más oscuro */
    color: #808080; /* Más claro */
}

/* Advertencias + visibles (raras) */
.advertencia {
    font-size: 0.8em;
    color: #f44336; /* Rojo */
}




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

  /* Evita que los bloques se corten en medio */
  .ejemplo,
  .actividad,
  .respuestas {
    break-inside: avoid;
  }

}
</style>
