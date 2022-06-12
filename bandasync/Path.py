import os
from .FileName import FileName



class Path(str):

	def __new__(C, string: str):

		drive, path = os.path.splitdrive(string)

		names = []
		left = path
		while True:
			left, name = os.path.split(left)
			if name:
				names.append(name)
			else:
				break

		result_path = os.path.join(*[
			FileName(f)
			for f in reversed(names)
		])
		if drive:
			result = os.path.sep.join([drive, result_path])
		else:
			result = result_path

		return result