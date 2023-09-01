"""Application main file."""
from fastapi import FastAPI, HTTPException

from neomodel import DoesNotExist, config
from .database_models import Artist, Song, Playlist
from .api_models import AlbumAPI, ArtistAPI, PlaylistAPI, SongAPI, PlaylistInput

config.DATABASE_URL = "bolt://neo4j:password@localhost:7687/spotify"


# Create app
app = FastAPI(title="neomodel sample project")


@app.get("/")
async def root():
    songs = Song.nodes.all()
    return {"# of songs": len(songs)}


@app.get("/artists")
async def get_artists(page_size: int = 10, page_number: int = 0):
    artists = Artist.nodes.order_by("name")[
        page_number * page_size : page_number * page_size + page_size
    ]
    return [
        ArtistAPI(
            uid=a.uid,
            name=a.name,
            songs=[
                SongAPI(uid=s.uid, title=s.title, popularity=s.popularity)
                for s in a.songs.all()
            ],
        )
        for a in artists
    ]


@app.get("/songs")
async def get_song(song_uid: str):
    song = Song.nodes.get(uid=song_uid)
    return SongAPI(
        uid=song.uid,
        title=song.title,
        loudness=song.loudness,
        liveness=song.liveness,
        tempo=song.tempo,
        valence=song.valence,
        instrumentalness=song.instrumentalness,
        danceability=song.danceability,
        speechiness=song.speechiness,
        duration=song.duration,
        mode=song.mode,
        popularity=song.popularity,
        acousticness=song.acousticness,
        key=song.key,
        energy=song.energy,
        albums=[AlbumAPI(uid=a.uid) for a in song.albums.all()],
    )


@app.post("/playlists")
async def create_playlist(input: PlaylistInput):
    try:
        playlist = Playlist(
            title=input.title,
        ).save()

        for _song in input.songs:
            song = Song.nodes.get(uid=_song)
            playlist.songs.connect(song)

    except DoesNotExist as e:
        raise HTTPException(status_code=500, detail="Item not found")
    except Exception as e:
        print(e)
    return PlaylistAPI(
        uid=playlist.uid,
        title=playlist.title,
        songs=[
            SongAPI(uid=s.uid, title=s.title, popularity=s.popularity)
            for s in playlist.songs.all()
        ],
    )
