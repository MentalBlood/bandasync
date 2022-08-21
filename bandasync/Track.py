import dataclasses

from .Path import Path
from .Content import Content
from .Container import Container
from .AudioFile import AudioFile




@dataclasses.dataclass(frozen=True)
class Track(Container):

	content: Content

	title: str
	album: str
	artist: str
	number: int
	composer: str
	duration: int
	released: bool
	genre: list[str]

	async def inside(self, path):
		yield AudioFile(
			content=self.content,
			path=Path(path, [self.composer, self.album, f'{self.title}.mp3']),
			tags={
				'genre': self.genre,
				'title': self.title,
				'album': self.album,
				'artist': self.artist,
				'composer': self.composer,
				'albumartist': self.artist,
				'tracknumber': str(self.number),
			}
		)