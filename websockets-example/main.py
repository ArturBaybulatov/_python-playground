from pydash import _
import asyncio
import datetime
import random
import websockets

from libs.baybulatov_util_py_0_3_0_plus import util


async def example(websocket, path):
    print(await websocket.recv())

    while True:
    #for x in range(5):
        await websocket.send(util.lorem(1))
        await asyncio.sleep(1)

    await websocket.close(reason='Goodbye from server')


loop = asyncio.get_event_loop()
loop.run_until_complete(websockets.serve(example, 'localhost', 49152))
loop.run_forever()



# import code; code.interact(local=dict(globals(), **locals()))
