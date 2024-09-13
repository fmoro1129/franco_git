try:
    perimetro=float(input("ingrese la medida de su perimetro: "))
except ValueError:
    print("ingrese datos validos, pruebe volver a ejecutar el programa.")
PI=3.14*2
radio=perimetro/PI
print (f"el radio del circulo es: {radio}")