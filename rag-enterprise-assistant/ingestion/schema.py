from dataclasses import dataclass
from typing import List

@dataclass
class RawDocument:
    source: str
    text: str 

@dataclass
class TextChunk:
    source: str
    chunk_id: str
    text: str 
