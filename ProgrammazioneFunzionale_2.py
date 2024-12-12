import functools
from itertools import chain

l = 'una volta sono andato a mangiare la pizza con i miei amici da terra mia ma purtroppo non  era terra mia di castelfranco emilia ma era terra mia di modena...'
o = 'Oggi ho vinto 30 euro alle macchinette'
i = 'Sono frociooooooooo'
d = 'Non ho paura oggi per quello mi sono rialzato'
s = 'Pensa te che frocio devo essere per parlare come il Ferrando..'

h = chain(l,o,i,d,s)

print(functools.reduce(lambda x, y: x | {y: x.get(y, 0) + 1}, h, {}))