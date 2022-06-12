import os
from .FileName import FileName



class Path(str):

	def __new__(C, root, path: list[str]):

		return os.path.join(root, *[
			FileName(p)
			for p in path
		])