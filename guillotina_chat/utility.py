import asyncio
import orjson
import logging

from guillotina.async_util import IAsyncUtility
from guillotina.component import getMultiAdapter
from guillotina.interfaces import IResourceSerializeToJsonSummary
from guillotina.renderers import GuillotinaJSONEncoder
from guillotina.utils import get_authenticated_user_id, get_current_request

logger = logging.getLogger('guillotina_chat')


class IMessageSender(IAsyncUtility):
    pass


class MessageSenderUtility:

    def __init__(self, settings=None, loop=None):
        self._loop = loop
        self._settings = {}
        self._webservices = []

    def register_ws(self, ws, request):
        ws.user_id = get_authenticated_user_id()
        self._webservices.append(ws)

    def unregister_ws(self, ws):
        self._webservices.remove(ws)

    async def send_message(self, message):
        summary = await getMultiAdapter(
            (message, get_current_request()),
            IResourceSerializeToJsonSummary)()
        await self._queue.put((message, summary))

    async def initialize(self, app=None):
        self._queue = asyncio.Queue()

        while True:
            try:
                message, summary = await self._queue.get()
                for user_id in message.__parent__.users:
                    for ws in self._webservices:
                        if ws.user_id == user_id:
                            await ws.send_str(orjson.dumps(summary))
            except Exception:
                logger.warn(
                    'Error sending message',
                    exc_info=True)
                await asyncio.sleep(1)
