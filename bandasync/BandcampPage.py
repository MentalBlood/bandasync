import dataclasses

from .Album import Album
from .Artist import Artist
from .Content import Content
from .Container import Container



@dataclasses.dataclass(frozen=True)
class BandcampPage(Container):

	url: str

	async def inside(self, *args, **kwargs):

		splited = self.url.split('/')

		yield (
			Album
			if ('album' in splited) or ('track' in splited)
			else Artist
		)(Content(self.url))