import pygame 

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("knots and crosses")

color = (128, 128, 128)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.draw.rect(screen, color,pygame.Rect(50, 50, 200, 350))

pygame.quit()