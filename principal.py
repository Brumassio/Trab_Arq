from instrucao import Instrucao
from uc import Uc              
from tools import *
from ula import *
from pipeline import *

# lista = []
memory= [None]*255


uc= Uc()
ula= ula()
memory[1]=Instrucao("0001", "001010100001")

uc.adicionarEnderecoPc("00000001")

memory[2]=Instrucao("0100", "001000000001")

uc.adicionarEnderecoPc("00000010")

memory[3]=Instrucao("0100", "000000000001")

uc.adicionarEnderecoPc("00000011")

memory[4]=Instrucao("0011", "000000000011")

uc.adicionarEnderecoPc("00000100")

memory[5]=Instrucao("0010", "000000000111")

uc.adicionarEnderecoPc("00000101")

pipeline = Pipeline()
pipeline.carroChefe(uc,memory,ula)



#TESTE DAS OPERACOES
# n1="0110"
# n2="110"
# resultado=""
# carryin=0

  
#print(resultado)


# stringas = "100100"

# soma(n1,n2)
# igualaCasas(n1,n2)



# print(soma(soma(soma("0000000","0001100"),"0011000"),"0110000"))

# stringas = complementoDois(stringas)
# print(stringas)  
# print(transformarNegativo(stringas))

# teste1 = "101"CLS
# teste2 = "111"
# print(multiplicacao(teste1,teste2))
# print(stringas)
        
# divisao("1000111","1000")