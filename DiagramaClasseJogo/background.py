#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

class Background:
    def __init__(self, image_path):
        if image_path:
            try:
                self.image = pygame.image.load(image_path).convert()
                # Garante que a imagem fique exatamente do tamanho da tela do jogo (800x600)
                self.image = pygame.transform.scale(self.image, (800, 600))
            except pygame.error:
                self.image = None
                print(f"Aviso: Imagem de fundo '{image_path}' não encontrada!")
        else:
            self.image = None

    def draw(self, window):
        if self.image:
            window.blit(self.image, (0, 0))
