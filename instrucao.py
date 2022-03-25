class Instrucao:
    def __init__(self, opcode, instrucao):
        self.opcode=opcode
        self.instrucao=instrucao 
    def getOpcode(self):
        return self.opcode
    def getInstrucao(self):
        return self.instrucao   