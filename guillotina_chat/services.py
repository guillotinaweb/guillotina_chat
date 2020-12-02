from guillotina import configure
from guillotina.component import getMultiAdapter
from guillotina.interfaces import IContainer, IResourceSerializeToJsonSummary
from guillotina.utils import get_authenticated_user_id
from guillotina_chat.content import IConversation


@configure.service(for_=IContainer, name='@get-conversations',
                   permission='guillotina.AccessContent')
async def get_conversations(context, request):
    results = []
    conversations = await context.async_get('conversations')
    user_id = get_authenticated_user_id()
    async for conversation in conversations.async_values():
        if user_id in conversation.users:
            summary = await getMultiAdapter(
                (conversation, request),
                IResourceSerializeToJsonSummary)()
            results.append(summary)
    results = sorted(results, key=lambda conv: conv['creation_date'])
    return results


@configure.service(for_=IConversation, name='@get-messages',
                   permission='guillotina.AccessContent')
async def get_messages(context, request):
    results = []
    async for message in context.async_values():
        summary = await getMultiAdapter(
            (message, request),
            IResourceSerializeToJsonSummary)()
        results.append(summary)
    results = sorted(results, key=lambda mes: mes['creation_date'])
    return results
