from functools import *
from collections import Counter

l = 'una volta sono andato a mangiare la pizza con i miei amici da terra mia ma purtroppo non  era terra mia di castelfranco emilia ma era terra mia di modena...'


f = filter(lambda x:x not in 'aeiou \n \t \b . ',l)
g = map(lambda y:y.upper() , f)

h = Counter(g)
print(h)

