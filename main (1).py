#Criar as variáveis
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
op = input(
    "a para SOMA; b para SUBTRAÇÃO; c para MULTIPLICAÇÃO; d para DIVISÃO: ")
d = print('CTRL+Enter para atualizar o programa')

#Criar as condições
if op == 'a':
  print(' a resposta é: ', a + b)
if op == 'b':
  print(' a resposta é: ', a - b)
if op == 'c':
  print(' a resposta é: ', a * b)
if op == 'd':
  print(' a resposta é: ', float(a / b))  #converter para float

#Atividade: Mudar o tipo de número dos resultados para número decimal.
