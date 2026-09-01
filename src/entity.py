#!/usr/bin/python
# -*- coding: utf-8 -*-
# entity.py
import pygame
from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, x, y, image_path, speed):
        # Carrega a imagem da entidade
        self.surface = pygame.image.load(image_path)

        # O 'rect' é a caixa de colisão e posicionamento do Pygame
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Velocidade de movimento
        self.speed = speed

    # método move abstrato porque o Player se move pelo teclado
    # e o Enemy se move por inteligência artificial (comportamentos diferentes!)
    @abstractmethod
    def move(self):
        pass

    def draw(self, window):
        # Método comum para desenhar qualquer entidade na janela
        window.blit(self.surface, self.rect)
