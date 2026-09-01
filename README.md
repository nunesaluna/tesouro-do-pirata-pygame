# 🏴‍☠️ Tesouro do Pirata - Jogo 2D com Pygame

Este projeto consiste em uma versão demo interativa e totalmente jogável, desenvolvida em Python com a biblioteca Pygame como um trabalho prático de engenharia de software. A aplicação foi estruturada seguindo requisitos específicos de escopo técnico, aplicando conceitos consolidados de arquitetura, padrões de projeto e boas práticas de programação.

O grande diferencial do desenvolvimento foi a aplicação prática dos pilares da Engenharia de Software, utilizando **Programação Orientada a Objetos (POO)**, **Herança de Classes** e o padrão de projeto **Factory Pattern (Padrão de Fábrica)** para garantir o desacoplamento e a escalabilidade do código.


## 🚀 Tecnologias Utilizadas
* **Python** (Lógica estruturada e controle de estados)
* **Pygame** (Manipulação de eventos do teclado, renderização de gráficos 2D e áudio)
* **Mermaid UML** (Modelagem e mapeamento da arquitetura de classes)

## 🎮 Como Jogar
* **Setas Direcionais:** Movimentam o personagem pirata na tela.
* **ENTER:** Inicia o jogo a partir do menu principal.
* **ESC:** Pausa ou retorna ao menu inicial.

## 🛠️ Engenharia de Software e Estrutura do Código
O projeto foi modelado seguindo boas práticas de desenvolvimento para garantir a escalabilidade e o desacoplamento do código:
* **Classe Mãe Abstrata (`entity.py`):** Define a estrutura base de comportamento para todas as entidades do jogo.
* **Fábrica de Entidades (`entityFactory.py`):** Centraliza e automatiza a criação de instâncias de jogadores, inimigos e cenários.
* **Gerenciamento de Telas:** Divisão clara de responsabilidades entre o loop principal (`game.py`), a interface de comandos (`menu.py`) e a execução da fase (`level.py`).

Para verificar o mapeamento completo e o diagrama de heranças, acesse o arquivo descritivo [arquitetura.md](./arquitetura.md).
