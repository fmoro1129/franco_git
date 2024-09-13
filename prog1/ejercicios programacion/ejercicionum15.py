try:
    radio=int(input("ingrese el radio de su circulo: "))
except ValueError:
    print("el valor ingresado no es valido, pruebe ingresar un numero entero.")
PI=3.14
superficie=radio*2 * PI
print (f"La superficie de su circulo es:{superficie}")