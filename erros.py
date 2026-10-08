'''
1. Erro de Sintaxe (SyntaxError)
Ocorre quando o código não segue as regras de sintaxe do Python, 
como esquecer dois pontos após uma declaração de função ou um loop[cite: 5].
'''
# Exemplo de código com erro (faltam os dois pontos após os parênteses da função):
# def minha_funcao()
#     print("olá")


'''
2. Erro de Nome (NameError)
Ocorre quando se faz referência a uma variável ou função que não foi definida[cite: 5].
'''
# Exemplo de código com erro (a variável 'variavel_nao_definida' nunca foi criada):
# print(variavel_nao_definida)


'''
3. Erro de Tipo (TypeError)
Ocorre quando se realiza uma operação com tipos de dados incompatíveis, 
como tentar somar um número e uma string[cite: 5].
'''
# Exemplo de código com erro (tentativa de somar um inteiro com uma string):
# resultado = 5 + "10"


'''
4. Erro de Índice (IndexError)
Ocorre quando se tenta acessar um índice fora do intervalo válido de uma lista ou sequência[cite: 5].
'''
# Exemplo de código com erro (a lista tem índices 0, 1 e 2; o índice 3 não existe):
# lista = [1, 2, 3]
# print(lista[3])