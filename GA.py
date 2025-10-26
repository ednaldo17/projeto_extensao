from sympy import Rational, sqrt

# Função para somar dois vetores
def somar_vetores(v, w):
    # Verifica se os dois vetores têm o mesmo tamanho (mesma dimensão)
    if len(v) != len(w):
        # Caso os vetores tenham tamanhos diferentes, dará erro
        raise ValueError("Vetores de dimensão diferentes.")
    # Retorna uma lista onde cada elemento é a soma dos elementos correspondentes dos dois vetores
    return [v[i] + w[i] for i in range(len(v))]        

# Função para subtrair dois vetores
def sub_vetores(v, w):
    # Verifica se os dois vetores têm o mesmo tamanho (mesma dimensão)
    if len(v) != len(w):
        # Caso os vetores tenham tamanhos diferentes, dará erro
        raise ValueError("Vetores de dimensão diferentes.")
    # Retorna uma lista onde cada elemento é a subtração dos elementos correspondentes
    return [v[i] - w[i] for i in range(len(v))]

# Função para calcular o produto escalar (produto interno)
def prod_esc(v, w):
    # Verifica se os dois vetores têm o mesmo tamanho (mesma dimensão)
    if len(v) != len(w):
        # Caso os vetores tenham tamanhos diferentes, dará erro
        raise ValueError("Vetores de dimensão diferentes.")
    # Retorna o valor do produto escalar entre v e w
    return sum(v[i] * w[i] for i in range(len(v)))
        
# Função para multiplicar um vetor por um escalar
def mult_escalar(v, escalar):
    # Retorna uma lista onde cada componente do vetor é multiplicado por um escalar 
    return [v[i] * escalar for i in range(len(v))]

# Função para calcular a norma (comprimento) de um vetor
def norma(v):
    # Retorna a norma de um vetor, calculando a raiz quadrada de v * v
    return sqrt(prod_esc(v, v))

# Função para calcular o vetor unitário
def unit(v):
    n = norma(v)
    # Verifica se o vetor é um vetor nulo
    if n == 0:
        # Caso o vetor seja nulo, dará erro
        raise ValueError("Não é possível calcular o vetor unitário de um vetor nulo.")
    # Retorna cada componente do vetor dividido pela norma
    return [v[i]/Rational(n) for i in range(len(v))]    

# Função para calcular o produto vetorial entre dois vetores 3D
def prod_vet(v, w):
    # Verifica se os dois vetores são tridimensionais
    if len(v) != 3 or len(w) != 3:
        # Caso os vetores não sejam 3D, dará erro
        raise ValueError("Vetores com dimensões diferentes de 3.")
    # Retorna o produto vetorial
    return [
        v[1] * w[2] - v[2] * w[1],
        v[2] * w[0] - v[0] * w[2],
        v[0] * w[1] - v[1] * w[0]
        ]

# Função para calcular a projeção de um vetor v sobre outro vetor w
def proj_vet(v, w):
    # Verifica se os dois vetores têm o mesmo tamanho (mesma dimensão)
    if len(v) != len(w):
        # Caso os vetores tenham diferentes, dará erro
        raise ValueError("Vetores de dimensão diferentes.")
    den = prod_esc(w, w) # Calcula w * w = ||w||²
    # Verifica se w é um vetor nulo
    if den == 0:
        # Caso w seja nulo, dará erro
        raise ValueError("Não é possível projetar sobre o vetor nulo.")
    num = prod_esc(v, w) # Calcula v * w
    coe = Rational(num, den) # Calcula o coeficiente escalar da projeção
    # Retorna a projeção de v sobre w
    return [coe * w[i] for i in range(len(v))]

# Função Gram-Schmidt para ortogonalizar um conjunto de vetores
def gram_schmidt(v):
    ortogonais = [] # Lista para armazenar os vetores ortogonais
    
    for i in v:
        v_ort = i # Começa com o vetor original
        # Remove a projeção de v em todos os vetores já ortogonais
        for u in ortogonais:
            proj = proj_vet(v_ort, u) # Projeção de v_ort sobre u
            v_ort = sub_vetores(v_ort, proj) # Subtrai a projeção
        ortogonais.append(v_ort) # Adiciona o vetor ortogonalizado à lista
    # Retorna os vetores ortogonalizados
    return ortogonais