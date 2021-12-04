import dataclasses
from enum import Enum


class Direction(str, Enum):
    up = "up"
    down = "down"
    forward = "forward"


@dataclasses.dataclass
class Vector:
    direction: Direction
    magnitude: int


@dataclasses.dataclass
class Coordinates:
    depth: int = 0
    horizontal: int = 0
    aim: int = 0
