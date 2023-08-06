import pygame
import random
import os

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird!")

BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'background.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

FPS = 60
BIRD_WIDTH = BIRD_HEIGHT = 40
PIPE_WIDTH = 100
SPACE_BETWEEN_PIPES = 175
BIRD_DROP_VELOCITY = 5
PIPE_VELOCITY = 7
BIRD_JUMP = 15


BIRD_IMAGE = pygame.image.load(os.path.join('Assets', 'bird.png'))
BIRD = pygame.transform.scale(BIRD_IMAGE, (BIRD_WIDTH, BIRD_HEIGHT))

PIPE_TOP_IMAGE = pygame.image.load(os.path.join('Assets', 'pipe_top.png'))
PIPE_TOP = pygame.transform.scale(PIPE_TOP_IMAGE, (PIPE_WIDTH, HEIGHT)) 

PIPE_BOTTOM_IMAGE = pygame.image.load(os.path.join('Assets', 'pipe_bottom.png'))
PIPE_BOTTOM = pygame.transform.scale(PIPE_BOTTOM_IMAGE, (PIPE_WIDTH, HEIGHT))

class Bird:
    def __init__(self):
        self.rect = BIRD.get_rect(center = (WIDTH / 2, HEIGHT / 2))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -BIRD_JUMP)
        self.rect.move_ip(0, BIRD_DROP_VELOCITY)

    def draw(self, win):
        win.blit(BIRD, self.rect)

class PipePair:
    def __init__(self):
        height = random.randint(50, HEIGHT - 50 - SPACE_BETWEEN_PIPES)
        self.top = PIPE_TOP.get_rect(midbottom = (WIDTH, height))
        self.bottom = PIPE_BOTTOM.get_rect(midtop = (WIDTH, height + SPACE_BETWEEN_PIPES))

    def move(self):
        self.top.move_ip(-PIPE_VELOCITY, 0)
        self.bottom.move_ip(-PIPE_VELOCITY, 0)

    def draw(self, win):
        win.blit(PIPE_TOP, self.top)
        win.blit(PIPE_BOTTOM, self.bottom)

def main():
    bird = Bird()
    pipes = [PipePair()]

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not run:
            break

        bird.move()
        for pipe in pipes:
            pipe.move()
            if bird.rect.colliderect(pipe.top) or bird.rect.colliderect(pipe.bottom):
                run = False
                break

        if pipes[0].top.right < 0:
            pipes.pop(0)
            pipes.append(PipePair())

        WIN.blit(BACKGROUND, (0, 0))
        bird.draw(WIN)
        for pipe in pipes:
            pipe.draw(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
