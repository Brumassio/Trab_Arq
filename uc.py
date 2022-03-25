from instrucao import Instrucao
class Uc:
    def __init__(self):
        self.pc=[]
        self.count=0

    def setMar(self):
        self.mar=self.pc[self.count]

    def adicionarInstrucao(self, instrucao:Instrucao):
        self.pc.append(instrucao)
        
    def  incrementarPc(self):
        self.count+=1
        self.pc[self.count]
        
    def printarPcAtual(self):
        print(self.pc[self.count].getOpcode())
        print(self.pc[self.count].getInstrucao())