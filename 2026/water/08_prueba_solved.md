# Prueba: Instalaciones de Agua

## Claves de corrección

### 1) [1.25ptos]

#### a)

Por Hazen-Williams, a igualdad de diámetro, tiene mayor pérdida la que tiene mayor caudal, es decir la boquilla 8.0 

$h_f = 10.67\frac{LQ^{1.852}}{C^{1.852}D^{4.87}}$

Donde: h_f: pérdida de carga (m.c.a.), L: longitud de cañería (m), Q: caudal m³/s, D: diámetro interno (m), C: coeficiente del material

#### b)

- Diámetro: $D = \sqrt{\frac{4Q}{\pi v}}$
- Velocidad: 1.2 m/s
- Q: 36 lit/min * m3/1000lit * 1min/60seg


```python
Vel = 1.2 # m/seg
Q = 36 / (1000*60) # m3/seg
print(f"Caudal en m3/seg: {Q}")
Dm = ((4*Q)/(3.14*Vel))**(1/2) # metros
Dmm = Dm*1000 # mm
print(f"Diámetro en mm: {Dmm}")
```

    Caudal en m3/seg: 0.0006
    Diámetro en mm: 25.23772325625344
    


```python

```
