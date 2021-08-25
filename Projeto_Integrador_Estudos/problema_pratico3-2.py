#Retirado do livro Introdução à Computação em Python - Um Foco no Desenolvimento de Aplicações - PERKOVIC, Ljubomir

#Traduza estas instruções condicionais em instruções if do Python:

#(a)Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'. 
#(b)Se o nome está na lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], exiba 'Um dos 5 maiores jogadores de beisebol de todos os tempos!'. 
#(c)Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.
#(d)Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.

#Resolução (a):

idade = eval(input('Qual é sua idade? '))
if idade > 62:
  print('Você pode obter benefícios de pensão')

#Resolução (b)

nome = input('Qual é o nome? ')
lista_nomes = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']

if nome in lista_nomes:
  print('Um dos 5 maiores jogadores de beisebol de todos os tempos!')

#Resolução (c)

golpes = eval(input('Quantos golpes? '))
defesas = eval(input('Quantas defesas? '))

if golpes > 10 and defesas == 0:
  print('Você está morto…')

#Resolução (d)

norte = eval(input('norte: '))
sul = eval(input('sul: '))
leste = eval(input('leste: '))
oeste = eval(input('oeste: '))

if norte == True  or sul == True or leste == True or oeste == True:
  print('Posso escapar.')
