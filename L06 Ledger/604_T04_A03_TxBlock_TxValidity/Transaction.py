from Signature import *
from cryptography.hazmat.primitives.serialization import *

class Tx:
    inputs = None
    outputs =None
    sigs = None
    reqd = None
    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.sigs = []

    def add_input(self, from_addr, amount):
        self.inputs.append((from_addr, amount))
        pass

    def add_output(self, to_addr, amount):
        self.outputs.append((to_addr, amount))
        pass

    def sign(self, private):
        self.sigs.append(sign(self.concactList(), private))


    def is_valid(self):
        amountInput = 0
        amountOutput = 0
        for i in self.inputs:
            amountInput += i[1]
        for o in self.outputs:
            amountOutput += o[1]
        if amountOutput < 0 or amountInput < 0:
            return False
        if amountInput < amountOutput:
            return False
        for s in self.sigs:
            if verify(self.concactList(), s, self.inputs[0][0]):
                if self.reqd is None:
                    return True
                for ss in self.sigs:
                    if verify(self.concactList(), ss, self.reqd):
                        return True
        return False


    def add_reqd(self, public):
        self.reqd = public


    def concactList(self):
        result = [*self.inputs, *self.outputs]
        return result