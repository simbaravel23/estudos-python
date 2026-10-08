def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media


print("Media:", calcular_media(10, 20, 30, 40))


def somar_3(x):
    return x + 3


soma = lambda x: x + 3

print("Somar 3 a um numero:", soma(5))

'''
Documentação de funções (docstrings)
É uma boa prática documentar nossas funções utilizando docstrings. Os docstrings são cadeias de texto que descrevem o propósito, os parâmetros e o valor de retorno de uma função. São colocados imediatamente após a definição da função e são encerrados entre aspas duplas triplas.
'''

def area_retangulo(base, altura):

    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """

    return base * altura


print("Área do retângulo:", area_retangulo(5, 3))

'''
Funções com número variável de argumentos
Python permite definir funções que aceitem um número variável de argumentos. Isso é feito utilizando o operador * antes do nome do parâmetro.
'''
def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(1, 2, 3))  # Imprime 6
print(soma_variavel(4, 5, 6, 7))  # Imprime 22