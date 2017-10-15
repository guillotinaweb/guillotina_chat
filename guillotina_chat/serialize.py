from guillotina import configure
from guillotina.interfaces import IResourceSerializeToJsonSummary
from guillotina.json.serialize_content import DefaultJSONSummarySerializer
from guillotina.utils import get_owners
from guillotina_chat.content import IConversation, IMessage
from zope.interface import Interface


@configure.adapter(
    for_=(IConversation, Interface),
    provides=IResourceSerializeToJsonSummary)
class ConversationJSONSummarySerializer(DefaultJSONSummarySerializer):
    async def __call__(self):
        data = await super().__call__()
        data.update({
            'id': self.context.id,
            'creation_date': self.context.creation_date,
            'title': self.context.title,
            'users': self.context.users
        })
        return data


@configure.adapter(
    for_=(IMessage, Interface),
    provides=IResourceSerializeToJsonSummary)
class MessageJSONSummarySerializer(DefaultJSONSummarySerializer):
    async def __call__(self):
        data = await super().__call__()
        data.update({
            'id': self.context.id,
            'creation_date': self.context.creation_date,
            'text': self.context.text,
            'author': get_owners(self.context)[0],
            'conversation_id': self.context.__parent__.id
        })
        return data
