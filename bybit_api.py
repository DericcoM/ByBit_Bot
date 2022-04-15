import json
import aiohttp
import asyncio
from settings import ID_BOX, REQUESTS_NUMBER


class BybitAPI:

    def __init__(self, id_box) -> None:
        self.id = id_box

        self.url_detail_box = f'https://api2.bybit.com/spot/api/nft/v1/market/detail?id={id_box}'
        self.url_buy_box = 'https://api2.bybit.com/spot/api/nft/v1/order/buy'
        self.results = []
    
    async def get_symbols(self, headers):
        async with aiohttp.ClientSession(headers=headers) as session:
            tasks = self.get_tasks(session)
            responses = await asyncio.gather(*tasks)
            for response in responses:
                self.results.append(await response.text())
    
    def get_tasks(self, session):
        tasks = []
        for _ in range(0, REQUESTS_NUMBER):
            tasks.append(
                asyncio.create_task(session.post
                (self.url_buy_box, ssl=False,
                data=json.dumps({'merchandiseId': ID_BOX})))
            )
        return tasks
    
    def startSsc(self, headers):
        asyncio.get_event_loop().run_until_complete(self.get_symbols(headers))
