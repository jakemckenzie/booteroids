import pygame
from constants import *
from player import Player
import asteroidfield
from asteroid import Asteroid
import sys

def print_startup():
    # Starting Booteroids!
    # Starting Asteroids!
    print("Starting Booteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


def update_state(state): 
    return {"frame_count": state["frame_count"] + 1}

def draw_screen(screen, state, drawables):

    screen.fill("black")
    
    for sprite in drawables:
        sprite.draw(screen)

    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Frame: {state['frame_count']}", True, (255, 255, 255))
    screen.blit(text_surface, (20, 20))
    
    pygame.display.flip()

def main():
    print_startup()
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Updatables: Contains sprites that need to run game logic (movement, state changes, physics, etc.).
    # Drawables: Contains sprites that only need to be drawn on the screen
    # Some sprites might not require an update every frame, or their update logic might be different from 
    # how they are drawn. Keeping them in separate groups allows you to call update() or draw() only on the 
    # relevant collection keeping a separation of concerns:
    # https://mzaks.medium.com/separation-of-concerns-e00f89fdc277
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    asteroidfield.AsteroidField.containers = (updatables,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = asteroidfield.AsteroidField()
    state = {"frame_count": 0}    

    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        updatables.update(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()
        
        
        player.update(dt)
        state = update_state(state)

        draw_screen(screen, state, drawables)
        
    pygame.quit()


if __name__ == "__main__":
    main()
