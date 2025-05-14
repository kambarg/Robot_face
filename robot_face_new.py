import pygame
import time
import sys
import cv2
import numpy as np
import platform

# Init
pygame.init()

# Initialize webcam with better error handling
def init_camera():
    # Try different camera indices
    for index in range(2):  # Try first two camera indices
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            return cap
        cap.release()
    
    # If running in WSL, try accessing the camera through DirectShow
    if platform.system() == "Linux" and "microsoft" in platform.release().lower():
        print("WSL detected. Trying DirectShow access...")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if cap.isOpened():
            return cap
    
    print("Error: Could not open webcam. Please ensure:")
    print("1. Your webcam is properly connected")
    print("2. If using WSL, make sure you have WSL2 and enabled camera access")
    print("3. Try running this script directly in Windows Python environment")
    sys.exit(1)

# Initialize camera
cap = init_camera()

# Load face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

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

def draw_robot(smile=True, wink=False, face_x=None):
    screen.fill((30, 30, 30))  # Background

    # Proportions based on screen size
    face_rect = pygame.Rect(WIDTH * 0.2, HEIGHT * 0.08, WIDTH * 0.6, HEIGHT * 0.75)
    pygame.draw.rect(screen, GRAY, face_rect, border_radius=40)
    pygame.draw.rect(screen, DARK_GRAY, face_rect, 6, border_radius=40)

    # Forehead panel
    forehead_rect = pygame.Rect(WIDTH * 0.31, HEIGHT * 0.10, WIDTH * 0.38, HEIGHT * 0.08)
    pygame.draw.rect(screen, BLUE, forehead_rect, border_radius=10)
    pygame.draw.rect(screen, WHITE, forehead_rect, 3, border_radius=10)

    # Base eye positions
    left_eye = pygame.Rect(WIDTH * 0.31, HEIGHT * 0.32, WIDTH * 0.075, HEIGHT * 0.22)
    right_eye = pygame.Rect(WIDTH * 0.59, HEIGHT * 0.32, WIDTH * 0.075, HEIGHT * 0.22)

    # Adjust eye positions based on face position
    if face_x is not None:
        # Calculate eye offset based on face position (max offset: 20% of eye width)
        max_offset = left_eye.width * 0.2
        # Map face_x from 0-1 to -max_offset to max_offset
        offset = (face_x - 0.5) * 2 * max_offset
        left_eye.x += offset
        right_eye.x += offset

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
face_detected = False
face_detected_time = 0
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Variables for robot's reaction
    current_face_x = None
    current_face_detected = len(faces) > 0

    # Process detected faces
    if current_face_detected:
        if not face_detected:
            face_detected = True
            face_detected_time = time.time()
        
        # Use the first detected face for eye tracking
        x, y, w, h = faces[0]
        # Calculate relative x position of face (0 to 1)
        current_face_x = (x + w/2) / frame.shape[1]
    else:
        face_detected = False

    # Robot's reaction logic
    if face_detected:
        elapsed_since_detection = time.time() - face_detected_time
        # Wink briefly when face is first detected
        if elapsed_since_detection < 1.0:
            draw_robot(smile=True, wink=True, face_x=current_face_x)
        else:
            draw_robot(smile=True, wink=False, face_x=current_face_x)
    else:
        # Default expression when no face is detected
        draw_robot(smile=False, wink=False, face_x=None)

# Cleanup
cap.release()
pygame.quit()
sys.exit()