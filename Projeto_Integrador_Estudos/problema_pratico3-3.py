#Retirado do livro Introdução à Computação em Python - Um Foco no Desenolvimento de Aplicações - PERKOVIC, Ljubomir

#Traduza estas declarações em instruções if/else do Python: 
#(a)Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário, exiba 'Definitivamente não é um ano bissexto.' 
#(b)Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba 'Melhor sorte da próxima vez…'.

#Resolução (a)
ano = eval(input('Em que ano estamos? '))

if ano % 4 ==0:
  print('Pode ser um ano bissexto.')
else:
  print('Definitivamente não é um ano bissexto.')

#Resolução (b)

bilhete = eval(input('Quais os números do seu bilhete? '))

loteria = [10, 23, 54, 56]

if bilhete == loteria:
  print('Você ganhou!')
else: print('Melhor sorte da próxima vez…')
