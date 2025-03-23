"""
View layer for Game Flow.
Manages the main game loop, processes user input, and delegates rendering to specific domain views.
"""
import pygame
from booteroids.common import constants
from booteroids.interactor.game_interactor import GameInteractor
from booteroids.presenter.player_presenter import PlayerPresenter
from booteroids.presenter.asteroid_presenter import AsteroidPresenter
from booteroids.presenter.shot_presenter import ShotsPresenter
from booteroids.presenter.game_presenter import GamePresenter
from booteroids.view.player_view import PlayerView
from booteroids.view.asteroid_view import AsteroidView
from booteroids.view.shot_view import ShotsView

class GameView:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Booteroids")
    self.clock = pygame.time.Clock()
    # Initialize the interactor and presenters
    self.game_interactor = GameInteractor()
    self.player_presenter = PlayerPresenter()
    self.asteroid_presenter = AsteroidPresenter()
    self.shot_presenter = ShotsPresenter()
    self.game_presenter = GamePresenter()
    # Initialize the view components for rendering
    self.player_view = PlayerView()
    self.asteroid_view = AsteroidView()
    self.shots_view = ShotsView()
    # Font for HUD text (score, lives, etc.)
    self.font = pygame.font.Font(None, 36)

    

  def run(self):
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            running = False
          elif event.key == pygame.K_SPACE:
            self.game_interactor.fire_player_shot()

      keys = pygame.key.get_pressed()

      if keys[pygame.K_d]:
        self.game_interactor.player_interactor.rotate_left()
      if keys[pygame.K_a]:
        self.game_interactor.player_interactor.rotate_right()
      if keys[pygame.K_w]:
        self.game_interactor.player_interactor.thrust()

      self.game_interactor.update()

      self.screen.fill(constants.BLACK)

      player_poly = self.player_presenter.present(self.game_interactor.player_interactor.player)
      asteroid_data = self.asteroid_presenter.present(self.game_interactor.asteroid_interactor.asteroids)
      shots_polygons = self.shot_presenter.present(self.game_interactor.shot_interactor.shots)
      hud_texts = self.game_presenter.present(self.game_interactor.score, self.game_interactor.lives, self.game_interactor.game_over)

      self.player_view.draw(self.screen, player_poly)
      self.asteroid_view.draw_all(self.screen, asteroid_data)
      self.shots_view.draw_all(self.screen, shots_polygons)

      score_surf = self.font.render(hud_texts['score_text'], True, constants.WHITE)
      lives_surf = self.font.render(hud_texts['lives_text'], True, constants.WHITE)

      self.screen.blit(score_surf, (10, 10))
      self.screen.blit(lives_surf, (10, 40))

      if self.game_interactor.game_over:
        game_over_surf = self.font.render(hud_texts['game_over_text'], True, constants.WHITE)
            
        rect = game_over_surf.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2))
        self.screen.blit(game_over_surf, rect)

      pygame.display.flip()
      self.clock.tick(constants.FPS)
    pygame.quit()

if __name__ == "__main__":
    GameView().run()
