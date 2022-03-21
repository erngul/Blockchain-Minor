from Signature import *
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
        self.inputs.append((amount, from_addr))
        pass

    def add_output(self, to_addr, amount):
        self.outputs.append((amount, to_addr))
        pass

    def sign(self, private):
        self.sigs.append(sign(self.concactList(), private))


    def is_valid(self):
        amount = 0
        for i in self.inputs:
            amount += i[0]
        for o in self.outputs:
            amount += o[0]
        if amount < 0:
            print('amount to low')
            return False
        for s in self.sigs:
            if verify(self.concactList(), s, self.outputs[0][1]) == True:
                if self.reqd is None:
                    return True
                for ss in self.sigs:
                    if verify(self.concactList(), ss, self.reqd) == True:
                        return True
        return False


    def add_reqd(self, public):
        self.reqd = public


    def concactList(self):
        result = [*self.inputs, *self.outputs]
        return result