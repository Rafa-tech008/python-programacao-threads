#OP.THR.3
#Declaração de variáveis

#Início

import multiprocessing 
import random
import time

def corrida (ID, salto, distp, distt):
    id = ID
    distt = 30
    
    print (f"O sapo {id + 1} inicia a corrida")
    while distp < distt:
        salto = random.randint (1, 5)
        distp += salto
        time.sleep (0.2)
        print (f"O sapo {id + 1} deu um salto de {salto}cm e percorreu {distp}cm")
    print (f"O sapo {id + 1} chegou!")    


def main ():
    id: int = 0
    salto: int = 0
    distp: int = 0
    distt: int = 0
    cont_threads: int = 0
    params = [(0, 0, 0, 0)]*5

    cont_threads = 5

    for id in range (5):
        params [id] = (id, salto, distp, distt)
        

    with multiprocessing.Pool (processes = cont_threads) as pool:
        pool.starmap (corrida, params)


if (__name__ == "__main__"):
    main ()

#Fim