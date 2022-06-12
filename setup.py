import os
from setuptools import setup, find_packages


if __name__ == '__main__':

	long_description = ''
	if os.path.exists('README.md'):
		with open('README.md', encoding='utf-8') as f:
			long_description = f.read()

	setup(
		name='bandasync',
		version='1.0.0',
		description='banduncamp remake',
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
