import os
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
args = parser.parse_args()


if args.log:
	logger.add(args.log)

if platform.system() == 'Windows':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(
	Task(args.url)(path='.')
)