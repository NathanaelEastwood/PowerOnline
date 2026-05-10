import pygame

from utils import expand_coords, spawnStartingPieces
from fixtures import tiles
pygame.init()

# Screen setup
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tile Board")

clock = pygame.time.Clock()
running = True

# Font for displaying text
font = pygame.font.SysFont(None, 36)

selected_grid = ""

white_pieces = spawnStartingPieces((255, 255, 255), "WHQ")
red_pieces = spawnStartingPieces((255, 0, 0), "RHQ")
yellow_pieces = spawnStartingPieces((255, 255, 0), "YHQ")
black_pieces = spawnStartingPieces((0, 0, 0), "BHQ")
all_pieces = white_pieces + red_pieces + yellow_pieces + black_pieces

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse click handling
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for tile in tiles:
                if tile["rect"].collidepoint(mouse_pos):
                    selected_grid = f"{tile['type']} Tile - Grid Ref: {tile['grid']}"
                    print(selected_grid)

    # Clear screen
    screen.fill((30, 30, 30))

    # Draw tiles
    for tile in tiles:
        pygame.draw.rect(screen, tile["color"], tile["rect"])

        # Draw tile border
        pygame.draw.rect(screen, (0, 0, 0), tile["rect"], 3)

        # Draw tile name
        text_surface = font.render(tile["type"], True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=tile["rect"].center)
        screen.blit(text_surface, text_rect)

    # Display selected tile/grid reference
    info_text = font.render(selected_grid, True, (255, 255, 255))
    screen.blit(info_text, (1000, 1000))

# Draw pieces
    for piece in all_pieces:

        tile = next((t for t in tiles if t["grid"] == piece["position"]), None)

        if tile is None:
            continue

        rect = tile["rect"]

        # Offset based on unit type
        offsets = {
            "Infantry": 10,
            "Fighter": 40,
            "Tank": 70,
            "Destroyer": 100
        }

        offset_y = offsets.get(piece["type"], 0)

        piece_x = rect.x + 10
        piece_y = rect.y + offset_y

        # Unit marker
        pygame.draw.circle(screen, piece["color"], (piece_x + 12, piece_y + 12), 12)

        # Unit text
        label = f"{piece['type']} x{piece['count']}"

        text_surface = font.render(label, True, (255, 255, 255))

        screen.blit(text_surface, (piece_x + 30, piece_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()