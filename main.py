# importing and initialising pygame
import pygame
import time

pygame.init()

screen_width = 500
screen_height = 500

size = (screen_height, screen_width)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pong")

white = (255, 255, 255)

running = True
clock = pygame.time.Clock()

# Initial position of the pixel
x, y = screen_width // 2, screen_height // 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses to move the pixel
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 10
    if keys[pygame.K_RIGHT]:
        x += 10
    if keys[pygame.K_UP]:
        y -= 10
    if keys[pygame.K_DOWN]:
        y += 10

    # Clear the screen
    screen.fill(white)

    # Draw the pixel (a small rectangle)
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 10, 10))
    
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 10, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()