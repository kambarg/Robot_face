import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Animated Emotions Face")
clock = pygame.time.Clock()

# Colors
YELLOW = (255, 223, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Current emotion
emotions = ["happy", "sad", "surprised"]
current_emotion = "happy"
last_change_time = time.time()

def draw_face(emotion):
    screen.fill(WHITE)

    center_x, center_y = 250, 250

    # Draw face
    pygame.draw.circle(screen, YELLOW, (center_x, center_y), 150)
    pygame.draw.circle(screen, BLACK, (center_x - 50, center_y - 50), 15)  # Left eye
    pygame.draw.circle(screen, BLACK, (center_x + 50, center_y - 50), 15)  # Right eye
    # pygame.draw.ellipse(screen, BLACK, (center_x - 50, center_y - 60, 40, 25)) 
    # pygame.draw.ellipse(screen, BLACK, (center_x + 50, center_y - 60, 40, 25))
    
    # Draw mouth based on emotion
    if emotion == "sad":
        pygame.draw.arc(screen, BLACK, (center_x - 60, center_y - 20, 120, 80), 0, 3.14, 5)
    elif emotion == "happy":
        pygame.draw.arc(screen, BLACK, (center_x - 60, center_y + 20, 120, 80), 3.14, 0, 5)
    elif emotion == "surprised":
        pygame.draw.circle(screen, BLACK, (center_x, center_y + 50), 20)

    # Draw emotion text
    font = pygame.font.SysFont("Arial", 30)
    text = font.render(f"{emotion.upper()}", True, BLACK)
    screen.blit(text, (180, 420))

    pygame.display.flip()

# Main loop
running = True
while running:
    clock.tick(60)
    now = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Change emotion every 3 seconds
    if now - last_change_time > 3:
        current_emotion = random.choice(emotions)
        last_change_time = now

    draw_face(current_emotion)

pygame.quit()
sys.exit()