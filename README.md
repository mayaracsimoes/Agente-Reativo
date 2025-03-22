# Agente Reativo - Aspirador de Pó Automático

Este projeto foi desenvolvido como parte da disciplina de Inteligência Artificial na FURB (Universidade Regional de Blumenau), durante o primeiro semestre de 2025. Ele implementa um **Agente Reativo Simples** que simula um aspirador de pó automático em um ambiente 6x6. O agente reage ao ambiente de forma direta: se houver sujeira na posição atual, ele a limpa; caso contrário, move-se aleatoriamente para uma posição adjacente válida.

---

## 📋 Descrição do Projeto

O ambiente é representado por uma matriz 6x6, onde:
- `1` representa paredes.
- `0` representa áreas limpas.
- `2` representa áreas sujas.

O agente começa em uma posição inicial (1x1) e se move pelo ambiente, limpando a sujeira que encontra. O programa continua executando até que toda a sujeira seja removida.

---

## 🛠️ Pré-requisitos

Para executar este projeto, você precisará ter instalado:
- **Python 3.x**
- Bibliotecas Python:
  - `numpy`
  - `matplotlib`

Você pode instalar as bibliotecas necessárias usando o seguinte comando:

```bash
pip install numpy matplotlib
```

---

## 🚀 Como Executar
1. Clone o repositório ou baixe o arquivo agente_reativo.py.

2. Navegue até o diretório onde o arquivo está localizado.

3. Execute o código com o seguinte comando:
```bash
python agente_reativo.py
```
4. O ambiente será exibido graficamente, e o agente começará a se mover e limpar a sujeira.

---

## 🎯 Funcionamento do Agente
- Reatividade Simples:

    Se houver sujeira na posição atual, o agente a limpa.

    Caso contrário, o agente move-se aleatoriamente para uma posição adjacente válida (cima, baixo, esquerda ou direita).

- Visualização:

    O ambiente é exibido graficamente usando matplotlib.
    
    O agente é representado por um ponto vermelho (o).
    
    As paredes são verdes, áreas limpas são azuis e áreas sujas são amarelas.

- Critério de Parada:

    O programa executa até que não haja mais sujeira no ambiente.

---

## 🖼️ Exemplo de Ambiente
Aqui está um exemplo de como o ambiente pode ser inicializado:
```bash
1 1 1 1 1 1
1 0 0 0 0 1
1 2 0 0 0 1
1 0 0 0 0 1
1 0 0 2 2 1
1 1 1 1 1 1
```
1: Parede (verde).

0: Área limpa (azul).

2: Área suja (amarelo).

---

## 📝 Estrutura do Código
O código está organizado da seguinte forma:

Função `criar_ambiente`: Cria o ambiente 6x6 com paredes e sujeira aleatória.

Função `exibir_ambiente`: Exibe o ambiente graficamente usando matplotlib.

Função `agente_reativo`: Implementa a lógica do agente reativo simples.

Função `main`: Controla a execução do programa, movendo o agente até que toda a sujeira seja limpa.

---

## 📊 Resultados Esperados
 - O agente limpa toda a sujeira do ambiente.

 - O tempo de execução pode variar dependendo da disposição aleatória da sujeira e dos movimentos do agente.

---

## 📜 Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
  
