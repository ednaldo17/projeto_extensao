from minhabibliotecasvm import *
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# Loop para pedir os vetores até que o usuário digite algo válido (sem divisão por zero)
while True:
    # Solicita os pontos ao usuário e remove espaços em branco
    pontos = (input("Insira os pontos (vetores em Rn) separados por vírgula: ")).replace(" ", "")
    
    # Verifica se existe algo como "/0" nos vetores (evitando divisão por zero)
    if "/0," not in pontos and "/0)" not in pontos:
        break  # Sai do loop quando válido

# Conta quantos vetores foram digitados (baseado nas fechamentos de parênteses)
qtd_vetores = pontos.count(")")

# Separa a entrada em cadeias individuais correspondentes a vetores
vetores = separar_cadeias_vetores(pontos)

# Verifica a dimensão dos vetores pelo número de vírgulas
dim_inicial = vetores[0].count(",")

# Checa se **todos** os vetores têm a mesma dimensão
mesma_dim = all(vetores[i].count(",") == dim_inicial for i in range(1, qtd_vetores))

# Caso as dimensões não coincidam, encerra
if not mesma_dim:
    print(f"Você inseriu os seguintes {qtd_vetores} pontos:")
    for v in vetores:
        print(tuple(vetorcadeia_para_vetornumerico(v)))  # Mostra vetores já convertidos para numéricos
    print("Não é possível operar pontos (vetores) de dimensões diferentes.")
    exit()

# Caso o usuário tenha digitado EXATAMENTE 2 vetores:
if qtd_vetores == 2:
    print(f"Você inseriu dois vetores de dimensão {dim_inicial + 1}:")
    
    # Converte cada vetor para lista de números e os coloca em b
    b = [vetorcadeia_para_vetornumerico(v) for v in vetores]
    
    # Exibe os vetores convertidos
    for v in b:
        print(tuple(v))
    
    # Se os vetores forem iguais, não existe reta distinta entre eles
    if b[0] == b[1]:
        print("Na realidade, os dois vetores inseridos são iguais.")
        exit()

    # Calcula o vetor diretor como diferença entre os dois vetores
    vetor_diretor = diferenca_vetores(b[0], b[1])
    print(f"\nO vetor diretor à reta é v = {tuple(b[0])} - {tuple(b[1])} = {tuple(vetor_diretor)}")
    
    # Escreve a equação vetorial da reta
    print("A equação vetorial da reta que passa pelos vetores dados é:")
    print(f"L: {tuple(b[0])} + t{tuple(vetor_diretor)}")
    
    # Caso seja R² (dimensão 2), é possível formar a equação analítica da reta
    if dim_inicial == 1:
        x, y = symbols("x,y")
        
        # Vetor normal obtido rotacionando o vetor diretor em 90°
        vetor_normal = [-vetor_diretor[1], vetor_diretor[0]]
        
        # Constante c da equação geral Ax + By = c
        c = produto_escalar(vetor_normal, b[0])
        
        print(f"O vetor normal à reta é n = {tuple(vetor_normal)}")
        print("Portanto, a equação fundamental da reta é:")
        print(f"{vetor_normal[0]*x + vetor_normal[1]*y} = c")
        print(f"Onde c = {tuple(vetor_normal)} * {tuple(b[0])} = {c}")
        
        # Forma da equação geral Ax + By = C (com sinal ajustado)
        print("Em consequência, a equação geral da reta que passa pelos pontos dados é: ", end="")
        if vetor_normal[0] < 0:
            print(f"{-(vetor_normal[0]*x + vetor_normal[1]*y)} = {-c}")
        else:
            print(f"{vetor_normal[0]*x + vetor_normal[1]*y} = {c}")
        
        # Plotagem da reta no plano cartesiano
        if vetor_normal[1] != 0:
            # Caso a reta não seja vertical, isolamos y
            x_vals = np.linspace(-20, 20, 400)
            y_vals = (c - vetor_normal[0] * x_vals) / vetor_normal[1]
            plt.plot(x_vals, y_vals)
        else:
            # Caso seja vertical, isolamos x
            x_vals = np.full(400, c / vetor_normal[0])
            y_vals = np.linspace(-20, 20, 400)
            plt.plot(x_vals, y_vals)
        
        # Eixos e grade para referência visual
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.grid(True)
        plt.show()

        exit()

# Caso o usuário tenha digitado EXATAMENTE 3 vetores e sejam de R³ (dimensão 3)
# Podemos, assim, determinar o plano que passa pelos três pontos
if qtd_vetores == 3 and dim_inicial == 2:
        print(f"\nVocê inseriu 3 vetores em R³:")

        # Converte as cadeias digitadas para vetores numéricos
        b = [vetorcadeia_para_vetornumerico(v) for v in vetores]

        # Exibe os vetores no formato de tupla (mais legível)
        for v in b:
            print(tuple(v))

        # Calculamos dois vetores do plano: v1 e v2 (origem comum em b[0])
        v1 = diferenca_vetores(b[0], b[1])
        v2 = diferenca_vetores(b[0], b[2])

        # O vetor normal ao plano é dado pelo produto vetorial entre v1 e v2
        n = produto_vetorial(v1, v2)

        # Se o vetor normal for o vetor nulo, então os 3 pontos são colineares
        if all(coord == 0 for coord in n):
            print("\nOs três vetores são colineares, logo não determinan um plano.")
            exit()

        # Calculamos o termo d da equação do plano usando produto escalar
        d = produto_escalar(n, b[0])

        # Exibindo vetores que pertencem ao plano
        print("\nDois vetores do plano:")
        print(f"v = {tuple(v1)} = {tuple(b[0])} - {tuple(b[1])}")
        print(f"w = {tuple(v2)} = {tuple(b[0])} - {tuple(b[2])}")

        # Exibição do vetor normal encontrado
        print("\nVetor normal ao plano:")
        print(f"n = v x w = {tuple(v1)} x {tuple(v2)} = {tuple(n)}")
        
        # Definição das variáveis simbólicas para expressar a equação do plano
        x, y, z = symbols("x,y,z")

        # Fórmula geral do plano: n1x + n2y + n3z = d
        plano_simbolico = n[0]*x + n[1]*y + n[2]*z

        print(f"Portanto, a equação do nosso plano é: {plano_simbolico} = d")
        print(f"Para d = {tuple(n)} * {tuple(b[0])} = {d}")
        
        # Ajuste de sinal para manter padrão visual (primeiro coeficiente positivo)
        if n[0] < 0:
            n = [-coord for coord in n] # Inverte todos os sinais de n
            d = -d                      # Ajusta d proporcionalmente
            plano_simbolico = -plano_simbolico

        # Exibe a forma final da equação do plano
        print('Em consequência, a equação do plano que passa pelos pontos dados é: ',end='')
        print(f"{plano_simbolico} = {d}")

        # Criação da figura 3D para plotar o plano
        fig = plt.figure(figsize=(7, 7))
        ax = fig.add_subplot(projection="3d")

        # Para plotar o plano, precisamos isolar uma variável dependendo de qual componente de n é não-nulo
        if n[2] != 0:
            # Se n₃ ≠ 0, isolamos z
            x_vals, y_vals = np.mgrid[-10:10:200j, -10:10:200j]
            z_vals = (d - n[0]*x_vals - n[1]*y_vals) / n[2]
        elif n[1] != 0:
            # Se n₂ ≠ 0, isolamos y
            x_vals, z_vals = np.mgrid[-10:10:200j, -10:10:200j]
            y_vals = (d - n[0]*x_vals - n[2]*z_vals) / n[1]
        else:
            # Caso contrário, isolamos x
            y_vals, z_vals = np.mgrid[-10:10:200j, -10:10:200j]
            x_vals = (d - n[1]*y_vals - n[2]*z_vals) / n[0]
        
        # Plota a superfície do plano
        ax.plot_surface(x_vals, y_vals, z_vals, alpha=0.6)

        # Marca os pontos originais no gráfico
        xs, ys, zs = zip(*b)
        ax.scatter(xs, ys, zs, s=50, color="red")
        
        # Rotula eixos
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

        # Exibe a figura
        plt.show()

# Caso o número de vetores seja igual à dimensão + 1 e todos tenha a mesma dimensão
# Podemos, assim, aplicar a ortogonalização de Gram-Schmidt
if qtd_vetores == dim_inicial + 1 and mesma_dim:
    # Calcula os vetores ortogonais a partir dos vetores originais
    vetores_ortogonais = ortogonalizacao_gram_schmidt(b)

    print("Os vetores obtidos na ortogonalização de Gram-Schmidt são:")

    # Percorre cada vetor ortogonal
    for vetor in vetores_ortogonais:
        # Se o vetor não for nulo, imprime sua versão unitária
        if norma(vetor) != 0:
            print(tuple(vetor_unitario(vetor)))
        else:
            # Caso o vetor seja nulo, imprime como está
            print(tuple(vetor))
