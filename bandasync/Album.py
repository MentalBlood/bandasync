import re
import html
import json
import dataclasses
from bs4 import BeautifulSoup

from .Track import Track
from .Cover import Cover
from .Content import Content
from .Container import Container



@dataclasses.dataclass(frozen=True)
class Album(Container):

	page: Content

	async def inside(self, *args, **kwargs):

		content = await self.page()
		text = content.decode('utf8')

		data = json.loads(
			html.unescape(
				re.sub(
					r'\\u\d\d\d\d',
					'',
					re.search(r'data-tralbum=\"([^\"]*)\"', text).group(1)
				)
			)
		)
		cover_url = re.search('<a class="popupImage" href="([^\"]*)', text).group(1)

		root = BeautifulSoup(text, 'html.parser')
		band_name_tag = root.find(id='band-name-location')
		composer = band_name_tag.select('span.title')[0].text

		album_name = data['current']['title']

		for t in data['trackinfo']:
			try:
				yield Track(
					content=Content(t['file']['mp3-128']),
					title=t['title'],
					album=album_name,
					artist=data['artist'],
					composer=composer,
					number=t['track_num'],
					duration=t['duration'],
					released=not t['unreleased_track']
				)
			except (TypeError, KeyError):
				pass
		
		yield Cover(
			content=Content(cover_url.replace('https', 'http')),
			composer_name=composer,
			album_name=album_name
		)
