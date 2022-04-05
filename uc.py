from instrucao import Instrucao
class Uc:
    def __init__(self):
        self.pc=[]
        self.count=0


    def setMar(self):
        self.mar=self.pc

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
       memory[endereco]
       self.mbr