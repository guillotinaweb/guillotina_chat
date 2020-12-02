from guillotina import configure
from guillotina.component import get_utility
from guillotina.interfaces import IContainer
from guillotina.transactions import get_tm
from guillotina_chat.utility import IMessageSender

import asyncio
import logging

logger = logging.getLogger('guillotina_chat')


@configure.service(
    context=IContainer, method='GET',
    permission='guillotina.AccessContent', name='@conversate')
async def ws_conversate(context, request):
    ws = request.get_ws()
    await ws.prepare()

    utility = get_utility(IMessageSender)
    utility.register_ws(ws, request)

    tm = get_tm()
    await tm.abort()
    try:
        async for msg in ws:
            # ws does not receive any messages, just sends
            pass
    finally:
        logger.debug('websocket connection closed')
        utility.unregister_ws(ws)
    return {}
