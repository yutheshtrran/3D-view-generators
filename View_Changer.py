#Quest 08
#21/ENG/009 A.HARISHAN
#21/ENG/131 S.YUTHESHTRRAN
#21/ENG/132 S.GEERTHIGA#

import pygame
import random
import math

# Define the characters and their 2D representations
characters = {
    '0': [
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111'
    ],
    '1': [
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111',
                            '11111'
    ],
    '2': [
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '11111          ',
                    '11111          ',
                    '11111          ',
                    '11111          ',
                    '11111          ',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111'
    ],
    '3': [
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111'
    ],
    '4': [
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111'
    ],
    '5': [
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '11111          ',
                    '11111          ',
                    '11111          ',
                    '11111          ',
                    '11111          ',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111'

    ],
    '6': [
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '11111          ',
                    '11111          ',
                    '11111          ',
                    '11111          ',
                    '11111          ',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111'
    ],
    '7': [
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
    ],
    '8': [
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',

    ],
    '9': [
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '11111     11111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '          11111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
                    '111111111111111',
    ]
}

# Define the colors
background_color = (0, 0, 0)  # Black
line_color = (255, 255, 255)  # Default color for lines

# Define the character colors
character_colors = {
    '0': (255, 0, 0),    # Red
    '1': (0, 255, 0),    # Green
    '2': (0, 0, 255),    # Blue
    '3': (255, 255, 0),  # Yellow
    '4': (255, 0, 255),  # Magenta
    '5': (0, 255, 255),  # Cyan
    '6': (255, 128, 0),  # Orange
    '7': (128, 0, 255),  # Purple
    '8': (128, 128, 128),  # Gray
    '9': (255, 255, 255)  # White
}

# Initialize pygame
pygame.init()

# Define the window size
window_w = 800
window_h = 600

# Create the window
window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("3D Number Animation")

# Define the colors
background_color = (0, 0, 0)  # Black
line_color = (255, 255, 255)  # White

# Define the rotation speeds
r_speed_x = random.uniform(0.01, 0.05)
r_speed_y = random.uniform(0.01, 0.05)
r_speed_z = random.uniform(0.01, 0.05)

# Choose a random character
# current_character = random.choice(list(characters.keys()))

# Getting user input
current_character = input("Enter numerical value between 0 and 9 : ")

# Define the initial rotation angles
angle_x = 0
angle_y = 0
angle_z = 0

# Main game loop
running = True
paused = False
clock = pygame.time.Clock()

while running:
    if paused:
        current_character = input("Enter numerical value between 0 and 9 : ")
        paused = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_RETURN:
                current_character = input("Enter numerical value between 0 and 9 : ")
                angle_x = 0
                angle_y = 0
                angle_z = 0

    if not paused:
        # Clear the screen
        window.fill(background_color)

        # Rotate the 2D character and draw the 3D representation
        for i, line in enumerate(characters[current_character]):
            for j, char in enumerate(line):
                if char == '1':
                    # Calculate the 3D coordinates based on the rotation angles
                    x = j - len(line) / 2
                    y = i - len(characters[current_character]) / 2
                    z = 0

                    # Rotate around the x-axis
                    y_rotated = y * math.cos(angle_x) - z * math.sin(angle_x)
                    z_rotated = y * math.sin(angle_x) + z * math.cos(angle_x)

                    # Rotate around the y-axis
                    x_rotated = x * math.cos(angle_y) + z_rotated * math.sin(angle_y)
                    z_rotated = -x * math.sin(angle_y) + z_rotated * math.cos(angle_y)

                    # Rotate around the z-axis
                    x_rotated_final = x_rotated * math.cos(angle_z) - y_rotated * math.sin(angle_z)
                    y_rotated_final = x_rotated * math.sin(angle_z) + y_rotated * math.cos(angle_z)

                    # Convert the 3D coordinates to 2D screen coordinates
                    scale = 10
                    x_screen = int(x_rotated_final * scale + window_w / 2)
                    y_screen = int(y_rotated_final * scale + window_h / 2)

                    # Get the color for the character
                    color = character_colors[current_character]

                    # Draw the point with color
                    pygame.draw.line(window, color, (x_screen, y_screen), (x_screen+20, y_screen+20))

        # Update the rotation angles
        angle_x += r_speed_x
        angle_y += r_speed_y
        angle_z += r_speed_z

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the program
pygame.quit()