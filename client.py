# import asyncio
# import websockets
# async def hello():
# 	async with websockets.connect('ws://localhost:8080') as websocket:
# 		name = input("What's your name??")
# 		await websocket.send(name)
# 		print(websocket)
# 		print("> {}".format(name))
# 		greeting = await websocket.recv()
# 		print("> {}".format(greeting))

# asyncio.get_event_loop().run_until_complete(hello())


from websocket import create_connection
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(module)s -  %(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

ws = create_connection("ws://127.0.0.1:12345")
logger.info("Open")
send = "11 23"
logger.info("Sending '{}'...".format(send))
ws.send(send)
logger.info("sent")
logger.info("Receiving...")
result = ws.recv()
logger.info("Received '{}".format(result))
ws.close()
logger.info("Close")


# import websocket
# import thread
# import time
# import logging

# logger = logging.getLogger(__name__)
