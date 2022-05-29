from enum import Enum

## SCREEN SIZE

WIDTH, HEIGHT = 1920, 1080
size = (WIDTH, HEIGHT)


##COLORS

class ColorEnum(tuple, Enum):
    BLACK = (0, 0, 0)
    BLUE = (0, 121, 150)
    BLUE_V2 = (0, 14, 71)
    WHITE = (255, 255, 255)


## OTHERS
SCALER = 30
OFFSET = 1
FPS = 30
