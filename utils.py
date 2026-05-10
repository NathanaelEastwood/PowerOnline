def expand_coords(x, y):
    return (x * 100, y * 100)

def spawnStartingPieces(color, HQ_grid):
    return [
        {'type': 'Infantry', 'color': color, 'position': HQ_grid, 'count': 2},
        {'type': 'Fighter', 'color': color, 'position': HQ_grid, 'count': 2},
        {'type': 'Tank', 'color': color, 'position': HQ_grid, 'count': 2},
        {'type': 'Destroyer', 'color': color, 'position': HQ_grid, 'count': 2},
    ]