from enum import Enum

## SCREEN SIZE

WIDTH, HEIGHT = 800, 800
SIZE = (WIDTH, HEIGHT)


##COLORS

class ColorEnum(tuple, Enum):
    BLACK = (0, 0, 0)
    BLUE = (0, 121, 150)
    BLUE_V2 = (0, 14, 71)
    WHITE = (255, 255, 255)
    GREEN = (127, 255, 0)


## OTHERS
SCALER = 10
OFFSET = 0.5
FPS = 30
NAME = "Game Of Life"
