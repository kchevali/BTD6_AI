from typing import List
import os, bot_log
from settings import GRID_HEIGHT, GRID_WIDTH

class BitMap:
    data: List[List[bool]] = []
    logger:bot_log.BotLogger = bot_log.BotLogger('snippet')

    def __init__(self, data: List[List[bool]] = []) -> None:
        self.data = data
        if self.data: return
        self.data = [[False for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    
    @staticmethod
    def load(path:str) -> 'BitMap':
        with open(path, "rb") as f:
            arr: bytes = f.read()
        
        bits: List[List[bool]] = []
        idx:int = 0
        for _ in range(GRID_HEIGHT):
            bool_list:List[bool] = []
            for _ in range(GRID_WIDTH):
                bool_list.append(BitMap.read_bit(arr, idx))
                idx += 1
            bits.append(bool_list)
        return BitMap(bits)
    
    def dump(self, path:str) -> None:
        BitMap.logger.info('Writing bitmap to "%s"', path)
        with open(path, "wb") as f:
            f.write(self._to_binary())
    
    def byte_size(self) -> int:
        length: int = self.size()
        return length // 8 + (0 if length % 8 == 0 else 1)
    
    def size(self) -> int:
        return (len(self.data) * len(self.data[0])) if len(self.data) > 0 else 0
    
    def _to_binary(self) -> bytes:
        x:int = 0
        for arr in self.data:
            for bit in arr:
                x = (x << 1) | bit
        return x.to_bytes(self.byte_size(), 'big')
    
    @staticmethod
    def read_bit(arr:bytes, idx:int) -> bool:
        arr_idx: int = idx // 8
        # BitMap.logger.debug("Read bit | Length: %d - Idx: %d", len(arr), idx)
        return (((arr[arr_idx] >> (idx % 8)) & 1) != 0) if arr_idx < len(arr) else False

def main() -> None:
    BitMap.logger.info("Hello World! - BitMap")
    tmp_dir:str = "tmp"
    os.makedirs(tmp_dir, exist_ok=True)

    bitmap: BitMap = BitMap([
        [True, False, True, False],
        [False, True, False, True],
        [True, False, True, False],
        [False, True, False, True]
    ])
    BitMap.logger.debug("Byte Count: %d", bitmap.byte_size())

    bitmap_file:str = os.path.join(tmp_dir, "bitmap")
    bitmap.dump(bitmap_file)

    cmpmap:BitMap = BitMap.load(bitmap_file)
    bitmap2_file:str = os.path.join(tmp_dir, "bitmap2")
    cmpmap.dump(bitmap2_file)

    empty: BitMap = BitMap()
    empty.dump(os.path.join(tmp_dir, "empty_bitmap"))

if __name__ == '__main__': 
    main()
