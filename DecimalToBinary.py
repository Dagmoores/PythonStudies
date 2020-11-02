##This Program will help you yo transform decimal numbers into binary numbers

class Pilha():
    def __init__ (self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)
    def top(self):
        if len(self.data) > 0:
            return self.data [-1]

    def empty(self):
        return not len(self.data) > 0

##You have to choose a number for W to transform this number in to a binary.

w =

p= Pilha ()
num = w
while num > 0:
    resto = num % 2
    num = num // 2

    p.push(resto)

while not p.empty():
    print(p.pop())

