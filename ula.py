from operator import concat
import os
from tools import ajudaATransformar, transformarNegativo, complementoDois, igualaCasas, verificaSinalMagnita, complementoDois2
class ula:
    def __init__(self):
        self.ac=""
        self.mq=""
        

    def soma(self,n1):
        n2=self.ac
        n1,n2=igualaCasas(n1,n2)
        carryin = 0
        resultado = ""
        aux2 = 0
        for i in range(len(n1)):
            aux2 = int(n1[-(i+1)]) ^ int(n2[-(i+1)]) ^ carryin
            resultado += str(int(aux2))
            if ((int(n1[-(i+1)]) + int(n2[-(i+1)]))==2) or ((int(n1[-(i+1)]) ^ int(n2[-(i+1)]))==1 and carryin==1):
                carryin=1
            else:
                carryin=0
        resultado += str(carryin) 
        self.ac=resultado[::-1]
        return resultado[::-1]

    def soma2(self,n1,n2):
        n1,n2=igualaCasas(n1,n2)
        carryin = 0
        resultado = ""
        aux2 = 0
        for i in range(len(n1)):
            aux2 = int(n1[-(i+1)]) ^ int(n2[-(i+1)]) ^ carryin
            resultado += str(int(aux2))
            if ((int(n1[-(i+1)]) + int(n2[-(i+1)]))==2) or ((int(n1[-(i+1)]) ^ int(n2[-(i+1)]))==1 and carryin==1):
                carryin=1
            else:
                carryin=0
        resultado += str(carryin) 
        self.ac=resultado[::-1]
        return resultado[::-1]

    def soma3(self,n1,n2):
            n1,n2=igualaCasas(n1,n2)
            carryin = 0
            resultado = ""
            aux2 = 0
            for i in range(len(n1)):
                aux2 = int(n1[-(i+1)]) ^ int(n2[-(i+1)]) ^ carryin
                resultado += str(int(aux2))
                if ((int(n1[-(i+1)]) + int(n2[-(i+1)]))==2) or ((int(n1[-(i+1)]) ^ int(n2[-(i+1)]))==1 and carryin==1):
                    carryin=1
                else:
                    carryin=0
            resultado += str(carryin) 
            return resultado[::-1]

    def subtracao2(self,n1,n2): 
        
        print(f"ME NOTA PEDRAUM SENPAI ! -> n1:{n1}, n2:{n2}")
        if verificaSinalMagnita(n1,n2) == 2:
            n2 = transformarNegativo(n2)
            n1,n2=igualaCasas(n1,n2)
            subtr = self.soma2(n1,n2)
            return subtr[2:]
        elif verificaSinalMagnita(n1,n2) == 0:
            n2 = transformarNegativo(n2)
            n1,n2=igualaCasas(n1,n2)
            subtr = self.soma2(n1,n2)
            return subtr[2:]
        elif verificaSinalMagnita(n1,n2) == 1:
            
            n2 = transformarNegativo(n2)
            n1,n2=igualaCasas(n1,n2)
            print("n2=",n2)
            subtr = self.soma2(n1,n2)
            print("resultado=",subtr)
            return subtr[2:]
        elif verificaSinalMagnita(n1,n2) == 3:
            print("estou no if == 0")
            n2 = transformarNegativo(n2)

            n1,n2=igualaCasas(n1,n2)
            print("n2=",n2)
            subtr = self.soma2(n1,n2)
            print("resultado=",subtr)
            return subtr[2:]

    def subtracao(self,n1):
        n1,self.ac = igualaCasas(n1,self.ac)
        if verificaSinalMagnita(n1,self.ac) == 2:
            print("estou no if == 2")
            self.ac = transformarNegativo(self.ac)
            subtr = self.soma2(n1,self.ac)
            self.ac = subtr
            return subtr
        elif verificaSinalMagnita(n1,self.ac) == 0:
            print("estou no if == 0")
            self.ac = transformarNegativo(self.ac)
            subtr = self.soma2(n1,self.ac)
            self.ac = subtr
            return subtr
        elif verificaSinalMagnita(n1,self.ac) == 1:
            print("estou no if == 1")
            self.ac = transformarNegativo(self.ac)
            subtr = self.soma2(n1,self.ac)
            self.ac = subtr
            return subtr
        elif verificaSinalMagnita(n1,self.ac) == 3:
            print("estou no if == 3")
            self.ac = transformarNegativo(self.ac)
            subtr = self.soma2(n1,self.ac)
            self.ac = subtr
            return subtr

    def multiplicacao2(self,num1,num2):
        linha=[]
        string_list1, string_list2 = igualaCasas(num1,num2)
        for i in range(len(string_list1)):
            aux = []
            for j in range(len(string_list2)):
                if string_list1[-(i+1)] == "0":
                    aux.insert(0,"0");
                elif string_list1[-(i+1)] == "1" and string_list2[-(j+1)] == "0":
                    aux.insert(0,"0")
                elif string_list1[-(i+1)] == "1" and string_list2[-(j+1)] == "1":
                    aux.insert(0,"1");   
                
            for k in range(i):
                aux.append("0");  
            linha.append(aux)


        for i in linha:

            i=igualaCasas(i,linha[-1])
        aux2 = 0
        mult = ""
        if verificaSinalMagnita(num1,num2) == 2:
            while aux2 < len(linha)-1:

                linha[aux2+1] = self.soma3(linha[aux2],linha[aux2+1]) 
                aux2 += 1
                if aux2+1 == len(linha)-1:
                    transformarNegativo(linha[aux2+1])
            mult =linha[aux2-1]
            print(mult)
            
        else:
            while aux2 < len(linha)-1:
                linha[aux2+1] = self.soma3(linha[aux2],linha[aux2+1]) 
                aux2 += 1
            mult =linha[aux2-1]
            print(mult) 

        self.mq=mult         
        return mult
    def multiplicacao(self,num1):
        
        linha=[]
        string_list1, string_list2 = igualaCasas(num1,self.mq)
        for i in range(len(string_list1)):
            aux = []
            for j in range(len(string_list2)):
                if string_list1[-(i+1)] == "0":
                    aux.insert(0,"0");
                elif string_list1[-(i+1)] == "1" and string_list2[-(j+1)] == "0":
                    aux.insert(0,"0")
                elif string_list1[-(i+1)] == "1" and string_list2[-(j+1)] == "1":
                    aux.insert(0,"1");   
                
            for k in range(i):
                aux.append("0");  
            linha.append(aux)


        for i in linha:
            i=igualaCasas(i,linha[-1])

        aux2 = 0
        mult = ""
        if verificaSinalMagnita(num1,self.mq) == 2:
            while aux2 < len(linha)-1:
                linha[aux2+1] = self.soma3(linha[aux2],linha[aux2+1]) 
                aux2 += 1
                if aux2+1 == len(linha)-1:
                    transformarNegativo(linha[aux2+1])
            mult =linha[aux2-1]
            print(mult)
        else:
            while aux2 < len(linha)-1:
                linha[aux2+1] = self.soma3(linha[aux2],linha[aux2+1]) 
                aux2 += 1
            mult =linha[aux2-1]
            print(mult)     

        self.mq = mult
        return mult

        
    def divisao2(self,num, den):
        resultado=""
        aux=transformarNegativo(complementoDois(den))
        used=len(den)
        resto=num[:used]
        while ((len(num)-(used))>=0):
                if(len(resto)==len(den)):
                    resto=self.soma3(complementoDois(resto), aux)
                    if(int(resto[1:],2)!=0):
                        resto=resto[(resto[1:].find("1")+1):]
                    else:
                        resto=""
                        resultado+="1"
                else:
                    if(used!=len(num)):
                        resto+=num[used]
                    if(len(resto)<len(den)):
                        resultado+="0"   
                    used+=1
        self.mq=resultado
        return resultado

    def divisao(self, den):
        resultado=""
        den=den[den.find("1"):]
        self.mq=self.mq[self.mq.find("1"):]

        # aux=transformarNegativo(complementoDois(den))
        print(f"MQ={self.mq} e DEN={den}")
        num=self.mq
        used=len(den)
        resto=num[:used]
        while ((len(num)-(used))>0):
                
                if(len(resto)==len(den) and int(resto,2)>=int(den,2)  or (len(resto)>len(den) and int(resto,2)>=int(den,2)) ):
                    print(f"Somando {complementoDois(resto)} com {complementoDois(den)}")
                    resto=self.subtracao2(complementoDois(resto), complementoDois(den))
                    

                    if(int(resto[1:],2)!=0):
                        resto=resto[(resto[1:].find("1")+1):]
                        print(f"RESTO={resto}")
                        resultado+="1"
                    else:
                        resto=""
                        resultado+="1"
                else:
                    if(used!=len(num)):
                        resto+=num[used]
                        print(f"RESTO={resto}")
                    if(len(resto)<len(den)):
                        resultado+="0"  
                    if(len(resto)==len(den) and int(resto,2)<int(den,2)):
                        resultado+="0"
                    used+=1
        print(f"RESULTADO={resultado}")
        self.mq=resultado
        return resultado
            





    
            
        
