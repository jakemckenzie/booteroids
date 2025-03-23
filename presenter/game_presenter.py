class GamePresenter:
  def present(self, score, lives, game_over):
    data = {}
    
    data['score_text'] = f"Score: {score}"
    data['lives_text'] = f"Lives: {lives}"
    
    if game_over:
      data['game_over_text'] = "GAME OVER - Press ESC to quit"
    else:
      data['game_over_text'] = ""
    return data
