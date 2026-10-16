# =====================================================================
# CONVERSÃO POR DIVISÃO EM PYTHON
# =====================================================================

# Atribuímos um valor inteiro à variável 'preco'
preco = 10
print(preco)  
# Saída: 10 (Tipo inteiro / int)


# 1. DIVISÃO COMUM ( / ):
# O operador de divisão simples ( / ) em Python sempre converte o resultado 
# implicitamente para o tipo ponto flutuante (float), mesmo que a divisão 
# seja exata.
print(preco / 2)  
# Saída: 5.0 (O tipo mudou automaticamente de int para float)


# 2. DIVISÃO INTEIRA ( // ):
# O operador de divisão inteira ( // ) descarta a parte fracionária do 
# resultado e preserva o tipo inteiro (int), caso ambos os operandos sejam 
# inteiros.
print(preco // 2)  
# Saída: 5 (O tipo continua sendo int)

# =====================================================================
# CONVERSÃO DE TIPO: Numérico para string
# =====================================================================

preco = 10.50
idade = 28

# Convertendo um número de ponto flutuante (float) para string
print(str(preco))  
# Saída: 10.5[cite: 5]


# Convertendo um número inteiro (int) para string
print(str(idade))  
# Saída: 28[cite: 5]


# Utilizando as variáveis dentro de uma f-string (interpolação)
# O Python converte implicitamente os valores para string ao exibi-los na f-string
texto = f"idade {idade} preco {preco}"
print(texto)  
# Saída: idade 28 preco 10.5

# =====================================================================
# CONVERSÃO DE TIPO: String para número
# =====================================================================

# As variáveis são declaradas originalmente como textos (strings)
preco = "10.50"
idade = "28"

# Converte a string "10.50" para um número decimal (float)
print(float(preco))  
# Saída: 10.5


# Converte a string "28" para um número inteiro (int)
print(int(idade))  
# Saída: 28

'''
### 💡 Explicação em Comentários:
* **`float("10.50")`**: Converte a sequência de caracteres em um valor numérico de ponto flutuante. É necessário para poder realizar operações matemáticas (como somas ou multiplicações) com o valor[cite: 6].
* **`int("28")`**: Converte o texto numérico num valor inteiro puro
* **Atenção**: Se a *string* contiver caracteres não numéricos (por exemplo `"10.50a"` ou `"vinte"`), o Python lançará um erro do tipo `ValueError`.

Precisas de mais algum exemplo ou esclarecimento sobre este tópico?
'''

preco = "python"
print(float(preco))

'''
### Saída / Erro no Terminal:

Traceback (most recent call last):
  File "main.py", line 3, in <module>
    print(float(preco))
ValueError: could not convert string to float: 'python'


### Explicação:
* **Atribuição**: A variável `preco` é inicializada com o valor de texto `"python"`[cite: 7].
* **Lançamento da Exceção**: Ao executar a função `float(preco)`, o interpretador Python tenta transformar esse texto num número decimal, mas depara-se com caracteres alfabéticos[cite: 7].
* **`ValueError`**: Como resultado, o Python interrompe a execução e gera um erro do tipo `ValueError`, informando que não foi possível realizar a conversão da *string* para `float`[cite: 7].

'''