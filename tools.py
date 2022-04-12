from operator import concat


def ajudaATransformar(num):
    for i in range(len(num)):
        if int(num[-(i+1)])==1:
            # print("retornando:",i+1)
            return i+1
            
    return -1

def transformarNegativo(num):

    string_list = list(num)
    aux=(len(num)-ajudaATransformar(num))-1
    if aux!=-1:
        while aux>=0:
            string_list[aux]=str(int(not(int(num[aux]))))
            aux-=1
    num= "".join(string_list)
    #print(num)
    return num   

def complementoDois(num):
    aux="0"+num
    return aux

def soma(n1,n2):
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

def igualaCasas(num1,num2):
    string_list1 = list(num1)
    string_list2 = list(num2)
    if len(string_list1) > len(string_list2):
        aux = len(string_list1) - len(string_list2)
        while aux != 0:
            string_list2.insert(0,num2[0])
            aux -= 1        
        print(string_list1," ",string_list2)
    else:
        aux = len(string_list2) - len(string_list1)
        while aux != 0:
            string_list1.insert(0,num1[0])
            aux -= 1
        print(string_list1, " ",string_list2)


def multiplicacao(num1,num2):
    
    linha=[]
    igualaCasas(num1,num2)
    string_list1 = list(num1)
    string_list2 = list(num2)
    aux=""
    for i in range(len(string_list1)):
        for j in range(len(string_list2)):
            if string_list1[i] == "0":
                aux += "0"
            elif string_list1[i] == "1" and string_list2[j] == "0":
                aux += "0"
            elif string_list1[i] == "1" and string_list2[j] == "1":
                aux += "1"     

        for k in range(i):
            aux+="0"    # aux += str((int(num1[(j)]))*(int(num2[-(i)])))
        linha.append(aux)
        aux =""
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
         

   print(resultado)




    
            
        
