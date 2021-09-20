"""
Ejercicio 1.7: La hipoteca de David
David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. 
Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

Ejercicio 1.8: Adelantos
Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.
Modificá el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos.

Ejercicio 1.9: Calculadora de adelantos
¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?

Ejercicio 1.10: Tablas
Modicá tu programa para que imprima una tabla mostrando el mes, el total pagado hasta el momento y el saldo restante.

Ejercicio 1.11: Bonus
Ya que estamos, corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.

"""
#Ejercicio 1.7
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))


#Ejercicio 1.8
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0

while saldo > 0:
    mes+=1
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    if mes <= 12:
        total_pagado +=1000
        saldo-=1000
print('Total pagado', round(total_pagado, 2))


#Ejercicio 1.9/1.10/1.11 
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes+=1
    if pago_mensual < saldo:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado += pago_mensual
        if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
            total_pagado += pago_extra
            saldo -= pago_extra
    else: 
        total_pagado +=saldo
        saldo -= saldo

    print(f"Mes: {mes} | Total pagado: {round(total_pagado, 2)} | Deuda: {round(saldo, 2)}")
    
print('Total pagado', round(total_pagado, 2))
print('Meses:', mes)