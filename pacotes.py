'''
CRIAR E UTILIZAR PACOTES EM PYTHON
Para criar um pacote, criamos um diretório com o nome desejado e adicionamos um 
arquivo especial chamado __init__.py dentro do diretório[cite: 11]. Este arquivo pode 
estar vazio ou conter código de inicialização do pacote[cite: 11].

Por exemplo, criamos um diretório chamado 'meu_pacote' com a seguinte estrutura[cite: 11]:
    meu_pacote/
        __init__.py
        modulo1.py
        modulo2.py
'''

# Depois, podemos importar e utilizar os módulos do pacote em nosso programa[cite: 11]:
from meu_pacote import modulo1, modulo2

# Utilizando as funções definidas em cada módulo do pacote[cite: 11]
modulo1.funcao1()
modulo2.funcao2()

'''
Neste exemplo, são importados os módulos modulo1 e modulo2 do pacote 
meu_pacote e são utilizadas as funções definidas neles[cite: 11].
'''