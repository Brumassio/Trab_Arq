# salve professor Felippe Fernandes  da Silva ! <3
# é us guri do python

#simulador do ciclo de instrução do computador.
# 1) Entrada de dados
# 2) ULA
    # 2.1) AC, MQ
# 3) UC
    # 3.1) MBR, MAR, IBR, IR, PC

# 4 bits para o opcode e 8 bits de referência dos operandos.
# ULA deve-se tratar overflow,
# valores negativos e positivos e realizar os cálculos necessários, além de
# outros registradores.

# Como implementar memória
# Como declarar var em Bits
# opcode e operando

# quer que limita as variaveis? 
# quer que implemente as operações?  Sim
# implementar memoria? Sim

from instrucao import Instrucao
from uc import Uc
import numpy as np


#0100 Soma
#0101 Subtração
#0010 Divisão
#0001 Multiplicação
lista = []
memory=np.array(range(255))


# uc= Uc()
# memory[1]=Instrucao("0101", "10101010")

# uc.adicionarEnderecoPc("00000001")

# memory[2]=Instrucao("0100", "10100000")

# uc.adicionarEnderecoPc("00000010")





# uc.printarTudo()

# while uc.count <=len(uc.pc)-1:
#     uc.setMar()
#     # uc.buscaMemoria()
#     # uc.realizarOperacao()

#     uc.incrementarPc()



        

    
# print(uc.count)
# for i in range(uc.count):
#     if uc.count <= len(uc.pc):
#         uc.setMar()
#         print(uc.mar)
#         uc.incrementarPc()
    
    
    



n1="0110"
n2="1101"
resultado=""
carryin=0

for i in range(len(n1)):
    if n1[i]==1 and n2[i]==1:
        if carryin ==1:
            resultado+='1'
        else:
            resultado += '0'
        carryin = 1
    elif n1[i] == 0 and n2[i]==0:
        if carryin ==1:
            resultado+='1'
        else:
            resultado += '0'
        carryin = 0
    elif n1[i] != n2[i]:
        if carryin == 1:
            resultado +='0'
        else:
            resultado += '1'
        carryin =0           

print(resultado)