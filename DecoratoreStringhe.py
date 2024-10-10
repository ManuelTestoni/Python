import  functools


lista = []

def concatenaStringhe(*args, separator="-" ):

    lista = args
    print(functools.reduce(lambda x,y: x+separator+y, args ))

concatenaStringhe('ciao', 'sono', 'un', 'gamer') #, separator="+") se si volesse cambiare il separatore potremmo fare così.
