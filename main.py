import random

import pygame
from sys import exit

pygame.init()
my_screen = pygame.display.set_mode((650, 500))  # display surface
pygame.display.set_caption("My Little Pony")  # window title
clock = pygame.time.Clock()  # frames per second control

plays_now = True
twilight = False
count = 0


# font = pygame.font.Font(None, 30)
# text = font.render("hi ", True, "Black")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []

        if plays_now:

            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-001-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-002-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-003-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-004-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-005-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-006-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-007-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-008-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-009-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-010-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-009-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-008-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-007-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-006-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-005-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-004-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-003-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-002-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-001-removebg-preview (1).png'), (150, 150)))
        else:
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_01.png'), (100, 100)))
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_02.png'), (100, 100)))
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_03.png'), (100, 100)))
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_04.png'), (100, 100)))
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_05.png'), (100, 100)))
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_06.png'), (100, 100)))
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_07.png'), (100, 100)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def set_rect(self, x, y):
        self.rect.topleft = [x, y]

    def update(self):

        self.current_sprite += .3
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


heights = random.randint(150, 400)
width = 40
obstacle_change = -4
obstacle_x = 0

def obstacles(height):
    pygame.draw.rect(my_screen, (200, 200, 200), (obstacle_x, 0, width, height))
    pygame.draw.rect(my_screen, (200, 200, 200), (obstacle_x, 500, width, 500-50-height))

def home():
    global plays_now
    bg_img = pygame.image.load('pics/start_img.png')
    bg_img = pygame.transform.scale(bg_img, (650, 500))
    chars_img = pygame.image.load('pics/ch.png')
    chars_img = pygame.transform.scale(chars_img, (300, 350))

    moving_sprite = pygame.sprite.Group()
    player = Sprite(350, 300)
    moving_sprite.add(player)

    while True:
        for event in pygame.event.get():  # to keep
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        my_screen.blit(bg_img, (0, 0))
        my_screen.blit(chars_img, (180, 300))
        moving_sprite.draw(my_screen)
        moving_sprite.update()

        if pygame.mouse.get_pressed()[0]:
            plays_now = False
            break

        clock.tick(60)
        pygame.display.update()


def start():
    global obstacle_x, obstacle_change, heights, width
    x = 0
    y = 0
    default_img = (650, 500)
    first_stage = pygame.image.load('pics/start_img.png')
    first_stage = pygame.transform.scale(first_stage, default_img)

    moving_sprite = pygame.sprite.Group()
    player = Sprite(30, 30)
    moving_sprite.add(player)

    while True:
        for event in pygame.event.get():  # to keep
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        move = pygame.key.get_pressed()
        if move[pygame.K_LEFT] and x > 0:
            x -= 5
        if move[pygame.K_RIGHT] and x < 650 - 50:
            x += 5
        if move[pygame.K_UP] and y > 0:
            y -= 5
        if move[pygame.K_DOWN] and y < 500 - 50:
            y += 5

        obstacle_x += obstacle_change
        if obstacle_x >= 660:
            obstacle_x = 0
        obstacles(heights)

        my_screen.blit(first_stage, (0, 0))
        player.set_rect(x, y)
        moving_sprite.draw(my_screen)
        moving_sprite.update()

        clock.tick(60)

        pygame.display.update()


# image surface

# bird = pygame.image.load('no.gif')
# bird = pygame.transform.scale(bird, DEFAULT_IMAGE_SIZE)


# love = pygame.transform.scale(love, DEFAULT_IMAGE_SIZE)
# pygame.image.load(r'C:\Users\student\PycharmProjects\pythonProject\pics\night sky.png')
# love = pygame.transform.scale(love, DEFAULT_IMAGE_SIZE)

def main():
    home()
    start()


if __name__ == "__main__":
    main()







