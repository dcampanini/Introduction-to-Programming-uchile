# escribirEnPosicion: int --> None
# dado un numero, escribe los digitos
# de este numero que esten en la posicion
# contando de derecha a izquierda
# Por ejemplo: escribirEnPosicion(624301)
# escribe 1, 3, 4 y 6
def escribirEnPosicion(numero):
    # es nencesario conocer la posicion
    # relativa del primer (cada) digito
    posicion = 1
    return mostrarEnPosicion(numero, posicion)


# mostrarEnPosicion: int int --> None
# dado un numero y una posicion, verifica
# si el primier digito del numero es igual
# a la posicion. Si lo es, lo escribe
# en pantalla. Luego incremente la posicion
# y revisa el resto del numero, sin el
# primer digito
# Ejemplo, mostrarEnPosicion(432, 2) escribe 2
# Ejemplo, mostrarEnPosicion(432, 3) no escribe nada
def mostrarEnPosicion(numero, posicion):
    if numero / 10 == 0: # Acaso queda solo 1 digito?
        if (posicion == numero):  # si esta en su posicion se escribe
            print posicion
    else:
        # se toma el primer digito
        digito = numero % 10
        # si con iguales se escribe en pantalla
        if digito == posicion:
            print posicion
        # se revisa el resto del numero, incrementando la posicion
        mostrarEnPosicion(numero / 10, posicion + 1)

        
escribirEnPosicion(624301)