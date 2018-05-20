# import asyncio
# import websockets

# async def hello(websocket, path):
# 	name = await websocket.recv()
# 	print("< {}".format(name))

# 	greeting  = "Hello {}!!".format(name)
# 	await websocket.send(greeting)
# 	print("> {}".format(greeting))

# start_server = websockets.serve(hello, 'localhost', 8080)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()

import logging
from websocket_server import WebsocketServer

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(module)s -  %(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

def new_client(client, server):
	logger.info('New Client {}:{} has joined'.format(client['address'][0], client['address'][1]))

def client_left(client, server):
	logger.info('New Client {}:{} has left'.format(client['address'][0], client['address'][1]))

def message_received(client, server, message):
	logger.info('Message "{}" has been received from {}:{}'.format(message, client['address'][0], client['address'][1]))
	# reply_message = 'Hi!!' + message
	result = message_processing(message)
	server.send_message(client, str(result))
	logger.info('Message "{}" has been received from {}:{}'.format(result, client['address'][0], client['address'][1]))

def message_processing(message):
	content = message.split(' ')
	return int(content[0]) + int(content[1])

if __name__ == '__main__':
	server = WebsocketServer(port=12345, host='127.0.0.1', loglevel=logging.INFO)
	server.set_fn_new_client(new_client)
	server.set_fn_client_left(client_left)
	server.set_fn_message_received(message_received)
	server.run_forever()