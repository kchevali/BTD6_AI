from typing import Any, Dict, List, Optional, Tuple
from bot_image import BotImage
from snippet import Snippet
from snippet_enum import SnippetEnum
from snippet_img import SnippetImage
from snippet_sel_type import SnippetSelType
from snippet_type import SnippetType
from settings import SNIPPET_INFO_PATH, SNIPPETS_DIR, SNIPPET_TYPES_PATH
from coord import Coord
import os, bot_log, json
import imagehash

class WhereAmI:

    snpt: Snippet = Snippet()
    snippets: Dict[SnippetEnum, SnippetImage] = {}
    snippet_types: Dict[str, SnippetType] = {}
    snippet_groups: Dict[SnippetType, List[SnippetImage]] = {}
    logger:bot_log.BotLogger = bot_log.BotLogger('whereami', bot_log.DEBUG)

    def __init__(self) -> None:
        self.reload_snippets()
    
    def load_json_files(self) -> None:
        with open(SNIPPET_TYPES_PATH) as f:
            type_json:Dict[str,Any] = json.load(f)

        for type_id, type_dict in type_json.items():
            if type_dict.get("is_full", False) is True:
                x1, y1, x2, y2 = Coord.X1, Coord.Y1, Coord.X2, Coord.Y2
            else:
                x1: Coord = Coord.from_monitor_x(int(type_dict["x1"]))
                y1: Coord = Coord.from_monitor_y(int(type_dict["y1"]))
                x2: Coord = Coord.from_monitor_x(int(type_dict["x2"]))
                y2: Coord = Coord.from_monitor_y(int(type_dict["y2"]))

            # WhereAmI.logger.debug('Snippet Type: %s - (%d x %d) -> (%d, %d), (%d, %d)', type_id, x2.real_space - x1.real_space, y2.real_space - y1.real_space, x1.real_space, y1.real_space, x2.real_space, y2.real_space)
            snippet_type = SnippetType(type_id, SnippetSelType[type_dict['selection']], x1,y1,x2,y2)
            self.snippet_types[type_id] = snippet_type
            self.snippet_groups[snippet_type] = []

        with open(SNIPPET_INFO_PATH) as f:
            info_json:Dict[str,Dict[str,str]] = json.load(f)
        for snippet_id, snippet_dict in info_json.items():
            snippet_enum: SnippetEnum = SnippetEnum[snippet_id]
            snippet_type: SnippetType = self.snippet_types[snippet_dict["type"]]
            snippet_img: SnippetImage = SnippetImage(snippet_type, snippet_enum)
            
            self.snippets[snippet_enum] = snippet_img
            self.snippet_groups[snippet_type].append(snippet_img)
            # WhereAmI.logger.debug('Info snippet: %s', snippet_enum._name_)
        WhereAmI.logger.debug('Loaded JSONs | snippet types: %d snippet info: %d', len(self.snippet_types), len(self.snippets))
    
    def reload_snippets(self) -> None:
        self.load_json_files()
        if not os.path.isdir(SNIPPETS_DIR): os.mkdir(SNIPPETS_DIR)
        snippet_files: list[str] = os.listdir(SNIPPETS_DIR)
        snippet_file_count:int = 0
        for file_name in snippet_files:
            file_base, file_ext = os.path.splitext(file_name)
            if file_ext != ".png": continue
            snippet_enum: SnippetEnum = SnippetEnum[file_base]
            # WhereAmI.logger.debug('Found snippet: "%s"', file_base)
            self.snippets[snippet_enum].set_image(BotImage.open(os.path.join(SNIPPETS_DIR, file_name)))
            snippet_file_count += 1
        WhereAmI.logger.debug("Loading Snippets | Found %d", snippet_file_count)

    def get_location(self) -> Optional[SnippetImage]:
        diff:List[Tuple[int, SnippetImage]] = []
        shot: BotImage = self.snpt.shot()
        # shot.save('tmp/shot.png')

        min_hash_diff:int = 65
        best_snippet: Optional[SnippetImage] = None
        for snippet_type in self.snippet_types.values():
            if snippet_type.sel != SnippetSelType.PAGE: continue
            crop: Optional[BotImage] = shot.select(snippet_type)
            if crop is None:
                WhereAmI.logger.warning('Cannot crop for snippet type: %s', snippet_type.name)
                continue
            # crop.save('tmp/shot_{}.png'.format(snippet_type.name))

            crop_hash: imagehash.ImageHash = BotImage.from_pil(crop.get_low_res()).get_image_hash()
            # WhereAmI.logger.debug("Crop hash: %d", crop_hash)

            for snippet in self.snippet_groups[snippet_type]:
                if snippet.image is None:
                    WhereAmI.logger.warning('No snippet image for: "%s"', snippet.snippet_id._name_)
                    continue
                snippet_hash: imagehash.ImageHash = snippet.image.get_image_hash()
                delta: int = abs(crop_hash - snippet_hash)
                diff.append((delta, snippet))

                if delta < min_hash_diff:
                    min_hash_diff = delta
                    best_snippet = snippet
        if best_snippet is not None:
            WhereAmI.logger.info('Current location: %s', best_snippet.snippet_id._name_)
        else:
            WhereAmI.logger.warning('Could not determine current location')
        # diff.sort(key = lambda x: x[0])
        # for hash_diff, snippet in diff:
        #     WhereAmI.logger.debug("Location: %s - diff: %d", snippet.snippet_id._name_, hash_diff)
            
            
    def get_missing_snippets(self) -> None:
        missing: list[SnippetEnum] = []
        for snippet_id, s_img in self.snippets.items():
            if s_img.image is not None: continue
            missing.append(snippet_id)

        if len(missing) == 0: return
        WhereAmI.logger.info("Getting missing snippets | Count: %d", len(missing))
        if Coord.WIDTH.real_space < Coord.WIDTH.standard_space:
            WhereAmI.logger.warning('Increase game window - width: %d < %d', Coord.WIDTH.real_space, Coord.WIDTH.standard_space)

        for snippet_id in missing:
            input("Please move to: '{}'".format(snippet_id._name_))
            snippet_path: str = os.path.join(SNIPPETS_DIR, "{}.png".format(snippet_id._name_))
            img: SnippetType = self.snippets[snippet_id].snippet_type
            self.snpt.shot_crop(img.x1, img.y1, img.x2, img.y2).pil_data.save(snippet_path)
            WhereAmI.logger.debug('Saved snippet to "%s"', snippet_path)

def main() -> None:
    wami: WhereAmI = WhereAmI()
    WhereAmI.logger.info("Hello World! - Where Am I?")
    wami.get_missing_snippets()
    wami.get_location()
    # import numpy as np
    # a = np.array([
    #     [[0,1],[2,3], [4,5]],
    #     [[10,11],[12,13], [14,15]],
    #     [[20,21],[22,23], [24,25]]
    # ])
    # print(a[0:2, 1])

if __name__ == '__main__':
    main()

