from instrucao import Instrucao
from uc import Uc              
import numpy as np
from tools import *
from auxliar import *
from ula import *

# lista = []
memory=np.array(range(255))


uc= Uc()
# ula= ula()
memory[1]=Instrucao("0101", "101010100001")

uc.adicionarEnderecoPc("00000001")

memory[2]=Instrucao("0100", "101000000001")

uc.adicionarEnderecoPc("00000010")


# uc.printarTudo()

while uc.count <=len(uc.pc)-1:
    uc.setMar()
    if uc.buscaMemoria():#seta o mbr
        uc.setRegistradores()
        uc.realizaOperacao()
    

    uc.incrementarPc()

    


n1="0110"
n2="110"
resultado=""
carryin=0

  
#print(resultado)


# stringas = "100100"

# soma(n1,n2)
# igualaCasas(n1,n2)

multiplicacao(n1,n2)


# print(soma(soma(soma("0000000","0001100"),"0011000"),"0110000"))

# stringas = complementoDois(stringas)
# print(stringas)  
# print(transformarNegativo(stringas))

# teste1 = "101"
# teste2 = "111"
# print(multiplicacao(teste1,teste2))
# print(stringas)
        
# divisao("1000111","1000")