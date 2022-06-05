import dataclasses

from .Album import Album
from .Artist import Artist
from .Content import Content
from .Container import Container



@dataclasses.dataclass(frozen=True)
class BandcampPage(Container):

	url: str

	async def inside(self, *args, **kwargs):
		yield (
			Album
			if 'album' in self.url.split('/')
			else Artist
		)(Content(self.url))