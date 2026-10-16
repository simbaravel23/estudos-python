print(10 - 5 * 2)  # 0
print((10 - 5) * 2)  # 10

print(10 ** 2 * 2)  # 200

print(10 ** (2 * 2))  # 10000

print(10 / 2 * 4)  # 20.0

produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)                                                                                            
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)

# 1. Misturando multiplicação, divisão e adição 
# (como * e / têm a mesma prioridade, são resolvidos da esquerda para a direita)
print(10 + 2 * 5 - 4 / 2)
# Saída esperada: 18.0
# Explicação: 2 * 5 = 10 | 4 / 2 = 2.0 | Logo: 10 + 10 - 2.0 = 18.0

# 2. Uso do operador módulo (%) junto com multiplicação
print(10 + 3 * 2 % 4)
# Saída esperada: 12
# Explicação: 3 * 2 = 6 | 6 % 4 = 2 (resto da divisão) | Logo: 10 + 2 = 12

# 3. Misturando parênteses, exponenciação e divisão inteira
print((2 + 3) ** 2 * (10 // 3))
# Saída esperada: 75
# Explicação: (2 + 3) = 5 | (10 // 3) = 3 | 5 ** 2 = 25 | Logo: 25 * 3 = 75

# 4. Avaliação da esquerda para a direita com divisão normal e multiplicação
print(9 / 2 * 2)
# Saída esperada: 9.0
# Explicação: 9 / 2 = 4.5 | 4.5 * 2 = 9.0