import pygame
import random
from booteroids.common import constants

class AsteroidView:
  def draw_all(self, screen, asteroids_data):
    for (x, y, radius) in asteroids_data:
      pygame.draw.circle(screen, constants.GRAY, (x, y), radius, width=0)