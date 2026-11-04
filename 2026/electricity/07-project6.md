---
title: "Proyecto - Etapa 6: Esquema de conexión a tierra y esquema unifilar"
autor: "José Juarez"
version: "04/11/26"
---

<!-- *** GUIDE START *** -->

## 1. Esquema de conexión a tierra y protección contra contactos indirectos

*Nota previa:* El dimensionamiento contra cortocircuitos entre conductores activos (fases) ya fue verificado y aprobado en el paso anterior. En este punto se abordará exclusivamente la **falla a tierra** y la **protección de las personas contra contactos indirectos**.

### Actividad

::: activity

Basándose en las Cláusulas **771.3** ("Esquemas de conexión a tierra") y **771.18** ("Protección de las personas contra los choques eléctricos") de la Reglamentación, desarrolle los siguientes ítems en su memoria técnica:

**a)** **Selección y Justificación del Esquema de Conexión a Tierra (ECT):** Para esto identifique la fuente de alimentación de su proyecto:

- **Caso A (Red Pública de BT):** Si la instalación se alimenta directamente desde la red de distribución urbana en Baja Tensión, especifique el ECT exigido obligatoriamente por la subcláusula 771.3.2. Dibuje o describa el lazo de falla correspondiente.
- **Caso B (Transformador propio MT/BT o Generador):** Si su proyecto contempla un centro de transformación propio dentro del predio o un grupo electrógeno, justifique la adopción del esquema correspondiente (ej. TN-S según 771.3.3.2.1) indicando las condiciones particulares que exige la norma.

**b)** **Selección de la Protección contra Contactos Indirectos:**

- De acuerdo con el ECT seleccionado, justifique qué dispositivo de protección debe instalarse para el corte automático de la alimentación (Subcláusula 771.18.4.3). 
- En caso de utilizar **Interruptor Diferencial (ID)** en esquema TT, especifique su sensibilidad $I_{\Delta n}$ y verifique que se cumpla la condición de tensión límite de contacto permanente $U_L \le 24\text{ V}$ considerando una resistencia de puesta a tierra $R_a \le 40\,\Omega$.

**c)** **Dimensionamiento del Sistema de Puesta a Tierra (PAT):**

- Determine la sección del conductor de protección (PE) y del conductor de puesta a tierra (SPAT) utilizando la **Tabla 771.18.III**.
- Indique las características constructivas de la toma de tierra (jabalina normalizada, cámara de inspección según 771.18.5.4 y ubicación respecto a la tierra de servicio).

## 2. Esquema Unifilar

<div hidden>
Borre lo de diseño de tablero que va incluído en el título, también lo borré de la consigna por cuestión de tiempo
**¿Por qué es necesario este punto si ya eligieron el guardamotor y el diferencial?**
Aunque los alumnos ya hayan calculado los calibres sueltos de las protecciones, en la práctica profesional **esos componentes deben integrarse dentro de un tablero físico y representarse en un plano técnico oficial**. 

El diseño del tablero y el esquema unifilar no es solo "juntar las llaves", sino cumplir con las exigencias constructivas y de presentación gráfica fijadas en la **Cláusula 771.20** y en la **Tabla 771.18.II** de la norma.

#### **¿Qué deben incluir y entregar los alumnos en el Punto 8?**

El Punto 8 se divide en dos aspectos fundamentales: **el diseño físico de la envolvente** y **la gráfica del esquema unifilar**.

8. DISEÑO DE TABLEROS ELÉCTRICOS Y ESQUEMA UNIFILAR

8.1 Especificación Constructiva del Tablero (Cláusula 771.20)
Los alumnos deberán definir las características del gabinete/envolvente que alojará los componentes:
1. Clasificación del Tablero: Definir si se trata de un Tablero Principal (TP), Tablero Seccional General (TSG) o Tablero Seccional de Fuerza Motriz (TSFM).
2. Grado de Protección (IP): Especificar el IP de la envolvente según su ubicación (ej. IP41 para interior limpio o IP54/IP65 para intemperie o ambiente industrial con polvo/humedad).
3. Tipo de Aislación y Material: Indicar si el gabinete es de material aislante (Clase II / Doble Aislación) o metálico con su correspondiente conexión a tierra.
4. Dispositivos de Cabecera y Seccionamiento: Especificar el interruptor principal del tablero, garantizando el corte omnipolar (seccionamiento del neutro si aplica, subcláusula 771.20.5.1).
5. Reserva Física Obligatoria: Garantizar el espacio de reserva libre en riel DIN dentro del gabinete según lo exige la subcláusula 771.20.4 (típicamente entre un 20 % y un 50 % de espacio libre adicional).
6. Barras de Distribución y PE: Especificar la bornera o barra colectora de Puesta a Tierra (PE / BPT) donde acometen los conductores verde-amarillo.
7. Señalización y Rotulado: Incluir la exigencia del símbolo de "Riesgo Eléctrico" (IRAM 10005-1) en el frente y la identificación unívoca de cada circuito.

</div>

### Actividad

::: activity
Diseñe el esquema unifilar del tablero utilizando la simbología normalizada del Anexo 771-K y guiándose por la estructura gráfica de distribución de la Figura 771.6.A y del Anexo 771-F. Complete la lámina indicando al lado de cada dispositivo y línea los datos técnicos obligatorios exigidos en la Tabla 771.18.II (calibres, secciones de conductor, capacidad de ruptura y características de actuación)
:::

<div hidden>

SOLUCIÓN

ESQUEMA DE PUESTA A TIERRA Y PROTECCIÓN CONTRA CONTACTOS INDIRECTOS

7.1 Adopción del Esquema de Conexión a Tierra (ECT)
De acuerdo con lo establecido en las Cláusulas 771.3.3.1 y 771.18.5.1 de la norma AEA 90364-7-771, la instalación adopta el Esquema de Conexión a Tierra TT:
- Neutro de la red pública conectado a tierra de servicio (Rb) por la empresa distribuidora.
- Masas eléctricas de la instalación (incluyendo la carcasa metálica del motor y tableros) conectadas mediante un conductor de protección aislada (PE) color verde-amarillo a una toma de tierra de protección independiente (Ra).
- Resistencia de la toma de tierra de protección: Se garantiza un valor permanente Ra ≤ 40 Ω mediante electrodo normalizado (jabalina) alojado en cámara de inspección.

7.2 Justificación de la Protección contra Contactos Indirectos
En el Esquema TT, la corriente de falla a tierra (Id) queda limitada por la impedancia del lazo de tierra (Ra + Rb), resultando en valores que no garantizan el disparo magnético instantáneo del guardamotor. 

Por lo tanto, en cumplimiento de la Subcláusula 771.18.4.3, la protección contra contactos indirectos por desconexión automática de la alimentación se realiza exclusivamente mediante un Interruptor Diferencial (ID).

7.3 Verificación de Seguridad y Tensión de Contacto
- Sensibilidad del Interruptor Diferencial seleccionado: IΔn = 30 mA (0,03 A) [o 300 mA si aplica en entorno industrial con personal BA4/BA5].
- Tensión límite de contacto máxima admisible: UL = 24 V (locales húmedos / industriales).
- Verificación de la condición de seguridad:
  U_contacto = IΔn · Ra = 0,03 A · 40 Ω = 1,2 V

Dado que 1,2 V es sensiblemente menor que la tensión límite de 24 V (y 50 V), queda garantizada la desconexión automática de la alimentación antes de que se produzca un riesgo eléctrico para las personas ante una falla de aislación en la masa del motor.

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
