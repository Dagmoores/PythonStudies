# Retirado do livro Introdução à Computação em Python - Um Foco no Desenolvimento de Aplicações - PERKOVIC, Ljubomir

# Acrescente a docstring retorna a média de x e y à função média() e a docstring exibe os números negativos contidos na lista lst à função negativos() dos Problemas Práticos 3.8 e 3.10. Verifique seu trabalho usando a ferramenta de documentação help(). Você deverá receber, por exemplo: >>> help(média) Ajuda sobre a função média no módulo __main__: média(x, y) retorna a média de x e y

def media(x, y):
  'retorna a média de x e y'
  (x + y) / 2

def negativos(input_list):
  'exibe os números negativos contidos na lista'

  if type(input_list) == type(list()):
    for i in input_list:
      if i < 0:
        print(i)

  else:
    print('Você deve digitar um tipo list')
