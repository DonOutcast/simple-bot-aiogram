import asyncio
import platform
from controller.controller import Controller

if __name__ == "__main__":
    if "Windows" == platform.system():
        asyncio.set_event_loop(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(Controller().main())
