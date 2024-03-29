import httpx
import random
import asyncio
import dataclasses
from math import sqrt
from loguru import logger



class SleepTime(float):

	def __new__(C, try_number: int) -> float:
		return random.randrange(2, 14) / 10 * sqrt(try_number)


client = httpx.AsyncClient(limits=httpx.Limits(max_connections=500))


@dataclasses.dataclass(frozen=True)
class Content:

	url: str

	async def __call__(self):

		try_number = 1

		while True:

			try:

				response = await client.get(self.url)

				if response.status_code == 200:
					return response.content
				elif response.status_code == 404:
					return b''
				elif response.status_code != 429:
					logger.warning(f'{self.url} {response}')

			except Exception as e:
				if type(e) not in [
					httpx.PoolTimeout,
					httpx.ConnectTimeout,
					httpx.ConnectError,
					httpx.ReadTimeout,
					httpx.RemoteProtocolError
				]:
					logger.warning(f'{type(e)} {e}')

			await asyncio.sleep(SleepTime(try_number))
			try_number += 1