#OP.THR.1
#Declaração de variáveis

#Início

import multiprocessing
import random
import time 

def operac (param):
    time.sleep (0.5)
    print (f"Threads #{param}")


def main ():
    id: int = 0
    params = [0]*5
    n_threads: int = 0

    n_threads = 5

    for id in range (5):
        params [id] = id + 1

    with multiprocessing.Pool (processes=n_threads) as pool:
        pool.map (operac, params)

if (__name__ == "__main__"):
    main ()

#Fim