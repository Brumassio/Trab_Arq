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
            print(string_list[aux])
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
    print(resultado[::-1]) 


def multiplicacao(num1,num2):
    linha = []
    aux=""
    for i in range(len(num2)):
        for j in range(len(num1)):
            aux += str((int(num1[-(j+1)]))*(int(num2[-(i+1)])))
        linha.append(aux)

    aux2 = 1
    sominha = linha[0]
    while aux2 <len(linha):
        sominha = soma(linha[aux2],linha[aux2-1])
        aux2 += 1
    print(sominha)
    


# 0110/100


# def divisao(num, den):
#    resultado=0
#    
#    resto=bin(num[:len(den)])-bin(den) 
#   
#    while (resto<=0)    
#       resultado+="1"
    
            
        
