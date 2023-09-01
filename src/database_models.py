from neomodel import (
    StructuredNode,
    StringProperty,
    IntegerProperty,
    FloatProperty,
    BooleanProperty,
    DateTimeProperty,
    RelationshipTo,
    ZeroOrMore,
    OneOrMore,
    UniqueIdProperty,
)


class Album(StructuredNode):
    uid = UniqueIdProperty()


class Song(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(index=True)
    loudness = FloatProperty()
    liveness = FloatProperty()
    tempo = FloatProperty()
    valence = FloatProperty()
    instrumentalness = FloatProperty()
    danceability = FloatProperty()
    speechiness = FloatProperty()
    duration = IntegerProperty()
    mode = BooleanProperty()
    popularity = IntegerProperty()
    acousticness = FloatProperty()
    key = IntegerProperty()
    energy = FloatProperty()

    albums = RelationshipTo(Album, "RELEASED_IN", cardinality=OneOrMore)


class Artist(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(index=True)

    songs = RelationshipTo(Song, "RECORDED", cardinality=ZeroOrMore)


class Playlist(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(index=True)

    songs = RelationshipTo(Song, "CONTAINS", cardinality=OneOrMore)
