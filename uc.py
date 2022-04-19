import opcode
from instrucao import Instrucao
class Uc:
    def __init__(self):
        self.pc=[]
        self.count=0


    def setMar(self):
        self.mar=self.pc

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
       endereco= int(self.pc[self.count].getEndereco())
       if len(memory)>endereco:
            self.mbr=memory[endereco]
            return 1
       return 0
       
    def realizaOperacao(self, ula):
        operando  =self.mbr.operando
        ac=ula.ac
        mq=ula.mq
        if self.mbr.opcode =="0001":
            # self.ac += self.mbr.mantica
            ula.soma(operando,ac)
        elif self.mbr.opcode =="0010":
            # self.ac += self.mbr.mantica
            ula.subtrai(operando,ac)
        elif self.mbr.opcode =="0011":
            ula.divide(operando,ac)     
        elif self.mbr.opcode =="0100": 
            # self.mq += self.mbr.mantica
            ula.multiplicacao(operando,mq)
