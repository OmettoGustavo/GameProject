# Bee's Bounty

Um jogo em 2D desenvolvido com Python e Pygame, utilizando padrões de projeto para uma arquitetura limpa e modular.

## 🚀 Sobre o Projeto

O **Bee's Bounty** é um projeto acadêmico/pessoal focado na aplicação prática de padrões de projeto (Design Patterns) como **Factory** e **Mediator** para gerenciar entidades do jogo e suas interações.

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem principal.
* **Pygame**: Biblioteca para desenvolvimento de jogos 2D.
* **SQLite**: Banco de dados para persistência de pontuações (Top 10).

## 🏗️ Arquitetura e Design Patterns

O projeto foi estruturado para ser altamente extensível:
* **Factory Pattern (`EntityFactory`)**: Centraliza a criação de entidades (jogadores, cenários, pontos), facilitando a adição de novos tipos de objetos.
* **Mediator Pattern (`EntityMediator`)**: Gerencia a lógica de colisões e interação entre entidades, garantindo que os objetos sejam desacoplados.
* **Clean Architecture**: Divisão clara entre constantes (`Const.py`), lógica de jogo (`Level.py`), entidades (`Entity.py`) e persistência (`DBProxy.py`).

## 🎮 Como Jogar

1.  **Pré-requisitos**: Certifique-se de ter o Python e o Pygame instalados.
    ```bash
    pip install pygame
    ```
2.  **Execução**: Execute o arquivo principal `main.py` (ou o ponto de entrada do seu sistema).
3.  **Controles**:
    * **Jogador 1**: Setas (Cima, Baixo, Esquerda, Direita).
    * **Jogador 2**: Teclas WASD.
    * **Navegação no Menu**: Setas e Enter.

## 📋 Funcionalidades
* Modo 1 Jogador e 2 Jogadores (Cooperativo/Competitivo).
* Sistema de níveis progressivos.
* Sistema de pontuação com persistência em banco de dados.
* Detecção de colisão dinâmica e gerenciamento de saúde das entidades.

## 📂 Estrutura de Pastas
```text
/code
  ├── Background.py    # Gerenciamento dos cenários
  ├── Const.py         # Configurações globais e constantes
  ├── DBProxy.py       # Acesso ao SQLite
  ├── Entity.py        # Classe base (Abstrata)
  ├── EntityFactory.py # Fábrica de entidades
  ├── EntityMediator.py# Lógica de colisões
  ├── Game.py          # Gerenciamento do ciclo de jogo
  ├── Level.py         # Loop de nível
  ├── Menu.py          # Interface do menu
  ├── Player.py        # Lógica do jogador
  ├── Point.py         # Lógica dos pontos
  └── Score.py         # Interface de pontuação
/asset                 # Imagens e áudios
