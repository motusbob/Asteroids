# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    timer = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shot, updatable, drawable)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        dt = timer.tick(60) / 1000
        #player.update(dt)
        #player.draw(screen)
        updatable.update(dt)
        for aste in asteroid:
            if aste.check_collision(player):
                print("Game over!")
                sys.exit()
        for aste in asteroid:
            for sh in shot:
                if aste.check_collision(sh):
                    aste.split()
                    sh.kill()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        



if __name__ == "__main__":
    main()
