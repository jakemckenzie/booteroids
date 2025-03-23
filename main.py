import pygame
from constants import *
from player import Player

def print_startup():
    # Starting Booteroids!
    # Starting Asteroids!
    print("Starting Booteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


def update_state(state):
    return {"frame_count": state["frame_count"] + 1}

def draw_screen(screen, state, player):

    screen.fill("black")
    player.draw(screen)

    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Frame: {state['frame_count']}", True, (255, 255, 255))
    screen.blit(text_surface, (20, 20))
    
    pygame.display.flip()

def main():
    print_startup()
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    state = {"frame_count": 0}
    
    dt = 0    

    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        player.update(dt)
        state = update_state(state)
        draw_screen(screen, state, player)
        

    pygame.quit()


if __name__ == "__main__":
    main()
