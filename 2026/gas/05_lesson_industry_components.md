---
title: "Componentes de una instalación industrial"
autor: "José Juarez"
version: "05/08/26"
---

Todo el contenido de esta guía tiene como base las Normaticas NAG201 y NAG200.

<div hidden>Contenido resumido por Gemini Notebook con solo las NAG200 y NAG201 como fuentes</div>


<!-- *** GUIDE START *** -->

## 1. Normativa aplicable

En Argentina la NAG200 es la norma base para instalaciones domiciliarias y la NAG201 lo es para las instalaciones industriales.

La relación entre la NAG-200 y la NAG-201 es de complementariedad, donde la primera actúa como norma supletoria de la segunda en casos no previstos específicamente.

## 2. Diferencias entre una instalación industrial y domiciliaria

Las diferencias entre una instalación de gas industrial (NAG-201) y una domiciliaria (NAG-200) radican principalmente en la **escala de operación, los niveles de presión, la robustez de los materiales y la complejidad de los sistemas de seguridad**.

A continuación, se presenta un resumen de las principales diferencias según las fuentes:

- **Presión:** Las instalaciones domiciliarias se limita a presiones de hasta 28 mbar. Las industriales van de 19 hasta 3,95 bares.

- **Planta de Regulación y Medición:** La domiciliaria tiene un gabinete simple con un regulador y un medidor. La industrial cuenta con una **Planta de Regulación y Medición Primaria (PRMP)** más compleja.

- **Materiales y Métodos de Unión:** La domiciliaria permite una variedad de materiales como acero, cobre y sistemas de termofusión (acero-polietileno), con uniones roscadas, soldadas o mecánicas. En la industrial predominan las uniones soldadas.

- **Sistemas de Seguridad en los Equipos:**  La domiciliaria usa artefactos que suelen usar dispositivos simples como la termocupla para el corte por falta de llama. La industrial (calderas, hornos) requieren sistemas automatizados complejos.

- **Protección y Entorno de la Instalación:** Las instalaciones industriales deben contar con protección catódica cuando corresponde, instalaciones eléctricas antiexplosivas y recintos construidos y especialmente señalizados.


## 3. Componentes de una instalación industrial 

<div hidden>Resumen ChatGPT del contenido de Gemini Notebook de más abajo</div>

::: figure
![](D:/im/insti/industrial-utilities-7/images/gas/inst_industrial_componentes.png){width=500px}

<small>Fuente: Gustavo Serna P (canal youtube)</small>
:::

Los componentes esecíficos organizados por sistema son:

- **Planta de Regulación y Medición Primaria (PRMP):** Válvula de bloqueo general, filtros, reguladores de presión, válvulas de seguridad, medidor de gas, by-pass, precalentador (cuando corresponde) y juntas dieléctricas. [⌕](../../images/gas/inst_industrial_estacion_reguladora.png) 

- **Plantas de Regulación Secundarias:** Reguladores, manómetros y válvulas de bloqueo para sectores con distinta presión.

- **Sistema de Conducción:** Cañerías de acero, uniones, soportes y válvulas de bloqueo de sector.

- **Sistemas de Seguridad:** Válvulas automáticas de cierre, detectores de llama, sistema de prebarrido y presóstatos. 

- **Protección y Auxiliares:** Protección catódica, instalación eléctrica antiexplosiva (APE) y señalización reglamentaria.


<div hidden>
Resumen de Gemini Notebook

Los componentes específicos organizados por sistemas:

### 1) Planta de Regulación y Medición Primaria (PRMP)

Es el conjunto de elementos instalados en el punto de entrega para reducir la presión de la red externa a los valores operativos de la planta y registrar el consumo. Sus componentes críticos son:

*   **Válvula de bloqueo general:** De accionamiento manual y cierre rápido (1/4 de vuelta) para corte total en la entrada.
*   **Filtros y Separadores:** Retienen partículas sólidas (mayores a 80 micrones) y líquidos para proteger los reguladores y medidores.
*   **Reguladores de presión:** Reducen la presión de entrada y la mantienen constante.
*   **Válvulas de Seguridad:** Incluyen válvulas de **bloqueo por sobrepresión** (cortan el flujo) y válvulas de **alivio por venteo** (liberan gas al exterior) para proteger la instalación.
*   **Sistema de Medición:** Instrumentos (turbinas, rotativos o de diafragma) para medir el caudal, que suelen contar con una conexión de emergencia o **"by-pass"** para mantenimiento sin interrumpir el servicio.
*   **Elementos de Acondicionamiento:** **Precalentadores** (evitan la formación de hidratos por el enfriamiento del gas al expandirse) y **sistemas de odorización** si el gas se recibe inodoro.
*   **Juntas Dieléctricas:** Ubicadas a la entrada y salida para aislar eléctricamente la planta industrial de la red externa.

### 2) Plantas de Regulación Secundarias (Subestaciones)

Se instalan cuando determinados equipos o sectores de la fábrica requieren una presión de trabajo distinta a la regulada en la planta primaria. Cuentan con sus propios reguladores, manómetros y válvulas de bloqueo y venteo.

### 3) Sistema de Conducción (Cañerías y Accesorios)
*   **Cañerías:** Generalmente de acero sin costura. Sus diámetros y espesores se calculan para que la velocidad del gas sea siempre **inferior a 40 m/s**.
*   **Uniones:** En industria son predominantemente **soldadas**. Las uniones roscadas solo se admiten para diámetros menores o iguales a 51 mm (2") y bajo ciertas presiones.
*   **Soportes y Anclajes:** Diseñados no solo para sostener el peso, sino para resistir vibraciones y esfuerzos por dilatación térmica o reacciones de las válvulas de seguridad.
*   **Válvulas de bloqueo de sector:** Ubicadas al exterior de cada nave o local para independizar sectores de la fábrica en caso de emergencia.

### 4) Sistemas de Seguridad en los Equipos de Consumo
Los artefactos industriales (calderas, hornos) requieren un "tren de válvulas" y controles complejos:
*   **Válvulas Automáticas de Cierre (VAC):** Válvulas motorizadas que interrumpen el paso de gas al quemador de forma inmediata ante cualquier señal de falla del sistema de mando.
*   **Dispositivos de Control de Llama:** Sensores (varillas de rectificación o sensores UV) que verifican la presencia de llama y activan el bloqueo si esta se apaga.
*   **Sistemas de Prebarrido (Pre-purgado):** Ventiladores que barren gases acumulados en la cámara de combustión con aire limpio antes de habilitar el encendido.
*   **Presóstatos:** Sensores de alta y baja presión de gas y de aire de combustión que bloquean el equipo si los valores salen de rango.

### 5. Protección y Auxiliares
*   **Protección Catódica:** Obligatoria para cañerías enterradas con presión superior a 19 mbar para evitar la corrosión mediante ánodos galvánicos.
*   **Instalación Eléctrica APE:** En los recintos de regulación y medición, toda la iluminación y los interruptores deben ser **antiexplosivos**.
*   **Señalización y Pintado:** Identificación de cañerías por colores (amarillo para gas, naranja para venteos, etc.) y colocación de carteles de "Prohibido Fumar" y de operaciones.
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
