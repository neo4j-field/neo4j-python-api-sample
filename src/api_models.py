from typing import List, Optional
from pydantic import BaseModel


class SongAPI(BaseModel):
    uid: str
    title: str
    popularity: int


class ArtistAPI(BaseModel):
    uid: str
    name: str
    songs: Optional[List[SongAPI]]


class PlaylistAPI(BaseModel):
    uid: str
    title: str
    songs: Optional[List[SongAPI]]


class PlaylistInput(BaseModel):
    title: str
    songs: List[str]
