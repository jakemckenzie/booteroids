import pygame
from common.constants import *
from player import Player
import asteroidfield
from asteroid import Asteroid
from shot import Shot
import sys

def print_startup():
    # Starting Booteroids!
    # Starting Asteroids!
    print("Starting Booteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


def update_state(state): 
    return {"frame_count": state["frame_count"] + 1}

def draw_screen(screen, state, drawables, background, score, lives):

    screen.blit(background, (0, 0))
    
    for sprite in drawables:
        sprite.draw(screen)

    font = pygame.font.Font(None, 36)
    hud_text = f"Frame: {state['frame_count']} Score: {score} Lives: {lives}"
    text_surface = font.render(hud_text, True, (255, 0, 0))
    screen.blit(text_surface, (20, 20))
    
    pygame.display.flip()

def main():
    print_startup()
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    background_raw = pygame.image.load("assets/background.png").convert()
    background = pygame.transform.scale(background_raw, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Updatables: Contains sprites that need to run game logic (movement, state changes, physics, etc.).
    # Drawables: Contains sprites that only need to be drawn on the screen
    # Some sprites might not require an update every frame, or their update logic might be different from 
    # how they are drawn. Keeping them in separate groups allows you to call update() or draw() only on the 
    # relevant collection keeping a separation of concerns:
    # https://mzaks.medium.com/separation-of-concerns-e00f89fdc277
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    asteroidfield.AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = asteroidfield.AsteroidField()
    state = {"frame_count": 0}    

    score = 0
    lives = 3
    paused = False

    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = not paused
        

        if not paused:
            updatables.update(dt)
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collides_with(shot):
                        if asteroid.radius > ASTEROID_MIN_RADIUS * 1.5:
                            score += SCORE_LARGE
                        elif asteroid.radius > ASTEROID_MIN_RADIUS:
                            score += SCORE_MEDIUM
                        else:
                            score += SCORE_SMALL
                        asteroid.split()
                        shot.kill()

        collision_detected = False
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                collision_detected = True
                break

        if collision_detected:
            lives -= 1
            if lives > 0:
                print(f"Respawning... Lives remaining: {lives}")
                player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                player.velocity = pygame.Vector2(0, 0)
                player.rotation = 0
            else:
                print("Game Over!")
                pygame.quit()
                sys.exit()
        state = update_state(state)
        draw_screen(screen, state, drawables, background, score, lives)
        
    pygame.quit()


if __name__ == "__main__":
    main()
