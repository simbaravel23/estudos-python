# =====================================================================
# FUNÇÕES DE ENTRADA E SAÍDA EM PYTHON
# =====================================================================

# A função input() é utilizada para ler uma entrada de dados enviada pelo utilizador através do terminal.
# O texto passado como argumento ("Informe o seu nome: ") é exibido como uma mensagem no ecrã.
# O valor introduzido pelo utilizador é guardado na variável 'nome' como texto (string).
nome = input("Informe o seu nome: ")

# A função print() exibe o conteúdo da variável no terminal.
print(nome)




### 🖥️ Exemplo de Execução no Terminal:

'''
Informe o seu nome: Guilherme
Guilherme


* **`input("Informe o seu nome: ")`**: Pausa a execução do programa e aguarda que o utilizador escreva algo e pressione a tecla *Enter*[cite: 8].
* **`print(nome)`**: Recebe a variável `nome` e imprime o seu valor logo de seguida[cite: 8].
'''

# =====================================================================
# FUNÇÕES DE ENTRADA E SAÍDA COM ARGUMENTOS DO PRINT
# =====================================================================

# Lê o nome introduzido pelo utilizador através do terminal
nome = input("Informe o seu nome: ")[cite: 9]

# Lê a idade introduzida pelo utilizador através do terminal
idade = input("Informe a sua idade: ")[cite: 9]

# Imprime os valores das variáveis 'nome' e 'idade' separados por um espaço (comportamento padrão)
print(nome, idade)[cite: 9]

# O argumento 'end=" "' altera o final do print: em vez de mudar de linha, 
# termina com um espaço em branco, permitindo que a próxima impressão continue na mesma linha.
print("teste", end=" ")[cite: 9]

# Imprime as variáveis e define um final personalizado com reticências e quebra de linha (\n)
print(nome, idade, end=" ... \n")[cite: 9]




### 🖥️ Explicação da Execução no Terminal:
* **`input(...)`**: Solicita interativamente os dados ao utilizador, que inseriu `guilherme` para o nome e `28` para a idade
* **`print(nome, idade)`**: Mostra `guilherme 28` na primeira linha de saída
* **`print("teste", end=" ")`**: Mostra `teste` e mantém o cursor na mesma linha graças ao parâmetro `end`
* **`print(nome, idade, end=" ... \n")`**: Continua na mesma linha imprimindo `guilherme 28`, seguido de ` ... ` e terminando com uma mudança de linha