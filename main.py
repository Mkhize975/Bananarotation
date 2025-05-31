import pygame

# initialize pygame
pygame.init()

# set the size of the window
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Spinning Banana")

# load the banana image
banana_img = pygame.image.load("banana.png")

# create a variable to hold the banana's position (changed from tuple to list)
banana_pos = [200, 0]

# set the speed of the banana's movement
banana_speed = 5

# create a variable to hold the banana's rotation angle
banana_angle = 0

# create a variable to control the banana's rotation direction
banana_rotation = 1

# create a variable to control the banana's rotation speed
banana_rotation_speed = 2

# create a loop to update the banana's position and rotation
running = True
while running:
    # clear the screen
    screen.fill((255, 255, 255))

    # update the banana's position
    banana_pos[1] += banana_speed

    # update the banana's rotation angle
    banana_angle += banana_rotation * banana_rotation_speed

    # rotate the banana image
    rotated_banana = pygame.transform.rotate(banana_img, banana_angle)

    # get the rectangle of the rotated image
    rotated_rect = rotated_banana.get_rect()

    # set the position of the rotated rectangle to the banana's position
    rotated_rect.center = banana_pos

    # draw the rotated banana on the screen
    screen.blit(rotated_banana, rotated_rect)

    # update the screen
    pygame.display.update()

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# quit pygame
pygame.quit()
