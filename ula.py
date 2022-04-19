from operator import concat
from tools import ajudaATransformar, transformarNegativo, complementoDois, igualaCasas


def soma(n1,n2):
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



def multiplicacao(num1,num2):
    
    linha=[]
    # string_list1 = list(num1)
    # string_list2 = list(num2)
    
    string_list1, string_list2 = igualaCasas(num1,num2)
    print(string_list1,"string 2: ", string_list2)
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

    print(linha)

    aux2 = 0
    mult = ""
    while aux2 < len(linha)-1:
        linha[aux2+1] = soma(linha[aux2],linha[aux2+1]) 
        aux2 += 1
    mult =linha[aux2-1]
    print(mult)

    # print(len(linha))
    # aux2 = 1
    # sominha = linha[0]
    # while aux2 <len(linha):
    #     sominha += soma(linha[-(aux2)],linha[-(aux2-1)])
    #     aux2 += 1

    # print(sominha)
    
def divisao(num, den):
   resultado=""
   aux=transformarNegativo(complementoDois(den))
   used=len(den)
   resto=num[:used]
   while ((len(num)-(used))>=0):
         if(len(resto)==len(den)):
            resto=soma(complementoDois(resto), aux)
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
         





    
            
        
