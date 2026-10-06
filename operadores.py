a = 10
b = 3


soma = a + b   # 13
subtracao = a - b    # 7
multiplicacao = a * b    # 30
divisao = a / b   # 3.333333333
divisao_inteira = a // b   # 3
modulo = a % b   # 1
exponenciacao = a ** b   # 1000

"""
Igual a (==): devolve True se ambos os valores são iguais.
Diferente de (!=): devolve True se os valores são diferentes.
Maior que (>): devolve True se o primeiro valor é maior que o segundo.
Menor que (<): devolve True se o primeiro valor é menor que o segundo.
Maior ou igual que (>=): devolve True se o primeiro valor é maior ou igual que o segundo.
Menor ou igual que (<=): devolve True se o primeiro valor é menor ou igual que o segundo.

"""

a = 10
b = 3


igual = a == b   # False
diferente = a != b   # True
maior que = a > b   # True
menor que = a < b   # False
maior ou igual = a >= b   # True
menor ou igual = a <= b   # False

#lógicos
a = 10
b = 3


resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False

"""
if condicao:

   # Bloco de código a executar se a condição for verdadeira
   instruções
"""
idade = 18


if idade >= 18:
   print ("Você é maior de idade.")

   idade = 15


if idade >= 18:
   print ("Você é maior de idade.")

else:
   print ("Você é menor de idade.")