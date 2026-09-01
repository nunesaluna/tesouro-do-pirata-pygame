#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys
import random
from entityFactory import EntityFactory
from background import Background


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name

        # 1. CARREGANDO O BACKGROUND DA FASE (extensão .jpg!)
        self.background = Background("assets/images/level_bg.jpg")

        # --- SISTEMA DE VIDAS ---
        self.vidas = 3
        self.score = 0
        self.fonte_hud = pygame.font.SysFont("Arial", 24, bold=True)

        # 2. ENTIDADES
        self.jogador = EntityFactory.create_entity("player", 400, 300)
        self.bau = EntityFactory.create_entity("chest", 200, 150)

        crab_x = random.randint(100, 700)
        crab_y = random.randint(50, 500)
        inimigo1 = EntityFactory.create_entity("crab", crab_x, crab_y, self.jogador)

        star_x = random.randint(100, 700)
        star_y = random.randint(50, 500)
        inimigo2 = EntityFactory.create_entity("star", star_x, star_y,self.jogador)

        shark_x = random.randint(100, 700)
        shark_y = random.randint(50, 500)
        inimigo3 = EntityFactory.create_entity("shark", shark_x, shark_y,self.jogador)

        self.entity_list = [self.jogador, inimigo1, inimigo2, inimigo3, self.bau]

    def run(self):
        jogando = True
        while jogando:
            # Mantém a fase rodando a 60 FPS estáveis
            pygame.time.Clock().tick(60)

            # --- CAPTURA DE EVENTOS (TECLADO E FECHAR JANELA) ---
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return "VOLTAR_MENU"

            # 1. ATUALIZAÇÃO DA LÓGICA DE MOVIMENTO
            for entidade in self.entity_list:
                entidade.move()

            # --- 2. SISTEMA DE COLISÃO RESTRITO (HITBOX AJUSTADA) ---
            for entidade in self.entity_list:
                if entidade != self.jogador:
                    hitbox_jogador = self.jogador.rect.inflate(-20, -20)
                    hitbox_inimigo = entidade.rect.inflate(-15, -15)

                    if hitbox_jogador.colliderect(hitbox_inimigo):
                        # === O INIMIGO SÓ DÁ DANO SE O PLAYER NÃO ESTIVER INVENCÍVEL ===
                        if not self.jogador.invencivel:
                            # O jogador perde 1 vida!
                            self.vidas -= 1

                            # === ATIVA A INVENCIBILIDADE E CAPTURA O RELÓGIO ===
                            self.jogador.invencivel = True
                            self.jogador.tempo_dano = pygame.time.get_ticks()

                            # Se ainda restarem vidas, dá um "respawn" seguro no centro
                            if self.vidas > 0:
                                self.jogador.rect.x = 400
                                self.jogador.rect.y = 300
                            else:
                                # Acabaram as vidas! Reseta para 3 e manda pro Game Over
                                self.vidas = 3
                                pygame.mixer.music.stop()
                                pygame.mixer.music.unload()
                                return "GAME_OVER"
            # 3. RENDERIZAÇÃO DO CENÁRIO DA FASE
            if self.background and self.background.image:
                self.background.draw(self.window)
            else:
                self.window.fill((34, 139, 34))

            # 4. DESENHO DAS ENTIDADES
            for entidade in self.entity_list:
                entidade.draw(self.window)

            # === ATUALIZAR E COLETAR O BAÚ ===
            # Checa se o pirata encostou no baú
            if self.jogador.rect.colliderect(self.bau.rect):
                self.score += 100  # Ganha 100 pontos!

                # Sorteia uma nova posição aleatória dentro dos limites da tela (800x600)
                self.bau.rect.x = random.randint(50, 700)
                self.bau.rect.y = random.randint(50, 500)

            # --- 5. DESENHAR INTERFACE (HUD - VIDAS E PONTOS) ---
            superficie_vidas = self.fonte_hud.render(f"VIDAS: {self.vidas} / 3", True, (255, 50, 50))
            self.window.blit(superficie_vidas, (20, 20))

            # Desenha o placar de pontos um pouco mais para a direita (x=600)
            superficie_score = self.fonte_hud.render(f"PONTOS: {self.score}", True, (255, 215, 0))  # Amarelo ouro!
            self.window.blit(superficie_score, (600, 20))

            # === NOVO: CHECAGEM DE FIM DE JOGO ===

            # 1. VITÓRIA: Se chegar a 1000 pontos, vence!
            if self.score >= 1000:
                return "VITORIA"

            # 2. DERROTA: O Game Over já é tratado na linha 49, reforço aqui:
            if self.vidas <= 0:
                return "GAME_OVER"

            # Atualiza a tela a cada frame do loop!
            pygame.display.flip()