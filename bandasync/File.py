import os
import dataclasses
from loguru import logger

from .Path import Path
from .Content import Content



@dataclasses.dataclass(frozen=True)
class File:

	content: Content
	path: Path

	async def __call__(self):

		if not os.path.exists(self.path):

			data = await self.content()

			try:
				os.makedirs(os.path.dirname(self.path))
			except:
				pass
			with open(self.path, 'wb') as f:
				f.write(data)

			logger.success(self.path)