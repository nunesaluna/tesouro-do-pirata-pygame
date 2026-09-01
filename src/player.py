#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from entity import Entity


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/images/player.png", speed=5)

        # === NOVAS VARIÁVEIS PARA O EFEITO DE PISCAR ===
        self.invencivel = False
        self.tempo_dano = 0
        self.duracao_invencibilidade = 1500  # Tempo em milissegundos (1,5 segundos)

    def move(self):
        teclas = pygame.key.get_pressed()

        # Movimentação normal
        if teclas[pygame.K_UP]:
            self.rect.y -= self.speed
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.speed
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # --- PAREDES INVISÍVEIS (LIMITES DA TELA) ---

        # 1. Limite da Esquerda (X mínimo é 0)
        if self.rect.x < 0:
            self.rect.x = 0

        # 2. Limite da Direita (Largura da tela 800 - largura do boneco)
        if self.rect.x > 800 - self.rect.width:
            self.rect.x = 800 - self.rect.width

        # 3. Limite de Cima (Y mínimo é 0)
        if self.rect.y < 0:
            self.rect.y = 0

        # 4. Limite de Baixo (Altura da tela 600 - altura do boneco)
        if self.rect.y > 600 - self.rect.height:
            self.rect.y = 600 - self.rect.height

    # === MÉTODO: CONTROLADOR DO DESENHO E DO PISCA-PISCA ===
    def draw(self, window):
        # 1. PEGA O RELÓGIO DO JOGO
        agora = pygame.time.get_ticks()

        # Se o jogador estiver no período de invencibilidade
        if self.invencivel:
            # Se o tempo acabou, desliga a invencibilidade
            if agora - self.tempo_dano > self.duracao_invencibilidade:
                self.invencivel = False
                # Mudamos de self.image para self.surface!
                window.blit(self.surface, self.rect)
            else:
                # Efeito de piscar alternando o desenho a cada 75ms
                if (agora % 150) > 75:
                    # Mudamos de self.image para self.surface!
                    window.blit(self.surface, self.rect)
        else:
            # Condição normal: apenas desenha o pirata na tela
            # Mudamos de self.image para self.surface!
            window.blit(self.surface, self.rect)