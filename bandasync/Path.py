import os
from .FileName import FileName



class Path(str):

	def __new__(C, string: str):
		return os.path.join(*[
			FileName(f)
			for f in string.split(os.path.sep)
		])