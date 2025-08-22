def destroy_walls(wall_healths):
    for wall_health in wall_healths:
        if wall_health <= 0:
            wall_healths.remove(wall_health)
    return wall_healths

