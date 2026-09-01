# Arquitetura do Jogo

```mermaid
graph TD
    game[game.py <br><i>Ponto de Partida & Janela Principal</i>] -->|Gerencia & Alterna| menu[menu.py <br><i>Tela de Menu & Comandos</i>]
    game -->|Gerencia & Alterna| level[level.py <br><i>Tela da Fase & Loop de Jogo</i>]
    
    level -->|Solicita Criação| factory[entityFactory.py <br><i>Fábrica de Entidades</i>]
    
    factory -->|Cria instâncias de| player[player.py <br><i>Jogador</i>]
    factory -->|Cria instâncias de| enemy[enemy.py <br><i>Inimigo</i>]
    factory -->|Cria instâncias de| bg[background.py <br><i>Cenário</i>]
    
    player -->|Herda de| entity[entity.py <br><i>Classe Mãe Abstrata</i>]
    enemy -->|Herda de| entity
    bg -->|Herda de| entity

    style game fill:#1a5276,stroke:#fff,stroke-width:2px,color:#fff
    style menu fill:#2e4053,stroke:#fff,stroke-width:1px,color:#fff
    style level fill:#2e4053,stroke:#fff,stroke-width:1px,color:#fff
    style factory fill:#7d6608,stroke:#fff,stroke-width:1px,color:#fff
    style entity fill:#117a65,stroke:#fff,stroke-width:1px,color:#fff