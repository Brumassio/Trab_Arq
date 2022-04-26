from operator import concat
import os
from tools import ajudaATransformar, transformarNegativo, complementoDois, igualaCasas, verificaSinalMagnita, complementoDois2
class ula:
    def __init__(self):
        self.ac=""
        self.mq=""
        
    def writeMQ(self,value):
        self.mq=value

    def writeAC(self,value):
        self.ac=value

    def readAC(self):
        return self.ac
    
    def readMQ(self):
        return self.mq

    def soma(self,n1,n2):
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

    def subtracao(self,n1,n2): 
        n2 = "1"+transformarNegativo(n2[2:])
        n1,n2=igualaCasas(n1,n2)
        subtr = self.soma(n1,n2)
        print("resultado subtracao=",subtr)
        return subtr[len(subtr)-len(n1):]



    def multiplicacao(self,num1,num2):
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
                linha[aux2+1] = self.soma(linha[aux2],linha[aux2+1]) 
                aux2 += 1
                if aux2+1 == len(linha)-1:
                    transformarNegativo(linha[aux2+1])
            
        else:
            while aux2 < len(linha)-1:
                linha[aux2+1] = self.soma(linha[aux2],linha[aux2+1]) 
                aux2 += 1
        mult =linha[aux2-1]
        print(f"resultado multiplicacao = {mult}") 
        return mult

    def divisao(self, num, den):
        resultado=""
        den=den[den.find("1"):]
        num=num[num.find("1"):]
        # aux=transformarNegativo(complementoDois(den))

        used=len(den)
        resto=num[:used]
        while ((len(num)-(used))>0):
                
                if((len(resto)==len(den) or (len(resto)>len(den)) and int(resto,2)>=int(den,2)) ):

                    resto=self.subtracao(complementoDois(resto), complementoDois(den))
                    

                    if(int(resto[1:],2)!=0):
                        resto=resto[(resto[1:].find("1")+1):]

                        resultado+="1"
                    else:
                        resto=""
                        resultado+="1"
                else:
                    if(used!=len(num)):
                        resto+=num[used]

                    if(len(resto)<len(den)):
                        resultado+="0"  
                    elif(len(resto)==len(den) and int(resto,2)<int(den,2)):
                        resultado+="0"
                    used+=1
        print(f"RESULTADO DIVISAO={resultado}")
        return resultado
            





    
            
        
