#!/usr/bin/python
# -*- coding: utf-8 -*-

# entityFactory.py
from player import Player
from enemy import Enemy
from chest import Chest


class EntityFactory:
    @staticmethod
    def create_entity(tipo, x, y, jogador=None):
        """
        Método estático que fabrica qualquer entidade do jogo.
        recebe o parâmetro opcional 'jogador' para os inimigos o perseguirem.
        """
        if tipo == "player":
            return Player(x, y)

        elif tipo == "crab":
            # Passa o jogador para o inimigo caranguejo
            return Enemy(x, y, "crab", jogador, speed = 0.6)

        elif tipo == "star":
            # Passa o jogador para o inimigo estrela
            return Enemy(x, y, "star", jogador, speed = 1.5)

        elif tipo == "shark":
            # Passa o jogador para o inimigo tubarão
            return Enemy(x, y, "shark", jogador, speed = 2.0)

        elif tipo == "chest":
            return Chest(x, y)

        return None
