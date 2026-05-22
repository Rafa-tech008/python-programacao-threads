#OP.THR.4
#Declaração de variáveis

#Início

import time
import platform
import subprocess
import multiprocessing

def sequence (nome, comand):
    vetor = []
    linha: str = ''
    saida: str = ''

    sys = platform.system ()

    if (sys == "Linux"):
        linha = ' '
        vetor= comand.split (' ')
        saida = subprocess.Popen (vetor, stdout = subprocess.PIPE)
        linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')
        while (linha != ''):
            time.sleep (0.05)
            if ('time' in linha):
                partes= linha.split ('=')
                if (len (partes) > 3):
                    temp = (partes [3].strip ())
                    print (f"O processo {nome} roda:", temp)
            if ('avg'in linha):
                parte= linha.split ('=')
                valor = parte [1].split ('/')
                avg = (valor [1].strip ())
                print (f"O processo {nome} termina:", avg)
            linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')
        

    elif (sys == "Windows"):
        linha = ' '
        vetor= comand.split (' ')
        saida = subprocess.Popen (vetor, stdout = subprocess.PIPE)
        linha = saida.stdout.readline().decode('cp850', errors = 'ignore')
        while (linha != ''):
            time.sleep (0.05)
            if ('time' in linha.strip()):
                partes= linha.split (' ')
                temp = (partes [2].strip ())
                temp = (temp.split () [0])
                print (f"O processo {nome} roda:", temp)
            if ('Média'in linha.strip()):
                parte= linha.split ('Média =')
                avg = (parte [1].strip ())
                print (f"O processo {nome} termina:", avg)
            linha = saida.stdout.readline().decode('cp850', errors = 'ignore')

def receber_conteudo (cont):
    params = [(0, 0, 0)]
    procg, proct, procu = cham_proc ()
    cont = 3

    n1 = 'google'
    n2 = 'terra'
    n3 = 'uol'
    params = [(n1, procg), (n2, proct), (n3, procu)]

    with multiprocessing.Pool (processes = cont) as pool:
        pool.starmap (sequence, params)


def cham_proc ():
    sys: str = ''
    procg: str = ''
    proct: str = ''
    procu: str = ''
    sys = platform.system ()

    if (sys == "Linux"):
        procg = ('ping -4 -c 10 www.google.com.br')
        proct = ('ping -4 -c 10 www.terra.com.br')
        procu = ('ping -4 -c 10 www.uol.com.br')

    elif (sys == "Windows"):
        procg = ('ping -4 -n 10 www.google.com.br')
        proct = ('ping -4 -n 10 www.terra.com.br')
        procu = ('ping -4 -n 10 www.uol.com.br')

    return procg, proct, procu



def main ():
    contador: int= 0
    
    cham_proc ()
    receber_conteudo (contador)


if (__name__ == "__main__"):
    main ()


#Fim