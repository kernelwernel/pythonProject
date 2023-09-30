import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1600, 1200
BALL_SPEED = 4
PADDLE_SPEED = 10
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Ball properties
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Paddle properties
player_lpaddle = pygame.Rect(50, HEIGHT // 2 - 60, 20, 175)
player_rpaddle = pygame.Rect(WIDTH - 50, HEIGHT // 2 - 60, 20, 175)
paddle_speed = PADDLE_SPEED

# Scores
player_score = 0
opponent_score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Right move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_lpaddle.top > 0:
        player_lpaddle.y -= paddle_speed
    if keys[pygame.K_s] and player_lpaddle.bottom < HEIGHT:
        player_lpaddle.y += paddle_speed

    # Left move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rpaddle.top > 0:
        player_rpaddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and player_rpaddle.bottom < HEIGHT:
        player_rpaddle.y += paddle_speed

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collisions with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Ball collisions with paddles
    if ball.colliderect(player_lpaddle) or ball.colliderect(player_rpaddle):
        ball_dx *= -1

    # Ball out of bounds
    if ball.left <= 0:
        opponent_score += 1
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_dx = BALL_SPEED
        ball_dy = BALL_SPEED

    if ball.right >= WIDTH:
        player_score += 1
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_dx = -BALL_SPEED
        ball_dy = BALL_SPEED

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player_lpaddle)
    pygame.draw.rect(screen, WHITE, player_rpaddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Display scores
    font = pygame.font.Font(None, 36)
    player_text = font.render(f"Player: {player_score}", True, WHITE)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
    screen.blit(player_text, (50, 20))
    screen.blit(opponent_text, (WIDTH - 250, 20))

    # Update the display
    pygame.display.flip()

pygame.quit()
