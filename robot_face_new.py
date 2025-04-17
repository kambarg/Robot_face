import pygame
import time
import sys

# Init
pygame.init()

# Get display resolution
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

# Set full screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Robot Face")
clock = pygame.time.Clock()

# Load and scale logo
logo = pygame.image.load("42ad_logo_small.png").convert_alpha()
logo_scale = 0.15  # Adjust this to your preference
logo = pygame.transform.smoothscale(logo, (int(logo.get_width() * logo_scale), int(logo.get_height() * logo_scale)))
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

    # Proportions based on screen size
    face_rect = pygame.Rect(WIDTH * 0.2, HEIGHT * 0.08, WIDTH * 0.6, HEIGHT * 0.75)
    pygame.draw.rect(screen, GRAY, face_rect, border_radius=40)
    pygame.draw.rect(screen, DARK_GRAY, face_rect, 6, border_radius=40)

    # Forehead panel
    forehead_rect = pygame.Rect(WIDTH * 0.31, HEIGHT * 0.10, WIDTH * 0.38, HEIGHT * 0.08)
    pygame.draw.rect(screen, BLUE, forehead_rect, border_radius=10)
    pygame.draw.rect(screen, WHITE, forehead_rect, 3, border_radius=10)

    # Eyes
    left_eye = pygame.Rect(WIDTH * 0.31, HEIGHT * 0.32, WIDTH * 0.075, HEIGHT * 0.22)
    right_eye = pygame.Rect(WIDTH * 0.59, HEIGHT * 0.32, WIDTH * 0.075, HEIGHT * 0.22)

    if wink:
        pygame.draw.line(screen, BLACK, (left_eye.centerx - WIDTH * 0.03, left_eye.centery),
                         (left_eye.centerx + WIDTH * 0.03, left_eye.centery), 8)
    else:
        pygame.draw.ellipse(screen, WHITE, left_eye)
        pygame.draw.ellipse(screen, BLACK, (
            left_eye.x + left_eye.width * 0.33,
            left_eye.y + left_eye.height * 0.3,
            left_eye.width * 0.33,
            left_eye.height * 0.4
        ))

    pygame.draw.ellipse(screen, WHITE, right_eye)
    pygame.draw.ellipse(screen, BLACK, (
        right_eye.x + right_eye.width * 0.33,
        right_eye.y + right_eye.height * 0.3,
        right_eye.width * 0.33,
        right_eye.height * 0.4
    ))

    # Smile
    if smile:
        mouth_rect = pygame.Rect(WIDTH * 0.375, HEIGHT * 0.62, WIDTH * 0.25, HEIGHT * 0.15)
        pygame.draw.arc(screen, BLACK, mouth_rect, 3.14, 0, 6)

    # Cheeks
    pygame.draw.circle(screen, RED, (int(WIDTH * 0.275), int(HEIGHT * 0.67)), int(WIDTH * 0.02))
    pygame.draw.circle(screen, RED, (int(WIDTH * 0.725), int(HEIGHT * 0.67)), int(WIDTH * 0.02))

    # Logo bottom-right with margin
    margin = 10
    logo_x = WIDTH - logo_rect.width - margin
    logo_y = HEIGHT - logo_rect.height - margin
    screen.blit(logo, (logo_x, logo_y))

    pygame.display.flip()

# Run
start_time = time.time()
running = True

while running:
    clock.tick(60)
    elapsed = (time.time() - start_time ) % 4

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # First 3 seconds: normal smile
    if elapsed < 3:
        draw_robot(smile=True, wink=False)
    # 3–4 seconds: wink
    else:
        draw_robot(smile=True, wink=True)

pygame.quit()
sys.exit()