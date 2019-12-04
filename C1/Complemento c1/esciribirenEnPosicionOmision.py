# escribirEnPosicionOmision: int int --> None
# dado un numero, escribe los digitos
# de este numero que esten en la posicion
# contando de derecha a izquierda
# Por ejemplo: escribirEnPosicion(624301)
# escribe 1, 3, 4 y 6
# Ejemplo, escribirEnPosicionOmision(423) escribe 2
# Ejemplo, escribirEnPosicionOmision(432, 2) escribe 2
# Ejemplo, escribirEnPosicionOmision(432, 3) no escribe nada
def escribirEnPosicionOmision(numero, posicion = 1):
    if numero / 10 == 0:  # Acaso queda solo 1 digito?
        if (posicion == numero):  # si esta en su posicion se escribe
            print posicion
    else:
        # se toma el primer digito
        digito = numero % 10
        # si con iguales se escribe en pantalla
        if digito == posicion:
            print posicion
        # se revisa el resto del numero, incrementando la posicion
        escribirEnPosicionOmision(numero / 10, posicion + 1)



# Se puede llamar con solo un parametro
print "Llamada sin parametros:"
escribirEnPosicionOmision(624301)

# Pero tambien se puede llamar con dos parametros
print "Llamada con parametros:"
escribirEnPosicionOmision(624301, 1)
