import pygame
import os
from entity import Entity


class Chest(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/images/chest.png", speed=0)

    def move(self):
        # O baú fica parado esperando o pirata coletar,
        #  não colocar lógica de movimento aqui.
        pass