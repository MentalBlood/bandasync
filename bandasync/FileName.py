import re



class FileName(str):

	def __new__(C, string: str):
		return re.sub(
			r'[\/\\:\*\?"\<\>|]',
			'',
			string
		).strip('. ')