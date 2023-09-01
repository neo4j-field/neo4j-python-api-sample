from typing import List, Optional
from pydantic import BaseModel


class AlbumAPI(BaseModel):
    uid: str


class SongAPI(BaseModel):
    uid: str
    title: str
    loudness: float
    liveness: float
    tempo: float
    valence: float
    instrumentalness: float
    danceability: float
    speechiness: float
    duration: int
    mode: bool
    popularity: int
    acousticness: float
    key: int
    energy: float

    albums: Optional[List[AlbumAPI]]


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
