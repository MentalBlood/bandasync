from setuptools import setup, find_packages


if __name__ == '__main__':

	try:
		with open('README.md', encoding='utf-8') as f:
			long_description = f.read()
	except FileNotFoundError:
		long_description = ''

	setup(
		name='bandasync',
		version='1.3.0',
		description='Fast, working tool for downloading music from bandcamp',
		long_description=long_description,
		long_description_content_type='text/markdown',
		author='mentalblood',
		install_requires=[
			'bs4',
			'loguru',
			'httpx',
			'mutagen',
			'python_version >= "3.10"'
		],
		packages=find_packages()
	)
