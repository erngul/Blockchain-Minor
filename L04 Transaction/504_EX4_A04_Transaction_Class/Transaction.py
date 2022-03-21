from Signature import *

class Tx:
    inputs = None
    outputs =None
    sigs = None

    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.sigs = []

    def add_input(self, from_addr, amount):
        self.inputs.append((amount, from_addr))
        pass

    def add_output(self, to_addr, amount):
        self.outputs.append((amount, to_addr))
        pass

    def sign(self, private):
        self.sigs.append(sign(self.concactList(), private))

    def concactList(self):
        result = [*self.inputs, *self.outputs]
        return result