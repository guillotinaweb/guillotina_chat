from guillotina import configure, content, Interface, schema
from guillotina.directives import index_field
from guillotina.interfaces import IFolder, IItem


class IConversation(IFolder):

    index_field("users", type="keyword")
    users = schema.List(
        value_type=schema.TextLine(),
        default=list()
    )


@configure.contenttype(
    type_name="Conversation",
    schema=IConversation,
    behaviors=["guillotina.behaviors.dublincore.IDublinCore"],
    allowed_types=['Message'])
class Conversation(content.Folder):
    pass


class IMessage(IItem):
    index_field("text", type="text")
    text = schema.Text(required=True)


@configure.contenttype(
    type_name="Message",
    schema=IMessage,
    behaviors=[
        "guillotina.behaviors.dublincore.IDublinCore",
        "guillotina.behaviors.attachment.IAttachment"
    ],
    globally_addable=False,
)
class Message(content.Item):
    pass
