from threading import Thread
from tools import *
import os
import time
class Pipeline:
    def __init__(self):
        self.etapa = [-1]*5
        self.using=[[]]*5
        self.tratar=[1]*5
        # self.matrix=[[0]*8]*5

    # def carroChefe(self,uc,memory,ula):
    #     i=0
    #     limite=1
    #     while self.etapa[4]!=4:
    #         while(i<limite):
    #             if(self.etapa[i]!=4):
    #                 print("oi felippe fernandes")
    #                 self.inicializaPipiline(i,uc,memory,ula)
    #             i+=1
    #         if limite<5:
    #             limite+=1
    #         i=0

    def carroChefe(self,uc,memory,ula):
        limite=0
        clock=0
        threads=[]
        while(limite<5):
            procedure=Thread(target=self.inicializaPipiline, args=[limite,uc,memory,ula])
            procedure.start()
            threads.append(procedure)
            limite+=1
        i=0
        limite=1
        while self.etapa[4]!=4:
            print("CLOCK=",clock)
            while(i<limite): 
                if(self.etapa[i]!=4):
                   self.etapa[i]+=1
                    # print("oi felippe fernandes")
                i+=1
                time.sleep(0.25)
            time.sleep(2)
            clock+=1
            if limite<5:
                limite+=1
            i=0

                


    # def inicializaPipiline(self,i,uc,memory,ula):
    #     if(self.etapa[i]==0):
    #         self.buscaInstrucao(uc)
    #         self.etapa[i]+=1   
    #     elif self.etapa[i]==1:

    #         if uc.buscaMemoria(memory):#seta o mbr
    #             print("IR recebendo o opcode (self.ir = self.mbr.opcode)")
    #             uc.setRegistradores()

    #             self.etapa[i]+=1
    #     elif self.etapa[i]==2:
    #         print("Realizando operacao...")
    #         uc.realizaOperacao(ula)
    #         self.etapa[i]+=1
    #     elif self.etapa[i]==3:
    #         uc.incrementarPc()
    #         self.etapa[i]+=1

    def inicializaPipiline(self,i,uc,memory,ula):
        
        while self.etapa[i] == -1:
            time.sleep(0)
        #Etapa1 - Busca e Decodifica
        j=0
        while self.etapa[i] == 0:
            # if(self.tratar[i] % 2 !=0):
            #     self.using[i].clear()
            #     self.using[i].append("MAR")
            #     if(i==0):
            #         self.tratar[i]+=1
            #     else:
            #         for aux in self.using[i-1]:
            #             for aux2 in self.using[i]:
            #                 if(aux==aux2):
            #                     print("HAZARD")
            #                     return
                
            # if j==0 and self.tratar[i]%2==0:
            #     uc.incrementarPc()
            #     self.buscaInstrucao(uc)
            #     j+=1

             if j==0:
                uc.incrementarPc()
                self.buscaInstrucao(uc)
                j+=1
            
        
        #Etapa2 - Busca na Memoria e Seta os registradores
        print(f"Buscando na memoria a instrucao...")
        j=0
        while self.etapa[i] == 1:
            if j==0:
                if uc.buscaMemoria(memory):#seta o mbr
                    print("IR recebendo o opcode (self.ir = self.mbr.opcode)")
                    uc.setRegistradores()
                j+=1
            
        
        #Etapa3 - Realiza as operacoes
        print("Realizando operacao...")
        j=0
        while self.etapa[i] == 2:
            if j==0:
                resultado=uc.realizaOperacao(ula)
                print(f"Resultado Instrucao({i}) = {resultado}")
                j+=1


        j=0
        #Etapa4 - Incrementa  o pc
        # while self.etapa[i] == 3:
        #     if j==0:
                
        #         j+=1
        #     time.sleep(0.25)
        

    def buscaInstrucao(self,uc):
        uc.setMar()
        print(f"MAR recebendo PC na posição count (Endereco Instrucao = {uc.mar})")
       
    

    def buscaMemorias(uc,memory,ula):
        if uc.buscaMemoria(memory):#seta o mbr
            print("IR recebendo o opcode (self.ir = self.mbr.opcode)")
            uc.setRegistradores()
            print("Realizando operacao...")
            uc.realizaOperacao(ula)
    