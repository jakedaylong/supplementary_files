import asyncio


async def get_chat_id(name):
    await asyncio.sleep(3)
    return "chat-%s" % name


async def do_long_calc():
    await asyncio.sleep(2)
    return 8874987


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_chat_id("django"))
    another_result = loop.run_until_complete(do_long_calc())
    print(result, another_result)


if __name__ == "__main__":
    main()
