

import bot_log
from settings import GAME_HEIGHT, GAME_WIDTH, GAME_X1, GAME_Y1, MONITOR_HEIGHT, MONITOR_WIDTH, MONITOR_X1, MONITOR_Y1, STANDARD_HEIGHT, STANDARD_WIDTH, STANDARD_X1, STANDARD_X2, STANDARD_Y1, STANDARD_Y2

class Coord:
    standard_space:int # snippet size | 0 -> standard size
    game_space:int # full screen | 0 -> full screen size
    real_space:int # pixel space | offset -> scaled size
    monitor_space: int# pixel in monitor | 0 -> monitior size

    _REAL_X1: int
    _REAL_Y1: int
    _REAL_WIDTH: int
    _REAL_HEIGHT: int
    _REAL_X2: int
    _REAL_Y2: int

    X1: 'Coord'
    Y1: 'Coord'
    WIDTH: 'Coord'
    HEIGHT: 'Coord'
    X2: 'Coord'
    Y2: 'Coord'

    logger:bot_log.BotLogger = bot_log.BotLogger('coord', bot_log.DEBUG)

    @staticmethod
    def from_standard_x(x:int) -> 'Coord':
        c: Coord = Coord()
        c.standard_space = x
        c.game_space = Coord._standard_to_game_x(x)
        c.real_space = Coord._standard_to_real_x(x)
        c.monitor_space = Coord._standard_to_monitor_x(x)
        return c

    @staticmethod
    def from_standard_y(y:int) -> 'Coord':
        c: Coord = Coord()
        c.standard_space = y
        c.game_space = Coord._standard_to_game_y(y)
        c.real_space = Coord._standard_to_real_y(y)
        c.monitor_space = Coord._standard_to_monitor_y(y)
        return c

    @staticmethod
    def from_real_x(x:int) -> 'Coord':
        c: Coord = Coord()
        c.real_space = x
        c.standard_space = Coord._real_to_standard_x(x)
        c.game_space = Coord._standard_to_game_x(c.standard_space)
        c.monitor_space = Coord._standard_to_monitor_x(c.standard_space)
        return c

    @staticmethod
    def from_real_y(y:int) -> 'Coord':
        c: Coord = Coord()
        c.real_space = y
        c.standard_space = Coord._real_to_standard_y(y)
        c.game_space = Coord._standard_to_game_y(c.standard_space)
        c.monitor_space = Coord._standard_to_monitor_y(c.standard_space)
        return c

    @staticmethod
    def from_game_x(x:int) -> 'Coord':
        c: Coord = Coord()
        c.game_space = x
        c.standard_space = Coord._game_to_standard_x(x)
        c.real_space = Coord._standard_to_real_x(c.standard_space)
        c.monitor_space = Coord._standard_to_monitor_x(c.standard_space)
        return c

    @staticmethod
    def from_game_y(y:int) -> 'Coord':
        c: Coord = Coord()
        c.game_space = y
        c.standard_space = Coord._game_to_standard_y(y)
        c.real_space = Coord._standard_to_real_y(c.standard_space)
        c.monitor_space = Coord._standard_to_monitor_y(c.standard_space)
        return c

    @staticmethod
    def from_monitor_x(x:int) -> 'Coord':
        c: Coord = Coord()
        c.monitor_space = x
        c.standard_space = Coord._monitor_to_standard_x(x)
        c.real_space = Coord._standard_to_real_x(c.standard_space)
        c.game_space = Coord._standard_to_game_x(c.standard_space)
        return c

    @staticmethod
    def from_monitor_y(y:int) -> 'Coord':
        c: Coord = Coord()
        c.monitor_space = y
        c.standard_space = Coord._monitor_to_standard_y(y)
        c.real_space = Coord._standard_to_real_y(c.standard_space)
        c.game_space = Coord._standard_to_game_y(c.standard_space)
        return c

    @staticmethod
    def set_real_y1(y1:int) -> None:
        Coord._REAL_X1 = 0
        Coord._REAL_Y1 = y1
        Coord._REAL_HEIGHT = MONITOR_HEIGHT - 2 * Coord._REAL_Y1
        Coord._REAL_WIDTH = GAME_WIDTH * Coord._REAL_HEIGHT // GAME_HEIGHT
        Coord._REAL_X2 = Coord._REAL_X1 + Coord._REAL_WIDTH
        Coord._REAL_Y2 = Coord._REAL_Y1 + Coord._REAL_HEIGHT
        Coord.logger.debug('window dimenisions: {}x{} at ({},{})'.format(
            Coord._REAL_WIDTH,
            Coord._REAL_HEIGHT,
            Coord._REAL_X1,
            Coord._REAL_Y1
        ))
        Coord.X1 = Coord.from_standard_x(STANDARD_X1)
        Coord.Y1 = Coord.from_standard_y(STANDARD_Y1)
        Coord.WIDTH = Coord.from_standard_x(STANDARD_WIDTH)
        Coord.HEIGHT = Coord.from_standard_y(STANDARD_HEIGHT)
        Coord.X2 = Coord.from_standard_x(STANDARD_X2)
        Coord.Y2 = Coord.from_standard_y(STANDARD_Y2)

    @staticmethod
    def _convert(value:int, x1:int, w1:int, x2:int, w2:int) -> int:
        return ((value - x1) * w2 // w1) + x2

    @staticmethod
    def _standard_to_real_x(x:int) -> int:
        return Coord._convert(x, STANDARD_X1, STANDARD_WIDTH, Coord._REAL_X1, Coord._REAL_WIDTH)

    @staticmethod
    def _standard_to_real_y(y:int) -> int:
        return Coord._convert(y, STANDARD_Y1, STANDARD_HEIGHT, Coord._REAL_Y1, Coord._REAL_HEIGHT)
    
    @staticmethod
    def _real_to_standard_x(x:int) -> int:
        return Coord._convert(x, Coord._REAL_X1, Coord._REAL_WIDTH, STANDARD_X1, STANDARD_WIDTH)

    @staticmethod
    def _real_to_standard_y(y:int) -> int:
        return Coord._convert(y, Coord._REAL_Y1, Coord._REAL_HEIGHT, STANDARD_Y1, STANDARD_HEIGHT)

    @staticmethod
    def _standard_to_game_x(x:int) -> int:
        return Coord._convert(x, STANDARD_X1, STANDARD_WIDTH, GAME_X1, GAME_WIDTH)

    @staticmethod
    def _standard_to_game_y(y:int) -> int:
        return Coord._convert(y, STANDARD_Y1, STANDARD_HEIGHT, GAME_Y1, GAME_HEIGHT)

    @staticmethod
    def _game_to_standard_x(x:int) -> int:
        return Coord._convert(x, GAME_X1, GAME_WIDTH, STANDARD_X1, STANDARD_WIDTH)

    @staticmethod
    def _game_to_standard_y(y:int) -> int:
        return Coord._convert(y, GAME_Y1, GAME_HEIGHT, STANDARD_Y1, STANDARD_HEIGHT)

    @staticmethod
    def _standard_to_monitor_x(x:int) -> int:
        return Coord._convert(x, STANDARD_X1, STANDARD_WIDTH, MONITOR_X1, MONITOR_WIDTH)

    @staticmethod
    def _standard_to_monitor_y(y:int) -> int:
        return Coord._convert(y, STANDARD_Y1, STANDARD_HEIGHT, MONITOR_Y1, MONITOR_HEIGHT)

    @staticmethod
    def _monitor_to_standard_x(x:int) -> int:
        return Coord._convert(x, MONITOR_X1, MONITOR_WIDTH, STANDARD_X1, STANDARD_WIDTH)

    @staticmethod
    def _monitor_to_standard_y(y:int) -> int:
        return Coord._convert(y, MONITOR_Y1, MONITOR_HEIGHT, STANDARD_Y1, STANDARD_HEIGHT)