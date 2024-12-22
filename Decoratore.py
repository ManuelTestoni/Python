import time

def time_function(function):

    numeri = [10,20,30,40,50,60,70,80,90,100]
    def new_function(*args, **kwargs):
        lista = args
        data = time.gmtime(time.time())

        f = open("execution_log.txt", "x")
        f.writelines(data.tm_year, data.tm_mon, data.tm_mday, data.tm_hour, data.tm_min, data.tm_sec)
        som = somma(numeri)
        f.writelines("new_function", lista)
        f.close()
        return som
    return new_function
@time_function
def somma(*args, **kwargs):
    return sum(args)

s = time_function(somma)
print(s)