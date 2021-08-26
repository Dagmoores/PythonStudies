# Retirado do livro Introdução à Computação em Python - Um Foco no Desenolvimento de Aplicações - PERKOVIC, Ljubomir

# Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por linha, os valores negativos na lista. A função não deverá retornar nada. >>> negatives([4, 0, -1, -3, 6, -9]) -1 -3 -9

def negativos(input_list):

  if type(input_list) == type(list()):
    for i in input_list:
      if i < 0:
        print(i)

  else:
    print('Você deve digitar um tipo list')

negativos([10, -4, -2, -1])
