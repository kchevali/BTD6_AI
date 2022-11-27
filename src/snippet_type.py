from coord import Coord
from snippet_sel_type import SnippetSelType

class SnippetType:
    name:str
    x1: Coord
    y1: Coord
    x2: Coord
    y2: Coord

    def __init__(self, name:str, sel:SnippetSelType, x1:Coord, y1:Coord, x2:Coord, y2:Coord) -> None:
        self.name = name
        self.sel = sel
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2