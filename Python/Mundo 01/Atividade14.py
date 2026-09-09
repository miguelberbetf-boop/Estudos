temC = float(input('Temp em °C: '))
cvt = (temC*9/5)+32
if cvt >= 64.4:
    print(f'Está fazedo {cvt} °F\n Está frio, use casaco!!')
else:
    print(f'Hoje está fazendo {cvt}°F\n Está bom para ir a praia!!')
