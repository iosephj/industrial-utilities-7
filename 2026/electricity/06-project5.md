---
title: "Proyecto - Etapa 5: Verificación por caída de tensión"
autor: "José Juarez"
version: "27/10/26"
---

<!-- *** GUIDE START *** -->


Es la última etapa del procedimiento de dimensionamiento de cables de la norma **AEA 90364-7-771**. Su objetivo es verificar que, ante la circulación de la corriente del circuito, la tensión en los bornes del equipo no caiga por debajo de los límites admisibles.

## 1. Límites Admisibles por Norma (Subcláusula 771.13.b)

Para circuitos específicos de **motores**, la norma exige medir la caída de tensión desde el Tablero Principal hasta la caja de bornes del motor y verificar dos condiciones:

1. **En Régimen Permanente (Funcionamiento normal):** La caída de tensión no debe superar el **5%**.
   * En $380\text{ V}$ trifásico: $\Delta U_{\text{máx}} = 380\text{ V} \cdot 0,05 = \mathbf{19\text{ V}}$.
2. **Durante el Arranque del Motor:** La caída de tensión no debe superar el **15%**.
   * En $380\text{ V}$ trifásico: $\Delta U_{\text{máx, arr}} = 380\text{ V} \cdot 0,15 = \mathbf{57\text{ V}}$.


## 2. Procedimiento de Cálculo

En corriente alterna, el cálculo exacto de la caída de tensión requiere conocer la resistencia y la reactancia inductiva de cada cable, además del ángulo de desfase.

Para simplificar este cálculo, la norma (subcláusula 771.19.7 c) establece valores tabulados llamados GDC (Gradiente de Caída de Tensión), que reúnen estas características eléctricas en un único valor y permiten calcular la caída de tensión según la corriente, la longitud y la sección del cable.

### A. Cálculo de la Caída de Tensión en Régimen Permanente

Se utiliza la fórmula del Gradiente de Caída para cargas generales (con $\cos\phi = 0,8$):

$\Delta U_{\text{régimen}} = \frac{\text{GDC} \cdot I \cdot L}{S} \quad [\text{en Volts}]$

* **$\text{GDC}$ (Gradiente de Caída):** Buscar su valor en la norma. <span hidden>Para sistemas trifásicos en cobre, $\text{GDC} = \mathbf{0,035}\text{ }\frac{\text{V}\cdot\text{mm}^2}{\text{A}\cdot\text{m}}$.</span>
* **$I$:** Corriente nominal del motor (en Amperes).
* **$L$:** Longitud de la línea en metros (distancia entre tableros/bornes).
* **$S$:** Sección propuesta del cable (en $\text{mm}^2$).

::: note
**Nota:** Para variaciones pequeñas del $\cos\phi$, por ejemplo entre 0,85 y 0,75 se puede seguir usando este método sin inrtoducir un error significativo. Para valores muy distintos o cálculo exacto se usa la Fórmula General.
:::


### B. Cálculo de la Caída de Tensión durante el Arranque

Durante el arranque el motor puede demandar una corriente significativamente mayor a la nominal y, por el contrario, el factor de potencia puede caer bastante. Pero todo va a depender del tipo de arranque seleccinado.

#### *B. 1)* Caso especial del arranque con variador de frecuencia

En este caso la corriente durante el arranque queda acotada a la intensidad nominal ($I_{\text{arr}} \approx I_n$) con factor de potencia de régimen ($\cos\phi \approx 0,85$). Por lo tanto, la caída de tensión en el arranque resulta idéntica a la de régimen permanente cumpliendo holgadamente el límite normativo del 15 % exigido en el arranque.

#### *B. 2)* Caso en que sea otro tipo de arranque

Se puede usar la fórmula del gradiente pero seleccionando bien los valores de cada cosa:

$\Delta U_{\text{arranque}} = \frac{\text{GDC}_{\text{arr}} \cdot I_{\text{arr}} \cdot L}{S} \quad [\text{en Volts}]$

* **$\text{GDC}_{\text{arr}}$:** La norma da un valor para arranque directo considerando un $\cos\phi$ de 0,3. Es razonable usar este mismo valor para el caso del arranque estrella triángulo. En el caso de un arranque con soft starter daría un rsultado menos realista y muy conservativo pero se puede usar. Como alternativa en cualquier caso se puede usar el método con la fórmula exacta.
* **$I_{\text{arr}}$:** Corriente de arranque del motor de acuerdo al método de arranque seleccionado. Se pueden encontrar valores orientativos en la tabla de abajo.


| Método de Arranque | $I_{\text{arr}}$ | Caída de Tensión | 
| :--- | :--- | :--- | 
| Directo (DOL) | $5 \ldots 7 \cdot I_n$ *(típicamente $6 \cdot I_n$)* | **Máxima** (pico elevado instantáneo) |
| Estrella - Triángulo | $2 \ldots 2,5 \cdot I_n$ *(1/3 del directo)* | **Moderada** | 
| Soft-Starter | $2 \ldots 3,5 \cdot I_n$ *(configurable)* | **Baja y controlada** | 


## 3. Actividad

::: activity

Verificar con el método GDC la caída de tensión en régimen permanente y en el arranque justificando los valores que usa.

En caso de que no verifique seleccionar una sección mayor de cable y verificar de nuevo.
:::

::: warning
Para aprobar esta etapa se presenta en papel esta parte de la memoria descriptiva, ordenada y prolija. Se explica además oralmente lo escrito.
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
