import random
import pygame

class Button():
    def _init_(self, x, y, pos, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos

    def clicked(self, pos):
        self.pos = pygame.mouse.get_pos()

        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
            return False
        
class RspGame():
    
    def _init_(self):
        pygame.init()

        self.screen = pygame.display.set_mode((960, 940))
        pygame.display.set_caption("RSP Shamsher")
