# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class SendRawMessageReqMsgType(object):
    pass


@attr.s
class SendRawMessageReqReceiveIDType(object):
    pass


@attr.s
class SendRawMessageReq(object):
    receive_id_type: SendRawMessageReqReceiveIDType = attr.ib(
        factory=lambda: SendRawMessageReqReceiveIDType(), metadata={"req_type": "query"}
    )  # 消息接收者id类型 open_id/user_id/union_id/email/chat_id, 示例值："open_id", 可选值有: `open_id`：以open_id来识别用户([什么是 Open ID？](https://open.feishu.cn/document/home/user-identity-introduction/open-id)), `user_id`：以user_id来识别用户。需要有获取用户 userID的权限 ([什么是 User ID？](https://open.feishu.cn/document/home/user-identity-introduction/user-id)), `union_id`：以union_id来识别用户([什么是 Union ID？](https://open.feishu.cn/document/home/user-identity-introduction/union-id)), `email`：以email来识别用户。是用户的真实邮箱, `chat_id`：以chat_id来识别群聊。可以调用接口 [搜索对用户或机器人可见的群列表](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat/search) 获取chat_id。群ID说明请参考：[群ID 说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat-id-description)
    receive_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 依据receive_id_type的值，填写对应的消息接收者id, 示例值："ou_7d8a6e6df7621556ce0d21922b676706ccs"
    content: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息内容为 json格式转义成string，格式说明参考: [发送消息content说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json), 示例值："{\"text\":\"<at user_id=\\\"ou_155184d1e73cbfb8973e5a9e698e74f2\\\">Tom</at> test content\"}"
    msg_type: SendRawMessageReqMsgType = attr.ib(
        factory=lambda: SendRawMessageReqMsgType(), metadata={"req_type": "json"}
    )  # 消息类型，包括：text、post、image、file、audio、media、sticker、interactive、share_chat、share_user, 示例值："text"


@attr.s
class SendRawMessageRespMentionIDType(object):
    pass


@attr.s
class SendRawMessageRespMention(object):
    key: str = attr.ib(default="", metadata={"req_type": "json"})  # mention key
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户open id
    id_type: SendRawMessageRespMentionIDType = attr.ib(
        factory=lambda: SendRawMessageRespMentionIDType(), metadata={"req_type": "json"}
    )  # id 可以是open_id，user_id或者union_id
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 被at用户的姓名
    tenant_key: str = attr.ib(default="", metadata={"req_type": "json"})  # tenant key


@attr.s
class SendRawMessageRespBody(object):
    content: str = attr.ib(default="", metadata={"req_type": "json"})  # 消息jsonContent


@attr.s
class SendRawMessageRespSenderIDType(object):
    pass


@attr.s
class SendRawMessageRespSender(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 该字段标识发送者的id
    id_type: SendRawMessageRespSenderIDType = attr.ib(
        factory=lambda: SendRawMessageRespSenderIDType(), metadata={"req_type": "json"}
    )  # 该字段标识发送者的id类型
    sender_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 该字段标识发送者的类型
    tenant_key: str = attr.ib(default="", metadata={"req_type": "json"})  # tenant key


@attr.s
class SendRawMessageRespMsgType(object):
    pass


@attr.s
class SendRawMessageResp(object):
    message_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息id open_message_id
    root_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 根消息id open_message_id
    parent_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 父消息的id open_message_id
    msg_type: SendRawMessageRespMsgType = attr.ib(
        factory=lambda: SendRawMessageRespMsgType(), metadata={"req_type": "json"}
    )  # 消息类型 text post card image等等
    create_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息生成的时间戳（毫秒）
    update_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息更新的时间戳（毫秒）
    deleted: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 消息是否被撤回
    updated: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 消息是否被更新
    chat_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 所属的群
    sender: SendRawMessageRespSender = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 发送者，可以是用户或应用
    body: SendRawMessageRespBody = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 消息内容，json结构，格式说明参考： [消息content说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/events/message_content)
    mentions: typing.List[SendRawMessageRespMention] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 被艾特的人或应用的id
    upper_message_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 上一层级的消息id open_message_id


def _gen_send_raw_message_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SendRawMessageResp,
        scope="Message",
        api="SendRawMessage",
        method="POST",
        url="https://open.feishu.cn/open-apis/im/v1/messages",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
