print("\n\n--- Problema 1 (Fig. phys_calc_presion8.png) ---\n")
print("Altura nivel agua = ha = 6 m")
ha = 6
print("Altura ducha = hd = 4.2 m")
hd = 4.2
p = ha - hd # mca
print (f"Pesión ducha: {p} mca")
p_kgfcm2 = p/10 # mca  1 kgf/cm2
                #      10 mca
print(f"""Transformando:
 mca * 1 Kgf/cm2 = {p_kgfcm2} kgf/cm2
       10 mca""")

print("")
print("\n--- Problema 2 (Fig. intensific_ae_1.png)  ---")
print("Altura nivel agua en m = ha = 0.7 + 5 = 5.7")
ha = 0.7 + 5 # m
print (f"Pesión agua: {ha} mca")
p_bar = (ha * 0.9807)/10 # mca  1 kgf/cm2   0.9807 bar
                         #      10 mca      1 Kgf/cm2
print(f"""Entonces:
 mca  *  1 Kgf/cm2  *  0.9807 bar  =  {p_bar} bares
         10 mca        1 kgf/cm2""")





  

