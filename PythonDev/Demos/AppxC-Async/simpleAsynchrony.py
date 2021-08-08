from time import strftime, localtime
import asyncio

async def displayAfter(msg, delay) :
    await asyncio.sleep(delay)
    now = strftime("%H:%M:%S", localtime())
    print("%s %s" % (now, msg))
    
def main():
    print("*****Start of main*****")
    asyncio.run(displayAfter("Hello", 3))
    print("*****End of main*****")
    
if __name__ == "__main__" :
    main()
