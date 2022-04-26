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

# class Pipeline:
#     def __init__(self):
#         self.etapa = [None]*5

#     def carroChefe(self,uc,memory,ula):
#         i=0
#         limite=1
#         while self.etapa[4]!=4:
#             while(i<limite):
#                 if(self.etapa[i]!=4):
#                     self.inicializarPipiline(i,uc,memory,ula)
#                 i+=1
#             if limite<=5:
#                 limite+=1
#             i=0


#     def inicializaPipiline(self,i,uc,memory,ula):
#         if(self.etapa[i]==0):
#             self.buscaInstrucao(uc)
#             self.etapa[i]+=1   
#         elif self.etapa[i]==1:
#              if uc.buscaMemoria(memory):#seta o mbr
#                 print("IR recebendo o opcode (self.ir = self.mbr.opcode)")
#                 uc.setRegistradores()
#                 self.etapa[i]+=1
#         elif self.etapa[i]==2:
#             print("Realizando operacao...")
#             uc.realizaOperacao(ula)
#             self.etapa[i]+=1
#         elif self.etapa[i]==3:
#             uc.incrementarPc()
#             self.etapa[i]+=1
        
        


   


# while uc.count <len(uc.pc):
    
#     uc.setMar()
#     print(f"MAR recebendo PC na posição count (Endereco Instrucao = {uc.mar})")
#     print(f"Buscando na memoria a instrucao...")
#     if uc.buscaMemoria(memory):#seta o mbr
#         print("IR recebendo o opcode (self.ir = self.mbr.opcode)")
#         uc.setRegistradores()
#         print("Realizando operacao...")
#         uc.realizaOperacao(ula)
    

#     uc.incrementarPc()


    # os.system("pause")
    


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