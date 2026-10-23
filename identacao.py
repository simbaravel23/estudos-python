# Bloco principal (0 espaços de indentação): Definição da função sacar
def sacar(valor):
    # Nível 1 de indentação (4 espaços): Pertence ao escopo interno da função sacar
    saldo = 500

    # Nível 1 de indentação (4 espaços): Estrutura condicional 'if' dentro da função
    if saldo >= valor:
        # Nível 2 de indentação (8 espaços): Código executado apenas se o 'if' for verdadeiro
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    # Nível 1 de indentação (4 espaços): Fora do 'if', mas ainda dentro da função 'sacar'
    print("Obrigado por ser nosso cliente, tenha um bom dia!")


# Bloco principal (0 espaços de indentação): Definição da função depositar
def depositar(valor):
    # Nível 1 de indentação (4 espaços): Pertence ao escopo interno da função depositar
    saldo = 500
    saldo += valor


# Bloco principal (0 espaços de indentação): Chamada da função para execução
sacar(1000)