saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    # ...
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")

# (Constante assumida num contexto anterior do código: MAIOR_IDADE = 18)
idade = int(input("Informe sua idade: "))

# Abordagem 1: Dois blocos 'if' independentes
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

# Abordagem 2: Estrutura condicional composta 'if / else'
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CNH.")    

idade = int(input("Informe sua idade: "))

# Abordagem 1: Múltiplos 'if' independentes
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

# Abordagem 2: Estrutura composta 'if / else'
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CNH.")

# Abordagem 3: Estrutura encadeada 'if / elif / else'
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

# ---------------------------------------------------------
# 1. ATRIBUIÇÃO DE VARIÁVEIS INICIAIS
# ---------------------------------------------------------
conta_normal = True        # Define que o tipo de conta é normal
conta_universitaria = False  # Define que não é conta universitária

saldo = 2000         # Saldo disponível na conta
saque = 500          # Valor que o utilizador pretende retirar[cite: 8]
cheque_especial = 450  # Limite adicional do cheque especial[cite: 8]

# ---------------------------------------------------------
# 2. ESTRUTURA CONDICIONAL ANINHADA (Nível 0 - Alinhado à esquerda)
# ---------------------------------------------------------
if conta_normal:
    # --- 1º Nível de Recuo (4 espaços) ---
    # Verifica se o saldo direto é suficiente para o saque[cite: 8]
    if saldo >= saque:
        # --- 2º Nível de Recuo (8 espaços) ---
        # Executado se o saldo cobrir o valor total[cite: 8]
        print("Saque realizado com sucesso!")
        
    # Caso o saldo direto não chegue, testa se o saque cabe com o cheque especial[cite: 8]
    elif saque <= (saldo + cheque_especial):
        # --- 2º Nível de Recuo (8 espaços) ---
        print("Saque realizado com uso do cheque especial!")

# Se não for conta normal, verifica se é conta universitária[cite: 8]
elif conta_universitaria:
    # --- 1º Nível de Recuo (4 espaços) ---
    if saldo >= saque:
        # --- 2º Nível de Recuo (8 espaços) ---
        print("Saque realizado com sucesso!")
    else:
        # --- 2º Nível de Recuo (8 espaços) ---
        # Executado caso o saldo seja insuficiente na conta universitária[cite: 8]
        print("Saldo insuficiente!")

# ---------------------------------------------------------
# VARIÁVEIS INICIAIS
# ---------------------------------------------------------
saldo = 2000           # Saldo disponível na conta
saque = 1500           # Valor solicitado para o saque
cheque_especial = 450  # Limite adicional do cheque especial

# ---------------------------------------------------------
# 1. VERIFICAÇÃO DE CONTA NORMAL (Nível 0 - Alinhado à esquerda)
# ---------------------------------------------------------
if conta_normal:[cite: 9]
    # --- 1º Nível de Recuo (4 espaços) ---
    if saldo >= saque:[cite: 9]
        # --- 2º Nível de Recuo (8 espaços) ---
        # Executado se o saldo direto cobrir o saque[cite: 9]
        print("Saque realizado com sucesso!")[cite: 9]
        
    elif saque <= (saldo + cheque_especial):[cite: 9]
        # --- 2º Nível de Recuo (8 espaços) ---
        # Executado se o saldo falhar, mas o cheque especial cobrir[cite: 9]
        print("Saque realizado com uso do cheque especial!")[cite: 9]
        
    else:[cite: 9]
        # --- 2º Nível de Recuo (8 espaços) ---
        # Executado se nem o saldo nem o cheque especial forem suficientes[cite: 9]
        print("Não foi possível realizar o saque, saldo insuficiente!")[cite: 9]

# ---------------------------------------------------------
# 2. VERIFICAÇÃO DE CONTA UNIVERSITÁRIA
# ---------------------------------------------------------
elif conta_universitaria:[cite: 9]
    # --- 1º Nível de Recuo (4 espaços) ---
    if saldo >= saque:[cite: 9]
        # --- 2º Nível de Recuo (8 espaços) ---
        print("Saque realizado com sucesso!")[cite: 9]
    else:[cite: 9]
        # --- 2º Nível de Recuo (8 espaços) ---
        print("Saldo insuficiente!")[cite: 9]

# ---------------------------------------------------------
# 3. VERIFICAÇÃO DE CONTA ESPECIAL
# ---------------------------------------------------------
elif conta_especial:[cite: 9]
    # --- 1º Nível de Recuo (4 espaços) ---
    print("Conta especial selecionada")[cite: 9]

# ---------------------------------------------------------
# 4. CASO PADRÃO (Fallback / Erro)
# ---------------------------------------------------------
else:[cite: 9]
    # --- 1º Nível de Recuo (4 espaços) ---
    # Executado se nenhum dos tipos de conta anteriores for verdadeiro[cite: 9]
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")[cite: 9]

# ---------------------------------------------------------
# 1. VARIÁVEIS INICIAIS
# ---------------------------------------------------------
saldo = 2000  # Define o saldo disponível na conta
saque = 500   # Define o valor pretendido para o saque

# ---------------------------------------------------------
# 2. ESTRUTURA CONDICIONAL TERNÁRIA
# ---------------------------------------------------------
# O operador ternário permite escrever uma condição numa única linha.
# Atribui "Sucesso" à variável status se a condição (saldo >= saque) for verdadeira;
# caso contrário, atribui "Falha".
status = "Sucesso" if saldo >= saque else "Falha"[cite: 10]

# ---------------------------------------------------------
# 3. SAÍDA DE DADOS (F-string)
# ---------------------------------------------------------
# Utiliza uma f-string (f"...") para interpolar a variável status diretamente na mensagem.
print(f"{status} ao realizar o saque!")[cite: 10]