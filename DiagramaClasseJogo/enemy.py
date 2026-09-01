#!/usr/bin/python
# -*- coding: utf-8 -*-

from entity import Entity


class Enemy(Entity):
    def __init__(self, x, y, tipo_inimigo, jogador, speed=2):
        # O tipo_inimigo vai definir qual imagem carregar dinamicamente!
        # Ex: se tipo_inimigo for "crab", carrega "assets/images/enemy_crab.png"
        caminho_imagem = f"assets/images/enemy_{tipo_inimigo}.png"

        # Passa a imagem correta para a classe mãe Entity
        super().__init__(x, y, caminho_imagem, speed)

        self.tipo = tipo_inimigo
        self.jogador = jogador

    def move(self):
        if not self.jogador:
            return

        # 1. Perseguição Suave (com tolerância para não tremer)
        tolerancia = 2

        # Move no X
        if abs(self.rect.x - self.jogador.rect.x) > tolerancia:
            if self.rect.x < self.jogador.rect.x:
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed

        # Move no Y
        if abs(self.rect.y - self.jogador.rect.y) > tolerancia:
            if self.rect.y < self.jogador.rect.y:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed

        # 2. A "Cerca Invisível": Impede que ele fuja da tela!
        # Isso garante que ele nunca passe de 0 ou saia da largura/altura da janela (800x600)
        self.rect.x = max(50, min(self.rect.x, 750))
        self.rect.y = max(50, min(self.rect.y, 550))