import asyncio
import aiohttp
from proxybroker import Broker
from bs4 import BeautifulSoup

async def show(proxies, loop=None):
    while True:
        proxy = await proxies.get()
        if proxy is None: 
            break
        proxy_url = 'http://%s:%d' % (proxy.host, proxy.port)
        print("Using proxy: ", proxy_url)
        try:
            timeout = aiohttp.ClientTimeout(total=30)
            async with aiohttp.ClientSession(timeout=timeout) as client:
                async with client.get('https://saisyam.com', proxy=proxy_url) as resp:
                    if resp.status == 200:
                        resp = await resp.text()
                        soup = BeautifulSoup(resp, "lxml")
                        title = soup.find("title").text
                        print(title)
                        break
                    else:
                        print("Invalid Proxy")
        except Exception as e:
            print(e)

loop = asyncio.get_event_loop()
proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['HTTP'], countries=['US'], strict=True, limit=10),
    show(proxies, loop))


loop.run_until_complete(tasks)