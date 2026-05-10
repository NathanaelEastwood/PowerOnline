import pygame

from utils import expand_coords

TILE_SIZE = 100

color_map = {
    "Grass": (34, 177, 76),
    "Water": (0, 162, 232),
    "Snow": (240, 240, 240),
    "Mountain": (120, 120, 120),
    "Forest": (0, 100, 0)
}
tiles = [
    {"type": "HQ", "color": color_map["Forest"], "grid": "YHQ", "rect": pygame.Rect(*expand_coords(0, 0), TILE_SIZE, TILE_SIZE)},
    {"type": "Sealane", "color": color_map["Water"], "grid": "S6", "rect": pygame.Rect(*expand_coords(1, 0), TILE_SIZE * 3, TILE_SIZE)},
    {"type": "Island", "color": color_map["Mountain"], "grid": "N", "rect": pygame.Rect(*expand_coords(4, 0), TILE_SIZE, TILE_SIZE)},
    {"type": "Sealane", "color": color_map["Water"], "grid": "S7", "rect": pygame.Rect(*expand_coords(5, 0), TILE_SIZE * 3, TILE_SIZE)},
    {"type": "HQ", "color": color_map["Forest"], "grid": "BHQ", "rect": pygame.Rect(*expand_coords(8, 0), TILE_SIZE, TILE_SIZE)},

    {"type": "Sealane", "color": color_map["Water"], "grid": "S5", "rect": pygame.Rect(*expand_coords(0, 1), TILE_SIZE, TILE_SIZE * 3)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "Y8", "rect": pygame.Rect(*expand_coords(1, 1), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "Y6", "rect": pygame.Rect(*expand_coords(2, 1), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "Y3", "rect": pygame.Rect(*expand_coords(3, 1), TILE_SIZE, TILE_SIZE)},
    {"type": "Sealane", "color": color_map["Water"], "grid": "S1", "rect": pygame.Rect(*expand_coords(4, 1), TILE_SIZE, TILE_SIZE * 3)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "B5", "rect": pygame.Rect(*expand_coords(5, 1), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "B7", "rect": pygame.Rect(*expand_coords(6, 1), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "B8", "rect": pygame.Rect(*expand_coords(7, 1), TILE_SIZE, TILE_SIZE)},
    {"type": "Sealane", "color": color_map["Water"], "grid": "S8", "rect": pygame.Rect(*expand_coords(8, 1), TILE_SIZE, TILE_SIZE * 3)},

    {"type": "Mainland", "color": color_map["Grass"], "grid": "Y7", "rect": pygame.Rect(*expand_coords(1, 2), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "Y4", "rect": pygame.Rect(*expand_coords(2, 2), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "Y1", "rect": pygame.Rect(*expand_coords(3, 2), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "B2", "rect": pygame.Rect(*expand_coords(5, 2), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "B4", "rect": pygame.Rect(*expand_coords(6, 2), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "B6", "rect": pygame.Rect(*expand_coords(7, 2), TILE_SIZE, TILE_SIZE)},

    {"type": "Mainland", "color": color_map["Grass"], "grid": "Y5", "rect": pygame.Rect(*expand_coords(1, 3), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "Y2", "rect": pygame.Rect(*expand_coords(2, 3), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "Y0", "rect": pygame.Rect(*expand_coords(3, 3), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "B0", "rect": pygame.Rect(*expand_coords(5, 3), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "B1", "rect": pygame.Rect(*expand_coords(6, 3), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "B3", "rect": pygame.Rect(*expand_coords(7, 3), TILE_SIZE, TILE_SIZE)},

    {"type": "Island", "color": color_map["Mountain"], "grid": "W", "rect": pygame.Rect(*expand_coords(0, 4), TILE_SIZE, TILE_SIZE)},
    {"type": "Sealane", "color": color_map["Water"], "grid": "S4", "rect": pygame.Rect(*expand_coords(1, 4), TILE_SIZE * 3, TILE_SIZE)},
    {"type": "Island", "color": color_map["Mountain"], "grid": "X", "rect": pygame.Rect(*expand_coords(4, 4), TILE_SIZE, TILE_SIZE)},
    {"type": "Sealane", "color": color_map["Water"], "grid": "S2", "rect": pygame.Rect(*expand_coords(5, 4), TILE_SIZE * 3, TILE_SIZE)},
    {"type": "Island", "color": color_map["Mountain"], "grid": "E", "rect": pygame.Rect(*expand_coords(8, 4), TILE_SIZE, TILE_SIZE)},

    {"type": "Sealane", "color": color_map["Water"], "grid": "S12", "rect": pygame.Rect(*expand_coords(0, 5), TILE_SIZE, TILE_SIZE * 3)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "R3", "rect": pygame.Rect(*expand_coords(1, 5), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "R1", "rect": pygame.Rect(*expand_coords(2, 5), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "R0", "rect": pygame.Rect(*expand_coords(3, 5), TILE_SIZE, TILE_SIZE)},
    {"type": "Sealane", "color": color_map["Water"], "grid": "S3", "rect": pygame.Rect(*expand_coords(4, 5), TILE_SIZE, TILE_SIZE * 3)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "W0", "rect": pygame.Rect(*expand_coords(5, 5), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "W2", "rect": pygame.Rect(*expand_coords(6, 5), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "W5", "rect": pygame.Rect(*expand_coords(7, 5), TILE_SIZE, TILE_SIZE)},
    {"type": "Sealane", "color": color_map["Water"], "grid": "S9", "rect": pygame.Rect(*expand_coords(8, 5), TILE_SIZE, TILE_SIZE * 3)},

    {"type": "Mainland", "color": color_map["Grass"], "grid": "R6", "rect": pygame.Rect(*expand_coords(1, 6), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "R4", "rect": pygame.Rect(*expand_coords(2, 6), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "R2", "rect": pygame.Rect(*expand_coords(3, 6), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "W1", "rect": pygame.Rect(*expand_coords(5, 6), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "W4", "rect": pygame.Rect(*expand_coords(6, 6), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "W7", "rect": pygame.Rect(*expand_coords(7, 6), TILE_SIZE, TILE_SIZE)},

    {"type": "Mainland", "color": color_map["Grass"], "grid": "R8", "rect": pygame.Rect(*expand_coords(1, 7), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "R7", "rect": pygame.Rect(*expand_coords(2, 7), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "R5", "rect": pygame.Rect(*expand_coords(3, 7), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "W3", "rect": pygame.Rect(*expand_coords(5, 7), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "W6", "rect": pygame.Rect(*expand_coords(6, 7), TILE_SIZE, TILE_SIZE)},
    {"type": "Mainland", "color": color_map["Grass"], "grid": "W8", "rect": pygame.Rect(*expand_coords(7, 7), TILE_SIZE, TILE_SIZE)},

    {"type": "HQ", "color": color_map["Forest"], "grid": "RHQ", "rect": pygame.Rect(*expand_coords(0, 8), TILE_SIZE, TILE_SIZE)},
    {"type": "Sealane", "color": color_map["Water"], "grid": "S11", "rect": pygame.Rect(*expand_coords(1, 8), TILE_SIZE * 3, TILE_SIZE)},
    {"type": "Island", "color": color_map["Mountain"], "grid": "S", "rect": pygame.Rect(*expand_coords(4, 8), TILE_SIZE, TILE_SIZE)},
    {"type": "Sealane", "color": color_map["Water"], "grid": "S10", "rect": pygame.Rect(*expand_coords(5, 8), TILE_SIZE * 3, TILE_SIZE)},
    {"type": "HQ", "color": color_map["Forest"], "grid": "WHQ", "rect": pygame.Rect(*expand_coords(8, 8), TILE_SIZE, TILE_SIZE)},

    {'type': 'Reserve', 'color': color_map["Snow"], 'grid': 'YR', 'rect': pygame.Rect(*expand_coords(10, 0), TILE_SIZE, TILE_SIZE)},
    {'type': 'Reserve', 'color': color_map["Snow"], 'grid': 'BR', 'rect': pygame.Rect(*expand_coords(11, 0), TILE_SIZE, TILE_SIZE)},
    {'type': 'Reserve', 'color': color_map["Snow"], 'grid': 'RR', 'rect': pygame.Rect(*expand_coords(10, 1), TILE_SIZE, TILE_SIZE)},
    {'type': 'Reserve', 'color': color_map["Snow"], 'grid': 'WR', 'rect': pygame.Rect(*expand_coords(11, 1), TILE_SIZE, TILE_SIZE)},
]

pieces = [
    {'type': 'Infantry', 'power': 2, 'ms': 2, 'tier': 1, 'area': 'Land', 'Upgrade': 'Regiment'},
    {'type': 'Tank', 'power': 3, 'ms': 3, 'tier': 1, 'area': 'Land', 'Upgrade': 'Heavy Tank'},
    {'type': 'Fighter', 'power': 5, 'ms': 5, 'tier': 1, 'area': 'Air', 'Upgrade': 'Bomber'},
    {'type': 'Destroyer', 'power': 10, 'ms': 1, 'tier': 1, 'area': 'Sea', 'Upgrade': 'Cruiser'},

    {'type': 'Regiment', 'power': 20, 'ms': 2, 'tier': 2, 'area': 'Land'},
    {'type': 'Heavy Tank', 'power': 30, 'ms': 3, 'tier': 2, 'area': 'Land'},
    {'type': 'Bomber', 'power': 25, 'ms': 5, 'tier': 2, 'area': 'Air'},
    {'type': 'Cruiser', 'power': 50, 'ms': 1, 'tier': 2, 'area': 'Sea'},

    {'type': 'Mega Missile', 'power': 1000, 'ms': 1000, 'tier': 2, 'area': 'Air'}
]