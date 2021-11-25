from src.module import Module

class EmptyModule(Module):
    def __init__(self, args):
        Module.__init__(self, args)

    def exec(self):
        pass
