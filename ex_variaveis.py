# Atribuição de valores a variáveis (podem ser alterados)
nome = "Guilherme"
idade = 28

# Sobrescrevendo a variável 'nome' com um novo valor
nome = "Giovanna"

# Exibe os valores atuais das variáveis nome e idade
print(nome, idade)  # Saída no terminal: Giovanna 28

# Exemplo de variável com padrão de nomenclatura de constante (letras maiúsculas)
limite_saque_diario = 1000

# Exemplo de constante (por convenção em letras maiúsculas, embora o Python permita reatribuição)
BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"]

# Reatribuindo um novo valor (inteiro) para a "constante", demonstrando que o Python permite
BRAZILIAN_STATES = 10

# Exibe o valor atual da variável BRAZILIAN_STATES
print(BRAZILIAN_STATES)  # Saída no terminal: 10