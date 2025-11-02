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
        x, y = symbols("x y")
        
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
