import dataclasses

from .Container import Container
from .BandcampPage import BandcampPage



@dataclasses.dataclass(frozen=True)
class Task(Container):

	urls: list[str]

	async def inside(self, *args, **kwargs):
		for u in self.urls:
			yield BandcampPage(u)