# ==========================================
# TIPOS BUILT-IN EM PYTHON (Conforme a aula)[cite: 1]
# ==========================================

# 1. TEXTO (str)
# O tipo 'str' (string) é utilizado para representar textos e cadeias de caracteres.
nome = "Python"  # Exemplo de texto delimitado por aspas simples ou duplas


# 2. NUMÉRICO (int, float, complex)
# 'int': Números inteiros (sem parte decimal).
idade = 30

# 'float': Números de ponto flutuante (com casas decimais).
altura = 1.75

# 'complex': Números complexos, que possuem uma parte real e uma parte imaginária (indicada por 'j').
numero_complexo = 3 + 5j


# 3. SEQUÊNCIA (list, tuple, range)
# 'list': Listas são coleções ordenadas e mutáveis (podem ser alteradas após a criação).
frutas = ["maçã", "banana", "laranja"]

# 'tuple': Tuplas são semelhantes às listas, porém imutáveis (não podem ser alteradas após criadas).
coordenadas = (10.5, 20.3)

# 'range': Representa uma sequência numérica, muito utilizada em estruturas de repetição (loops).
intervalo = range(0, 10)  # Gera números de 0 a 9


# 4. MAPA (dict)
# 'dict': Dicionários armazenam dados no formato de pares de chave e valor.
usuario = {"nome": "Maria", "idade": 25, "cidade": "São Paulo"}


# 5. COLEÇÃO (set, frozenset)
# 'set': Conjuntos são coleções não ordenadas de elementos únicos (não aceitam itens duplicados) e são mutáveis.
emails = {"teste@email.com", "usuario@email.com"}

# 'frozenset': É a versão imutável de um 'set' (conjunto congelado, cujos elementos não podem ser alterados).
emails_fixos = frozenset(["admin@email.com", "suporte@email.com"])


# 6. BOOLEANO (bool)
# 'bool': Representa valores lógicos, assumindo apenas dois estados: Verdadeiro (True) ou Falso (False).
is_ativo = True
tem_permissao = False


# 7. BINÁRIO (bytes, bytearray, memoryview)
# 'bytes': Sequências de bytes imutáveis.
dados_bytes = b"Exemplo"

# 'bytearray': Semelhante aos bytes, porém é uma sequência mutável (pode ser modificada).
dados_bytearray = bytearray(b"Exemplo")

# 'memoryview': Permite que o código acesse os dados internos de um objeto que suporta o protocolo de buffer sem precisar copiá-los.
dados_memoryview = memoryview(b"Exemplo")

print(1+10)
# Transcrição do código original da aula
print(11 + 10 + 1000)
print(1.5 + 1 + 0.5)
print(True)
print(False)
print("Python")

int()
float()
str()
bool()