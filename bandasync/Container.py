import abc
import asyncio



class Container(metaclass=abc.ABCMeta):

	async def __call__(self, *args, **kwargs):
		return await asyncio.gather(*[
			i(*args, **kwargs)
			if isinstance(i, Container)
			else i()
			async for i in self.inside(*args, **kwargs)
		])

	@abc.abstractmethod
	async def inside(self, *args, **kwargs) -> None:
		pass