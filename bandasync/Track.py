import os
import mutagen
import dataclasses
from mutagen.easyid3 import EasyID3

from .Path import Path
from .File import File
from .Content import Content
from .Container import Container




@dataclasses.dataclass(frozen=True)
class Track(Container):

	content: Content

	title: str
	album: str
	artist: str
	composer: str
	number: int
	duration: int
	released: bool

	async def inside(self, path):
		yield File(
			content=self.content,
			path=Path(os.path.join(path, self.composer, self.album, f'{self.title}.mp3'))
		)

	# def download(self, downloader, output_folder, logger) -> None:

	# 	if not self.url:
	# 		return

	# 	file_path = os.path.join(output_folder, FileName(f'{self.title}.mp3'))
	# 	if os.path.exists(file_path):
	# 		return

	# 	downloader(self.url, file_path)

	# 	try:
	# 		tags = EasyID3(file_path)
	# 	except mutagen.id3.ID3NoHeaderError:
	# 		f = mutagen.File(file_path, easy=True)
	# 		f.add_tags()
	# 		tags = f

	# 	tags.update({
	# 		'title': self.title,
	# 		'album': self.album,
	# 		'artist': self.artist,
	# 		'composer': self.composer,
	# 		'albumartist': self.artist,
	# 		'tracknumber': str(self.number)
	# 	})
	# 	tags.save(file_path, v1=2)

	# 	logger.success(file_path)