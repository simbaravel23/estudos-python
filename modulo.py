'''
=============================================================================
TEMA 1: CRIAÇÃO E IMPORTAÇÃO DE MÓDULOS PRÓPRIOS
=============================================================================
Para criar um módulo personalizado, criamos um novo arquivo Python com o nome 
desejado e definimos as funções, classes e variáveis que queremos incluir nele[cite: 10].
Por exemplo, podemos criar o arquivo 'meu_modulo.py' com o seguinte conteúdo[cite: 10]:

    # --- Conteúdo do arquivo meu_modulo.py ---
    def saudar(nome):
        print(f"Olá, {nome}!")

    def calcular_soma(a, b):
        return a + b

Depois, podemos importar e utilizar essas funções em nosso programa principal[cite: 10].
'''

import meu_modulo

# Utilizando funções do módulo personalizado
meu_modulo.saudar("João")  # Imprime "Olá, João!"[cite: 10]
resultado_ex1 = meu_modulo.calcular_soma(5, 3)
print(resultado_ex1)  # Imprime 8[cite: 10]


'''
=============================================================================
TEMA 2: ORGANIZAÇÃO DO CÓDIGO EM MÓDULOS SEGUNDO A FUNCIONALIDADE
=============================================================================
À medida que nossos programas crescem em tamanho e complexidade, é uma boa prática 
organizar nosso código em módulos separados segundo sua funcionalidade. Isso nos 
permite manter um código mais legível, agrupado em módulos e fácil de manter.

Por exemplo, podemos ter:
1. Um módulo 'operacoes.py' com funções matemáticas:
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

2. Um módulo 'utilidades.py' com funções de uso geral:
    def imprimir_mensagem(mensagem):
        print(mensagem)

    def obter_nome_usuario():
        return input("Digite seu nome: ")

Abaixo simulamos o uso desses módulos integrados em um programa principal:
'''

# Simulando importações de múltiplos arquivos organizados por funcionalidade:
# import operacoes
# import utilidades

# Exemplo prático de fluxo integrado:
# resultado_op = operacoes.somar(10, 5)
# utilidades.imprimir_mensagem(f"O resultado da operação é: {resultado_op}")

'''
VANTAGEM FINAL:
Ao organizar nosso código em módulos, podemos reutilizar funções facilmente e 
manter a estrutura limpa, modularizada e altamente manutenível.
'''