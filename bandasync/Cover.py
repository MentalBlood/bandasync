import dataclasses

from .File import File
from .Path import Path
from .Content import Content
from .Container import Container



@dataclasses.dataclass(frozen=True)
class Cover(Container):

	content: Content
	artist_name: str
	album_name: str

	async def inside(self, path):
		yield File(
			content=self.content,
			path=Path(path, [self.artist_name, self.album_name, 'cover.jpg'])
		)