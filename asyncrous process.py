import asyncio
async def greetings():
    asyncio.create_task(disp())
    print("good morning")
    await asyncio.sleep(1)
    print("good byee..")
async def disp():
    print("good afternoon")
    await asyncio.sleep(1)
    print("good byee..")
asyncio.run(greetings())
