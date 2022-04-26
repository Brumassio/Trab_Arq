import opcode
from instrucao import Instrucao
from tools import *

class Uc:
    def __init__(self):
        self.pc=[]
        self.count=-1


    def setMar(self):
        print(self.count)
        self.mar=self.pc[self.count]
        
    def setRegistradores(self):
        self.ir=self.mbr.opcode
        

    def adicionarEnderecoPc(self, endereco):
        self.pc.append(endereco)
        
    def  incrementarPc(self):
        self.count+=1


        
    # def printarPcAtual(self):
    #     print(self.pc[self.count].getOpcode())
    #     print(self.pc[self.count].getInstrucao())

    # def printarTudo(self):
    #     while self.uc.count <=len(self.uc.pc)-1:
    #         self.uc.setMar()
    #         print(self.uc.pc[self.uc.count])
    #         self.uc.incrementarPc()    

    def buscaMemoria(self, memory):
       endereco= int(self.mar,2)
       if len(memory)>endereco:
            print(f"MBR recebe a instrucao:\nOpcode: {memory[endereco].getOpcode()}\nOperando: {memory[endereco].getOperando()}")
            self.mbr=memory[endereco]
            return 1
       return 0
       
    def realizaOperacao(self, ula):
        operando  =self.mbr.operando
        ac=ula.readAC()                                        
        mq=ula.readMQ()                                        
        if self.mbr.opcode =="0001":

            if self.mbr.operando[:6]=="000000":
                resultado= ula.soma(ac,operando[7:])
                print(f"resultado soma={resultado}")
                return resultado
            elif self.mbr.operando[7:]=="000000":
                resultado=ula.soma(ac,operando[:6])
                print(f"resultado soma={resultado}")
                return resultado
            else:
                resultado=ula.soma(operando[:6],operando[7:])
                print(f"resultado soma={resultado}")
                return resultado

        elif self.mbr.opcode =="0010":

            if self.mbr.operando[:6]=="000000":
                resultado=ula.subtracao(ac,operando[7:])
                return resultado
            elif self.mbr.operando[7:]=="000000":
                resultado=ula.subtracao(ac,operando[:6])
                return resultado
            else:
                resultado=ula.subtracao(operando[:6],operando[7:])
                return resultado

        elif self.mbr.opcode =="0011":
            if self.mbr.operando[:6]=="000000":
                resultado=ula.divisao(mq,operando[7:])
                return resultado
            elif self.mbr.operando[7:]=="000000":
               resultado=ula.divisao(mq,operando[:6])
               return resultado
            else:
                resultado=ula.divisao(operando[:6],operando[7:]) 
                return resultado
                
        elif self.mbr.opcode =="0100": 
            
            if self.mbr.operando[:6]=="000000":
                 resultado=ula.multiplicacao(mq,operando[7:])
                 return resultado
            elif self.mbr.operando[7:]=="000000":
                resultado=ula.multiplicacao(mq,operando[:6])
                return resultado
            else:
                resultado=ula.multiplicacao(operando[:6],operando[7:])
                return resultado
            
        return resultado