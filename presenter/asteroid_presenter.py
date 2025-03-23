class AsteroidPresenter:
  def present(self, asteroids):
    asteroid_draw_data = []

    for asteroid in asteroids:
      asteroid_draw_data.append((int(asteroid.x), int(asteroid.y), asteroid.radius))

    return asteroid_draw_data
