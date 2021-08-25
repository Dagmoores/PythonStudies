#Implemente um programa que solicita a temperatura atual em graus Fahrenheit do usuário e exibe a temperatura em graus Celsius usando a fórmula

#Seu programa deverá ser executado da seguinte forma: >>> Digite a temperatura em graus Fahrenheit: 50 A temperatura em graus Celsius é 10.0

#Celsius = 5/9(fahrenheit - 32)

fahrenheit_input = input('Qual é a temperatura em Fahrenheit? ')

fahrenheit_input = eval(fahrenheit_input)



celsius = 5/9(fahrenheit_input -32)
print('A temperatura em Celsius é ', celsius)
