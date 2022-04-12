# salve professor Felippe Fernandes  da Silva ! <3
# é us guri do python

#simulador do ciclo de instrução do computador.
# 1) Entrada de dados
# 2) ULA
    # 2.1) AC, MQ
# 3) UC
    # 3.1) MBR, MAR, IBR, IR, PC

# 4 bits para o opcode e 8 bits de referência dos operandos.
# ULA deve-se tratar overflow,
# valores negativos e positivos e realizar os cálculos necessários, além de
# outros registradores.

# Como implementar memória
# Como declarar var em Bits
# opcode e operando

# quer que limita as variaveis? 
# quer que implemente as operações?  Sim
# implementar memoria? Sim

from xml.etree.ElementTree import tostring
from instrucao import Instrucao
from uc import Uc
import numpy as np
from tools import *


#0100 Soma
#0101 Subtração
#0010 Divisão
#0001 Multiplicação
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
n2="1101"
resultado=""
carryin=0
# 1011
  
#print(resultado)


#Soma
# for i in range(len(n1)):
#     aux2 = int(n1[-(i+1)]) ^ int(n2[-(i+1)]) ^ carryin
#     resultado += str(int(aux2))
#     if ((int(n1[-(i+1)]) + int(n2[-(i+1)]))==2) or ((int(n1[-(i+1)]) ^ int(n2[-(i+1)]))==1 and carryin==1):
#           carryin=1
#     else:
#         carryin=0
# resultado += str(carryin)        
# print(resultado[::-1]) 






stringas = "100100"
complementoDois(stringas)


            

stringas = complementoDois(stringas)
print(stringas)  
print(transformarNegativo(stringas))

teste1 = "101"
teste2 = "111"
print(multiplicacao(teste1,teste2))
# print(stringas)
        