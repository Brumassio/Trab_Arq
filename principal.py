# salve professor Felippe Fernandes  da Silva ! <3

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
# quer que implemente as operações?
# implementar memoria?

from instrucao import Instrucao
from uc import Uc


uc= Uc()
uc.adicionarInstrucao(Instrucao("0101", "10101010"))
uc.adicionarInstrucao(Instrucao("0100", "10100000"))
uc.setPcAtual()
uc.setMar()
print(uc.mar)
uc.incrementarPc()
uc.setMar()
print(uc.mar)





