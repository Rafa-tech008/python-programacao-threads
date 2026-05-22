#OP.THR.2
#Declaração de variáveis

#Início

import multiprocessing
import random
import time 

def operac_soma (ID, val1, val2, val3, val4, val5):
    id: int = 0
    cont: int = 0
    soma: int = 0
    linha: int = 1
    valores = []*6

    id = ID
    linha = 0
    valores = [val1, val2, val3, val4, val5]

    print (f"Início da Thread #{id}")
    for cont in valores:
        soma += cont
        linha += 1
        time.sleep (0.2)
        print (f"Na thread #{id} a soma da linha {linha} é igual a {soma}. ")
    print (f"O resultado final da Thread #{id} é igual a {soma}")



def main ():
    a: int = 0
    r: int = 0
    x: int = 0
    y: int = 0
    z: int = 0
    id: int = 0
    n_thr: int = 0
    params = [(0, 0, 0, 0, 0, 0)]*3

    n_thr = 3

    for id in range (3):
        a = random.randint (1, 100)
        r = random.randint (1, 100)
        x = random.randint (1, 100)
        y = random.randint (1, 100)
        z = random.randint (1, 100)    
        params [id]= (id+1, a, r, x, y, z)
    print (params)

    with multiprocessing.Pool (processes=n_thr) as pool:
        pool.starmap (operac_soma, params)
    

if (__name__ == "__main__"):
    main ()

#Fim