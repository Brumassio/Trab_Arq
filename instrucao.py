class Instrucao:
    def __init__(self, opcode, operando):
        self.opcode=opcode
        self.operando=operando 
    def getOpcode(self):
        return self.opcode
    def getoperando(self):
        return self.operando