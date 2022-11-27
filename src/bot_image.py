from typing import Optional
import numpy as np
from numpy.typing import NDArray #type:ignore
from PIL import Image
import bot_log
from settings import STANDARD_HEIGHT, STANDARD_WIDTH
from snippet_type import SnippetType
import imagehash
from coord import Coord

class BotImage:
    
    np_data: NDArray[np.uint8]
    pil_data: Image.Image
    low_res_data: Optional[Image.Image] = None
    low_res_reduction: int = 16
    image_hash:Optional[imagehash.ImageHash] = None

    logger:bot_log.BotLogger = bot_log.BotLogger('bot_image')

    @staticmethod
    def from_array(data:NDArray[np.uint8]) -> 'BotImage':
        img: BotImage = BotImage._from_pil(Image.fromarray(data)) # type:ignore
        img.np_data = data
        return img

    @staticmethod
    def from_pil(data:Image.Image) -> 'BotImage':
        img: BotImage = BotImage._from_pil(data)
        img.np_data = np.asarray(img.pil_data)
        return img
    
    @staticmethod
    def _from_pil(data:Image.Image) -> 'BotImage':
        img: BotImage = BotImage()
        img.pil_data = data

         # cannot use Coord.WIDTH or Coord.HEIGHT as it is not set yet when this is first called
        img.pil_data.thumbnail((STANDARD_WIDTH, STANDARD_HEIGHT), Image.Resampling.LANCZOS)
        return img
    
    @staticmethod
    def open(path:str) -> 'BotImage':
        return BotImage.from_pil(Image.open(path))
    
    def get_low_res(self) -> Image.Image:
        if self.low_res_data is None:
            width: int = self.get_width() // self.low_res_reduction
            height: int = self.get_height() // self.low_res_reduction
            self.low_res_data = self.pil_data
            self.low_res_data.thumbnail((width, height), Image.Resampling.LANCZOS)
            self.pil_data = Image.fromarray(self.np_data) # type:ignore # thumbnail is destructive
        return self.low_res_data

    def get_width(self) -> int:
        return 0 if self.get_height() == 0 else len(self.np_data[0])
    
    def get_height(self) -> int:
        return len(self.np_data)

    def save(self, path:str) -> None:
        BotImage.logger.info('Writing image to file: "%s"', path)
        self.pil_data.save(path)
    
    def select(self, snippet_type:SnippetType) -> Optional['BotImage']:
        width: int = snippet_type.x2.real_space-snippet_type.x1.real_space
        height: int = snippet_type.y2.real_space-snippet_type.y1.real_space
        y_offset: int = Coord.Y1.real_space
        # BotImage.logger.debug("Select %s | original %dx%d -> %dx%d", snippet_type.name, len(self.np_data[0]), len(self.np_data), width, height)
        if height > len(self.np_data) or width > len(self.np_data[0]): return
        return BotImage.from_array(self.np_data[
            snippet_type.y1.real_space - y_offset:snippet_type.y2.real_space-y_offset,
            snippet_type.x1.real_space:snippet_type.x2.real_space
        ])

    def get_image_hash(self) -> imagehash.ImageHash:
        if self.image_hash is None:
            self.image_hash = imagehash.average_hash(self.pil_data) #type:ignore
        return self.image_hash


def main() -> None:
    BotImage.logger.info('Hello World! - Bot Image')
    img:BotImage = BotImage.from_pil(Image.open("tmp/shot.png"))
    low_res: Image.Image = img.get_low_res()
    path:str = 'tmp/bot_img_shot_low_res.png'
    BotImage.logger.info('Writing to: %s', path)
    low_res.save(path)

if __name__ == '__main__':
    main()