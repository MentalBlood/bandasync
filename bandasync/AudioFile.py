import os
import io
import dataclasses
from loguru import logger
from mutagen import mp3, easyid3, id3

from .Path import Path
from .Content import Content



@dataclasses.dataclass(frozen=True)
class AudioFile:

	content: Content
	path: Path
	tags: dict[str, str]

	async def __call__(self):

		if not os.path.exists(self.path):

			data_io = io.BytesIO(await self.content())

			try:
				tags = easyid3.EasyID3(data_io)
			except id3.ID3NoHeaderError:

				data_io.seek(0)
				f = mp3.MP3(data_io)

				f.add_tags()
				f.save(data_io)

			data_io.seek(0)
			tags = easyid3.EasyID3(data_io)

			tags.update(self.tags)
			tags.save(data_io)

			try:
				os.makedirs(os.path.dirname(self.path))
			except:
				pass

			data_io.seek(0)
			with open(self.path, 'wb') as f:
				f.write(data_io.read())

			logger.success(self.path)