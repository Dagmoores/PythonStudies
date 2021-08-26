# Retirado do livro Introdução à Computação em Python - Um Foco no Desenolvimento de Aplicações - PERKOVIC, Ljubomir

# Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista. Você pode considerar que a lista não estará vazia. A função não deverá retornar nada. >>> ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs'] >>> trocaPU(ingredientes) >>> ingredientes ['maçãs', 'açúcar', 'manteiga', 'farinha']

ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs'] 

def trocaPU(input_list):
  input_list[0] = 'abacaxi'
  input_list[-1] = 'mexirica'

  print(input_list)
