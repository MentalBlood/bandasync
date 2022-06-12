import os
import json
import asyncio
import platform
import argparse
from loguru import logger

from .Task import Task



parser = argparse.ArgumentParser(description='Download audio from Bandcamp')
parser.add_argument(
	'url',
	nargs='*',
	default=[],
	help='input page: album URL or discography URL'
)
parser.add_argument(
	'-o',
	'--output',
	default=os.getcwd(),
	help='output folder path'
)
parser.add_argument(
	'-l',
	'--log',
	default=None,
	help='log file path'
)
parser.add_argument(
	'-f',
	'--file',
	type=str,
	nargs='*',
	default=[],
	help='JSON file with output-to-URLs mapping'
)
args = parser.parse_args()


if args.log:
	logger.add(args.log)

output_to_urls = {
	args.output: args.url
}
if args.file:
	for path in args.file or []:
		with open(path) as f:
			for o, urls in json.load(f).items():
				if o not in output_to_urls:
					output_to_urls[o] = []
				for u in urls:
					output_to_urls[o].append(u)

async def main():
	await asyncio.gather(*[
		Task(urls)(path=p)
		for p, urls in output_to_urls.items()
	])

if platform.system() == 'Windows':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(
	main()
)