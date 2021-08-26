# Retirado do livro Introdução à Computação em Python - Um Foco no Desenolvimento de Aplicações - PERKOVIC, Ljubomir

# Implemente a função perímetro(), que aceita, como entrada, o raio de um círculo (um número não negativo) e retorna o perímetro do círculo. Você deverá escrever sua implementação em um módulo chamado perímetro.py. Um exemplo de uso é: >>> perimeter(1) 6.283185307179586

import math

def f(r):
  if r < 0:
    print('O raio precisa ser positivo.')
  else:
    return 2 * math.pi * r
