import pygame
import button

pygame.init()

screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Crab")
clock = pygame.time.Clock()

running = True
victorBlorez = button.button(50,50,50,50)
IraelBhavez= button.button(350,350,50,50)
IzaeahCordzaea = button.button(680, 0, 20, 20)
miguelMiguel = button.button(100,100,50,50)
fuunyman = button.button(150,150,50,50)

pygame.init()
pygame.font.init()
pygame.mixer.init()

#def crash():
#    pygame.mixer.Sound.play(sound)
#    pygame.mixer.music.stop()
    
#    sound = pygame.mixer.Sound("sound.mp3")
while running:
    clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    lmouse = pygame.mouse.get_pressed(3)
    mousePos = pygame.mouse.get_pos()
    if victorBlorez.click(mousePos[0],mousePos[1],lmouse[0]):
        print("click")
        pygame.mixer.music.pause()
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(-1)

    if IraelBhavez.click(mousePos[0],mousePos[1],lmouse[0]):
        print("click")
        pygame.mixer.music.pause()
        pygame.mixer.music.load('tnt.mp3')
        pygame.mixer.music.play(-1)

    if miguelMiguel.click(mousePos[0],mousePos[1],lmouse[0]):
        pygame.mixer.music.pause()
        pygame.mixer.music.load('gta.mp3')
        pygame.mixer.music.play(-1)

    if fuunyman.click(mousePos[0],mousePos[1],lmouse[0]):
        pygame.mixer.music.pause()
        pygame.mixer.music.load('wot.mp3')
        pygame.mixer.music.play(-1)

    if IzaeahCordzaea.click(mousePos[0],mousePos[1],lmouse[0]):
        pygame.mixer.music.pause()

    IraelBhavez.draw(screen)
    victorBlorez.draw(screen)
    IzaeahCordzaea.draw(screen)
    miguelMiguel.draw(screen)
    fuunyman.draw(screen)
    pygame.display.flip()

pygame.quit()
