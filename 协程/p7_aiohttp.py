import asyncio
import aiohttp

urls = [
    'http://httpbin.org',
    'http://httpbin.org/get',
    'http://httpbin.org/ip',
    'http://httpbin.org/headers'
]

async def crawler():
    async with aiohttp.ClientSession() as session:
        # 创建任务列表
        tasks = [asyncio.create_task(session.get(url)) for url in urls]
        # 使用as_completed按完成顺序处理
        for future in asyncio.as_completed(tasks):
            response = await future
            # 打印响应状态和部分内容，或者使用response.text()
            # 注意：如果打印response对象本身，不会输出内容，最好打印文本。
            # 但这里为了简单，打印状态码和url
            print(f"{response.url}: {response.status}:{response.text}")
            # 如果需要打印响应体，可以读取文本，但注意可能会很大
            # text = await response.text()
            # print(text[:200])
            await response.release()  # 确保连接释放（aiohttp自动处理上下文，但显式释放也好）

if __name__ == "__main__":
    asyncio.run(crawler())


#协程不是同步返回，是异步的，不是顺序的，所以不是按顺序返回数据，而是哪个页面返回快返回哪个