import os
import dataclasses
from loguru import logger
from bs4 import BeautifulSoup, Tag

from .Path import Path
from .Album import Album
from .Content import Content
from .Container import Container



@dataclasses.dataclass(frozen=True)
class Artist(Container):

	page: Content

	async def inside(self, path, *args, **kwargs):

		root = BeautifulSoup(await self.page(), 'html.parser')

		try:

			composer_name = root.find('meta', {'property': 'og:title'})['content']

			grid_items = filter(
				lambda c: isinstance(c, Tag),
				root.find(id='music-grid').children
			)

			base_url = root.find('meta', {'property': 'og:url'})['content']

			for g in grid_items:

				album_name = g.find('p').text.split('\n')[1].strip()
				album_path = Path(path, [composer_name, album_name])
				if not (
					os.path.exists(album_path) and
					any(
						p.endswith('.mp3')
						for p in os.listdir(album_path)
					)
				):
					a = g.find('a')['href']
					if a.startswith('https'):
						url = a
					else:
						url = f"{base_url}{a}"

					yield Album(Content(url))
		
		except Exception as e:
			yield Album(self.page)