# I'm using this file to learn about the creation and manipulation of queues in Python

class Fila():
    def __init__(self):
        self.data = []

    def inserir(self,x):
        self.data.append(x)

    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

    def empty(self):
        return not len(self.data) > 0

