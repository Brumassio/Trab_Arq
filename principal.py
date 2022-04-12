from instrucao import Instrucao
from uc import Uc
import numpy as np
from tools import *
from auxliar import *

lista = []
memory=np.array(range(255))


# uc= Uc()
# memory[1]=Instrucao("0101", "10101010")

# uc.adicionarEnderecoPc("00000001")

# memory[2]=Instrucao("0100", "10100000")

# uc.adicionarEnderecoPc("00000010")


# uc.printarTudo()

# while uc.count <=len(uc.pc)-1:
#     uc.setMar()
#     # uc.buscaMemoria()
#     # uc.realizarOperacao()

#     uc.incrementarPc()



        

    
# print(uc.count)
# for i in range(uc.count):
#     if uc.count <= len(uc.pc):
#         uc.setMar()
#         print(uc.mar)
#         uc.incrementarPc()

n1="0110"
n2="1010"
resultado=""
carryin=0

  
#print(resultado)


# stringas = "100100"

# soma(n1,n2)
# igualaCasas(n1,n2)

multiplicacao(n1,n2)
# stringas = complementoDois(stringas)
# print(stringas)  
# print(transformarNegativo(stringas))

# teste1 = "101"
# teste2 = "111"
# print(multiplicacao(teste1,teste2))
# print(stringas)
        
# divisao("1000111","1000")