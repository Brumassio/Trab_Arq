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
        print("VALOR MAIS A ESQUERDA=",num1[0])
        while aux != 0:
            string_list1.insert(0,num1[0])
            aux -= 1
        print(string_list1, " ",string_list2)
    return string_list1,string_list2






    
            
        
