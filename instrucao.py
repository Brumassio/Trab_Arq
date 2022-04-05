class Instrucao:
    def __init__(self, opcode, endereco):
        self.opcode=opcode
        self.endereco=endereco 
    def getOpcode(self):
        return self.opcode
    def getEndereco(self):
        return self.endereco