<<<<<<< HEAD


import pygame, math

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

FPSCLOCK = pygame.time.Clock()

pi = 3.14159
degree = 0

green = [0,128,0]
blue = [0,0,255]
red = [255,0,0]
white = [255,255,255]
grey = [128,128,128]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    radar = (100, 100)
    radar_len = 50
    x = radar[0] + math.cos(math.radians(degree)) * radar_len
    y = radar[1] + math.sin(math.radians(degree)) * radar_len

    pygame.draw.rect(screen, [0,255,0],(0,0,100,100),1)
    pygame.draw.line(screen, white ,radar, [x,y],1)





    #pygame.draw.line(screen, blue, [80,80],(x,y),1)
    pygame.display.flip()




    FPSCLOCK.tick(30)

=======


import pygame, math

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

FPSCLOCK = pygame.time.Clock()

pi = 3.14159
degree = 0

green = [0,128,0]
blue = [0,0,255]
red = [255,0,0]
white = [255,255,255]
grey = [128,128,128]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    radar = (100, 100)
    radar_len = 50
    x = radar[0] + math.cos(math.radians(degree)) * radar_len
    y = radar[1] + math.sin(math.radians(degree)) * radar_len

    pygame.draw.rect(screen, [0,255,0],(0,0,100,100),1)
    pygame.draw.line(screen, white ,radar, [x,y],1)





    #pygame.draw.line(screen, blue, [80,80],(x,y),1)
    pygame.display.flip()




    FPSCLOCK.tick(30)

>>>>>>> fbca7da7abe4ab3d4609abfd3dad9c5f7cbf0209
