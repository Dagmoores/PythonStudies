#Retirado do livro Introdução à Computação em Python - Um Foco no Desenolvimento de Aplicações - PERKOVIC, Ljubomir

#Implemente um programa que solicite do usuário uma lista de palavras (ou seja, strings) e depois exiba na tela, uma por linha, todas as strings de quatro letras nessa lista. >>> Digite a lista de palavras: ['pare', 'desktop', 'tio', 'pote']                   pare pote

lista_palavras = eval(input('Digite uma lista de palavras \n'))

for i in lista_palavras:
  if len(lista_palavras[i]) == 4
    print(lista_palavras[i])
