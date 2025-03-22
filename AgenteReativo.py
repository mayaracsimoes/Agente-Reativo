import time

import numpy as np
import matplotlib.pyplot as plt
import random

def mapear_ambiente():
    ambiente = np.ones((6, 6), dtype=int)
    ambiente[1:5, 1:5] = 0  # Define o espaço útil 4x4 como limpo

    # Adiciona sujeira aleatoriamente no espaço útil - Definido como '2' na matriz
    for i in range(1, 5):
        for j in range(1, 5):
            if random.random() < 0.4:  # 40% de chance de sujeira em cada célula
                ambiente[i, j] = 2

    return ambiente

def exibir_ambiente(ambiente, pos_agente):
    plt.imshow(ambiente, 'gray')
    plt.nipy_spectral()
    plt.plot([pos_agente[1]], [pos_agente[0]], marker='*', color='r', ls='', label='Agente Reativo')
    plt.legend()
    plt.show(block=False)
    plt.pause(0.5)
    plt.clf()

def main():
    ambiente = mapear_ambiente()

    # Posição inicial fixa (1, 1)
    pos_agente = (1, 1)

    # Percorre a matriz em zigue-zague
    for i in range(1, 5):
        if i % 2 == 1:  # Linhas impar, esquerda para direita
            for j in range(1, 5):
                # Exibe o ambiente antes de mover o agente
                print(f"Agente se movendo para ({i}, {j})")
                exibir_ambiente(ambiente, pos_agente)
                time.sleep(0.2)  # Pausa para visualizar o movimento

                # Move o agente para a nova posição
                pos_agente = (i, j)

                # Exibe o ambiente após mover o agente
                print(f"Agente chegou a ({i}, {j})")
                exibir_ambiente(ambiente, pos_agente)
                time.sleep(0.2)  # Pausa para visualizar a nova posição

                # Verifica se há sujeira na posição atual
                if ambiente[i, j] == 2:
                    print(f"Agente Reativo: Encontrou sujeira em ({i}, {j}). Limpando...")
                    time.sleep(0.2)  # Pausa antes de limpar
                    ambiente[i, j] = 0

                    exibir_ambiente(ambiente, pos_agente)  # Exibe o ambiente após limpar
                    time.sleep(0.2)  # Pausa para visualizar a célula limpa
        else:  # Linhas pares: direita para esquerda
            for j in range(4, 0, -1):
                # Exibe o ambiente antes de mover o agente
                print(f"Agente se movendo para ({i}, {j})")
                exibir_ambiente(ambiente, pos_agente)
                time.sleep(0.2)  # Pausa para visualizar o movimento

                # Move o agente para a nova posição
                pos_agente = (i, j)

                # Exibe o ambiente após mover o agente
                print(f"Agente chegou a ({i}, {j})")
                exibir_ambiente(ambiente, pos_agente)
                time.sleep(0.2)  # Pausa para visualizar a nova posição

                # Verifica se há sujeira na posição atual
                if ambiente[i, j] == 2:
                    print(f"Agente Reativo: Encontrou sujeira em ({i}, {j}). Limpando...")
                    time.sleep(0.2)  # Pausa antes de limpar
                    ambiente[i, j] = 0

                    exibir_ambiente(ambiente, pos_agente)  # Exibe o ambiente após limpar
                    time.sleep(0.2)  # Pausa para visualizar a célula limpa

    print("Todas as células foram visitadas!")
    exibir_ambiente(ambiente, pos_agente)  # Exibe o estado final


if __name__ == "__main__":
    main()