import mss # type:ignore
import bot_log, os
import numpy as np
from numpy.typing import NDArray #type:ignore
from bot_image import BotImage
from coord import Coord
from settings import GAME_HEIGHT

class Snippet:
    logger:bot_log.BotLogger = bot_log.BotLogger('snippet', bot_log.DEBUG)

    def __init__(self) -> None:
        self.sct = mss.mss()
        self.update_frame()
    
    def update_frame(self) -> None:
        # Snippet.logger.debug('updating frame')
        img: BotImage = self.full_page_shot()
        data: NDArray[np.uint8] = img.np_data
        pixel:int = 0
        while pixel < GAME_HEIGHT and data[pixel][pixel][1] == 0 and data[pixel][pixel][2] == 0 and data[pixel][pixel][3] == 0:
            pixel += 1
        Coord.set_real_y1(pixel)
    
    def full_page_shot(self) -> BotImage:
        monitor = self.sct.monitors[1]
        img: NDArray[np.uint8] = np.array(self.sct.grab(monitor))
        return BotImage.from_array(img[...,::-1])
    
    def shot_crop(self, x1:Coord, y1:Coord, x2:Coord, y2:Coord) -> BotImage:
        img: NDArray[np.uint8] = np.array(self.sct.grab((x1.real_space, y1.real_space, x2.real_space, y2.real_space)))
        return BotImage.from_array(img[:,:,[2,1,0]]) # type:ignore
    
    def shot(self) -> BotImage:
        return self.shot_crop(Coord.X1, Coord.Y1, Coord.X2, Coord.Y2)
    
    def __del__(self) -> None:
        self.sct.close()

def main() -> None:
    snpt: Snippet = Snippet()
    full: BotImage = snpt.full_page_shot()

    if not os.path.isdir("tmp"): os.mkdir("tmp")

    full.save('tmp/full_page.png')
    low_res_path:str = 'tmp/full_low_res.png'
    snpt.logger.info('Writing to file: %s', low_res_path)
    full.get_low_res().save(low_res_path)
    shot: BotImage = snpt.shot()
    shot.save('tmp/shot.png')
    low_res_shot_path:str = 'tmp/shot_low_res.png'
    snpt.logger.info('Writing to file: %s', low_res_shot_path)
    shot.get_low_res().save(low_res_shot_path)

if __name__ == '__main__':
    main()