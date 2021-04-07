import pygame

# запуск pygame
pygame.init()

# цвета RGB
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# экран
size = [1024, 600]
screen = pygame.display.set_mode(size)

#-------------------------Основной цикл---------------------------------
# FPS
clock = pygame.time.Clock()

done=True
while done==True:
    # События 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=False
    # События конец
    
    
    # Рисование
    # экран, цвет, точка1, точка2, размер
    pygame.draw.line(screen, white, [0, 0], [640, 360], 15)
    # Рисование конец
    
    
    # Логика
    # Логика конец
    
    # обновление экрана
    pygame.display.flip()
    
    # управление обновление экрана
    clock.tick(60)
    
pygame.quit()

    
    
