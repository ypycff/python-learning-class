from time import strftime, localtime
import asyncio

async def createStringAfter(msg, delay) :
    await asyncio.sleep(delay)
    now = strftime("%H:%M:%S", localtime())
    return "{0} {1}".format(now, msg)
    
async def main():
    print("*****Start of main*****")
    result = await asyncio.create_task(createStringAfter("Bonjour", 10))
    print(result)
    print("*****End of main*****")
    
if __name__ == "__main__" :
    asyncio.run(main())
