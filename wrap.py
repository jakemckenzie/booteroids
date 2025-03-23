def wrap_position(position, screen_width, screen_height):
    if position.x < 0:
        position.x += screen_width
    elif position.x > screen_width:
        position.x -= screen_width
    if position.y < 0:
        position.y += screen_height
    elif position.y > screen_height:
        position.y -= screen_height
    return position