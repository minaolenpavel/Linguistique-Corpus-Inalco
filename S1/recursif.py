from time import sleep
from random import randint

#def f1(num:int) -> int:
#    return num

#def f2(num:int):
#    global i
#    i+=1
#    print(i)
#    if i >= num:
#        return True
#    else:
#        i = f2(num)
#i = 0


def ping(max:int, i = 0):
    i+=1
    sleep(randint(0,3))
    print("ping", i)
    if i == max:
        return True
    else:
        pong(max, i)
    
def pong(max:int, i = 0):
    i+=1
    sleep(randint(0,3))
    print("pong", i)
    if i == max:
        return True
    else:
        ping(max, i)

ping(100)