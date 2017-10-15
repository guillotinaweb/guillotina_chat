from guillotina import configure, content, Interface, schema


class IConversation(Interface):

    users = schema.List(
        value_type=schema.TextLine()
    )


@configure.contenttype(
    type_name="Conversation",
    schema=IConversation,
    behaviors=["guillotina.behaviors.dublincore.IDublinCore"],
    allowed_types=['Message'])
class Conversation(content.Folder):
    pass


class IMessage(Interface):
    text = schema.Text(required=True)


@configure.contenttype(
    type_name="Message",
    schema=IMessage,
    behaviors=[
        "guillotina.behaviors.dublincore.IDublinCore",
        "guillotina.behaviors.attachment.IAttachment"
    ])
class Message(content.Item):
    pass
