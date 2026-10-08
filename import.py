'''
EXEMPLO 1: Importar o módulo completo
Neste exemplo, importa-se o módulo math utilizando a declaração import[cite: 8]. 
Em seguida, utiliza-se a função sqrt() do módulo math para calcular a raiz quadrada de 25[cite: 8].
'''

import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0[cite: 8]


'''
EXEMPLO 2: Importar funções específicas de um módulo
Também podemos importar funções específicas de um módulo utilizando a sintaxe from módulo import função[cite: 8].
Neste caso, importa-se apenas a função sqrt() do módulo math, o que nos permite 
utilizá-la diretamente sem ter que precedê-la com o nome do módulo[cite: 8].
'''

from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0[cite: 8]