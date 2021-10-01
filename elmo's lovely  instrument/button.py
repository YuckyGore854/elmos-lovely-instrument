import pygame

class button:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def click(self, mouseX, mouseY, lclick):
        if mouseX > self.x and mouseX < self.x + self.w and mouseY > self.y and mouseY < self.y+self.h and lclick is True:
            return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, (120, 180, 140), (self.x, self.y, self.w, self.h))
