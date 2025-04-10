import pygame
import time
import sys

# Init
pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Robot Face")
clock = pygame.time.Clock()

# Load logo image
logo = pygame.image.load("42ad_logo_small.png").convert_alpha()
logo_rect = logo.get_rect()

# Colors
GRAY = (180, 180, 180)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
BLUE = (50, 100, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def draw_robot(smile=True, wink=False):
    screen.fill((30, 30, 30))  # Background

    # Face base
    pygame.draw.rect(screen, GRAY, (150, 40, 500, 400), border_radius=40)
    pygame.draw.rect(screen, DARK_GRAY, (150, 40, 500, 400), 6, border_radius=40)

    # Forehead panel
    pygame.draw.rect(screen, BLUE, (250, 60, 300, 40), border_radius=10)
    pygame.draw.rect(screen, WHITE, (250, 60, 300, 40), 3, border_radius=10)

    # Eyes
    left_eye_rect = pygame.Rect(250, 150, 60, 100)
    right_eye_rect = pygame.Rect(490, 150, 60, 100)

    if wink:
        # Wink left eye (draw line)
        pygame.draw.line(screen, BLACK, (left_eye_rect.centerx - 25, left_eye_rect.centery),
                         (left_eye_rect.centerx + 25, left_eye_rect.centery), 8)
    else:
        pygame.draw.ellipse(screen, WHITE, left_eye_rect)
        pygame.draw.ellipse(screen, BLACK, (left_eye_rect.x + 20, left_eye_rect.y + 30, 20, 40))  # pupil

    pygame.draw.ellipse(screen, WHITE, right_eye_rect)
    pygame.draw.ellipse(screen, BLACK, (right_eye_rect.x + 20, right_eye_rect.y + 30, 20, 40))  # pupil

    # Smile
    if smile:
        pygame.draw.arc(screen, BLACK, (300, 250, 200, 100), 3.14, 0, 6)

    # Cheeks
    pygame.draw.circle(screen, RED, (230, 290), 15)
    pygame.draw.circle(screen, RED, (570, 290), 15)

	# Position logo in the bottom-right corner with 10px margin
    logo_x = 800 - logo_rect.width - 10
    logo_y = 480 - logo_rect.height - 10
    screen.blit(logo, (logo_x, logo_y))

    pygame.display.flip()

# Run
start_time = time.time()
running = True
wink_triggered = False

while running:
    clock.tick(60)
    elapsed = time.time() - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # First 3 seconds: normal smile
    if elapsed < 3:
        draw_robot(smile=True, wink=False)
    # Then wink for 1 second
    elif elapsed < 4:
        draw_robot(smile=True, wink=True)
    else:
        draw_robot(smile=True, wink=False)

pygame.quit()
sys.exit()