from threading import Thread
from tools import *
import os
import time
class Pipeline:
    def __init__(self):
        self.etapa = [-1]*5
        self.using=[[]]*5
        self.tratar=[1]*5
        self.matrix=[list(range(1 + 20 * m, 1 + 20 * (m + 1)))
                            for m in range(5)]
        self.regClock=[]
        self.hazards=[]
        #0- PC
        #1- MAR
        #2- MBR
        #3- IR
        #4- AC
        #5- MQ
        


    def carroChefe(self,uc,memory,ula):
        limite=0
        self.clock=0
        threads=[]
        
        while(limite<5):
            procedure=Thread(target=self.inicializaPipiline, args=[limite,uc,memory,ula])
            procedure.start()
            threads.append(procedure)
            limite+=1
        i=0
        limite=1
        while self.etapa[4]!=3:
            print("CLOCK=",self.clock)
            print("ETAPA4= ",self.etapa[4])
            self.regClock.append("")
            while(i<limite): 
                if(self.etapa[i]!=4):
                    if(self.conditionHazard(self.etapa,self.etapa[i],limite,i)):
                        self.etapa[i]+=1
                    else:
                        break
                    # print("oi felippe fernandes")
                i+=1
                # time.sleep(1)
            time.sleep(1)
            self.clock+=1
            if limite<5 and limite==i:
                limite+=1
            i=0
            for j in range(5):
                for k in range(len(self.matrix[j])):
                    if type(self.matrix[j][k])==int:
                        print(f"[  ]",end = '')
                    else:
                        print(f"[{self.matrix[j][k]}]",end = '')
                print("\n")

        for j in range(self.clock):
            print("Clock ",j,"= ",self.regClock[j])

        

    def inicializaPipiline(self,i,uc,memory,ula):
        
        while self.etapa[i] == -1:
            time.sleep(0)
        #Etapa1 - Busca e Decodifica
        j=0
        while self.etapa[i] == 0:

             if j==0:

                uc.incrementarPc()
                self.buscaInstrucao(uc)
                print(f"adding na mtx BI..[{i}][{self.clock}]")
                self.matrix[i][self.clock]="BI"
                self.regClock[self.clock]+=f"Instrucao {i}: PC->{uc.pc[uc.count]}, MAR->{uc.mar} "
                j+=1
            
        
        #Etapa2 - Busca na Memoria e Seta os registradores
        print(f"Buscando na memoria a instrucao...")
        j=0
        while self.etapa[i] == 1:
            if j==0:
                if uc.buscaMemoria(memory):#seta o mbr
                    self.matrix[i][self.clock]="BM"
                    print(f"adding na bm..[{i}][{self.clock}]")
                    print("IR recebendo o opcode (self.ir = self.mbr.opcode)")
                    uc.setRegistradores()
                    self.regClock[self.clock]+=f"Instrucao {i}: MBR->{uc.mbr.opcode}|{uc.mbr.operando}, MAR->{uc.mar}, IR->{uc.ir} "
                j+=1
            
        
        #Etapa3 - Realiza as operacoes
        print("Realizando operacao...")
        j=0
        while self.etapa[i] == 2:
            if j==0:
                resultado, oper=uc.realizaOperacao(ula)
                self.matrix[i][self.clock]="RE"
                self.regClock[self.clock]+=f"Instrucao {i}: MBR->{uc.mbr.opcode}|{uc.mbr.operando}, AC->{ula.ac}, MQ->{ula.mq} "
                print(f"Resultado Instrucao({i}) = {resultado}")
                j+=1


        j=0
        #ETAPA 4 Write em ac ou mq
        print("Writing...")
        while self.etapa[i] == 3:
            if j==0:
                if oper=="ac":
                    ula.writeAC(resultado)
                    self.regClock[self.clock]+=f"Instrucao {i}: AC->{ula.ac} "
                elif oper=="mq":
                    ula.writeMQ(resultado)    
                    self.regClock[self.clock]+=f"Instrucao {i}: MQ->{ula.mq} "
                self.matrix[i][self.clock]="WR"
                j+=1
            time.sleep(0.25)
        

    def buscaInstrucao(self,uc):
        uc.setMar()
        print(f"MAR recebendo PC na posição count (Endereco Instrucao = {uc.mar})")
       
    

    def buscaMemorias(uc,memory,ula):
        if uc.buscaMemoria(memory):#seta o mbr
            print("IR recebendo o opcode (self.ir = self.mbr.opcode)")
            uc.setRegistradores()
            print("Realizando operacao...")
            uc.realizaOperacao(ula)
    
    def conditionHazard(self,etapas,etapa, limite,indice):
        if(etapa==-1):
            for i in range(limite):
                if(etapas[i]==1 and i!=indice):
                    self.matrix[indice][self.clock]="ZZ"
                    self.hazards.append("Hazard MAR")
                    return 0
        elif(etapa==0):
            for i in range(limite):
                if(etapas[i]==0 and i!=indice):
                    self.matrix[indice][self.clock]="ZZ"
                    self.hazards.append("Hazard MAR")
                    return 0
                elif(etapas[i]==2 and i!=indice):
                    self.matrix[indice][self.clock]="ZZ"
                    self.hazards.append("Hazard MBR")
                    return 0
        elif(etapa==1):
            for i in range(limite):
                if(etapas[i]==1 and i!=indice):
                    self.matrix[indice][self.clock]="ZZ"
                    self.hazards.append("Hazard MBR")
                    return 0
                elif(etapas[i]==3 and i!=indice):
                    self.matrix[indice][self.clock]="ZZ"
                    self.hazards.append("Hazard AC/MQ")
                    return 0
        elif(etapa==2):
            for i in range(limite):
                if(etapas[i]==2 and i!=indice):
                    self.matrix[self.indice][self.clock]="ZZ"
                    self.hazards.append("Hazard AC/MQ")
                    return 0
 
        return 1