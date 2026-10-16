# Exemplo 1
age = 28
name = 'Guilherme'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')
# Saída: Meu nome é Guilherme e eu tenho 28 ano(s) de idade.

# Exemplo 2
age = 27
name = 'Giovanna'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')
# Saída: Meu nome é Giovanna e eu tenho 27 ano(s) de idade.

# ==========================================
# DIFERENÇA ENTRE VARIÁVEIS E CONSTANTES
# ==========================================

# 1. VARIÁVEIS:
# São espaços na memória reservados para armazenar valores que PODEM 
# ser alterados (mutados) ao longo da execução do programa.
# No exemplo abaixo, 'age' e 'name' recebem novos valores na segunda parte.

age = 28
name = 'Guilherme'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.') #[cite: 1]

age = 27
name = 'Giovanna'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.') #[cite: 1]


# 2. CONSTANTES:
# São valores que, por definição de negócio ou lógica, NÃO devem ser alterados 
# após sua definição inicial. 
# 
# NOTA TÉCNICA SOBRE O PYTHON:
# Python não possui um mecanismo nativo (rígido) que impeça a alteração de uma 
# constante como outras linguagens fazem. Por convenção na comunidade Python, 
# nós escrevemos o nome das constantes **inteiramente em letras maiúsculas** 
# para sinalizar aos outros programadores que aquele valor é fixo e não deve ser mudado.

# Exemplo de Constante:
TAXA_JUROS = 0.05  # O valor 5% é fixo para este contexto
PI = 3.14159       # O valor matemático de Pi não muda

# Se você tentar alterar uma constante por engano, o Python tecnicamente permite 
# (pois é apenas uma convenção de nomenclatura), mas altera a regra de boas práticas:
# TAXA_JUROS = 0.10  <-- Evite fazer isso!

# =====================================================================
# TRANSCRIÇÃO DA AULA: Python não tem constantes
# =====================================================================

# Não existe uma palavra reservada para informar ao interpretador que o valor é constante. 
# Em algumas linguagens por exemplo: Java e C utilizamos final e const, respectivamente, 
# para declarar uma constante.

# Em Python usamos a convenção que diz ao programador que a variável é uma constante. 
# Para fazer isso, você deve criar a variável com o nome todo em letras maiúsculas:

# Exemplo de boa prática em Python:
# 
# LIMITES_CONEXAO = 5000
# BRAZILIAN_STATES = ["SP", "RJ", "MG", ... ]
