import pygame
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Spiel: Schlange")

run = True
speed = 5
image = pygame.image.load("schlange.png")
image_rect = image.get_rect()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            image_rect.x -= speed
        if keys[pygame.K_RIGHT]:
            image_rect.x += speed
        if keys[pygame.K_UP]:
            image_rect.y -= speed
        if keys[pygame.K_DOWN]:
            image_rect.y += speed
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX-60
            image_rect.y = mouseY-60
    screen.fill((100, 15, 100))
    screen.blit(image, image_rect)
    pygame.display.flip()

# eog game, eof file
pygame.quit()
