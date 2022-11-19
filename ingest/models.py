from collections import Counter
from typing import Any, Dict, List, Tuple

from pydantic import BaseModel


class Post(BaseModel):
    content: str
    publication: str

class ProcessedPost(BaseModel):
    publication: str
    entities: Counter = Counter()
    article_count: int = 0

    @property
    def pub_key(self) -> str:
        return None
    
    def transform_for_database(self, top_n=2000) -> List[Tuple[str, str, str, Dict]]:
        return None

    def __add__(self, other) -> ProcessedPost:
        return self
 
