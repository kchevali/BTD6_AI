from typing import Optional
from bot_image import BotImage
from snippet_enum import SnippetEnum
from snippet_type import SnippetType

class SnippetImage:
    image: Optional[BotImage]
    snippet_type: SnippetType
    snippet_id: SnippetEnum

    def __init__(self, snippet_type:SnippetType, snippet_id:SnippetEnum) -> None:
        self.snippet_type = snippet_type
        self.snippet_id = snippet_id
        self.image = None
    
    def set_image(self, image:BotImage) -> None:
        self.image = image