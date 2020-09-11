entero1= int(input('ingrese el primer numero entero'))
entero2= int(input('ingrese el segundo numero'))

if entero1>entero2:
    calculo1 = (entero1**2) / (entero2**2)
    print(f'el resultado es {calculo1}')
else:
    calculo2= (entero2**2)/ (entero1**2)
    print(f'el resultado es {calculo2}')

if entero1==entero2:
    print(f'los numeros ingresados son iguales')
