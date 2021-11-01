# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io
from pylark.lark_type_message_post import MessageContentPostAll


@attr.s
class SendRawMessageOldReqContent(object):
    text: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "text"}
    )  # 文本消息内容，文本消息中可以 at 个人或全体成员<br>at 全体成员：<at user_id="all">  </at> <br> at 个人：<at user_id="ou_xxxxxxx"></at>，user_id 为用户 user_id或者open_id
    post: MessageContentPostAll = attr.ib(
        default=None, metadata={"req_type": "json", "key": "post"}
    )  # 富文本消息


@attr.s
class SendRawMessageOldReq(object):
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "chat_id"}
    )  # 给用户发私聊消息，只需要填 open_id、email、user_id 中的一个即可，向群里发消息使用群的 chat_id。服务端依次读取字段的顺序为 chat_id > open_id > user_id > email   ( user_id 对应V3接口的 employee_id , chat_id 对应V3的 open_chat_id )
    open_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "open_id"}
    )  # 给用户发私聊消息，只需要填 open_id、email、user_id 中的一个即可，向群里发消息使用群的 chat_id。服务端依次读取字段的顺序为 chat_id > open_id > user_id > email   ( user_id 对应V3接口的 employee_id , chat_id 对应V3的 open_chat_id )
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 给用户发私聊消息，只需要填 open_id、email、user_id 中的一个即可，向群里发消息使用群的 chat_id。服务端依次读取字段的顺序为 chat_id > open_id > user_id > email   ( user_id 对应V3接口的 employee_id , chat_id 对应V3的 open_chat_id )
    email: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "email"}
    )  # 给用户发私聊消息，只需要填 open_id、email、user_id 中的一个即可，向群里发消息使用群的 chat_id。服务端依次读取字段的顺序为 chat_id > open_id > user_id > email   ( user_id 对应V3接口的 employee_id , chat_id 对应V3的 open_chat_id )
    root_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "root_id"}
    )  # 如果需要回复某条消息，填对应消息的消息 ID
    msg_type: lark_type.MsgType = attr.ib(
        factory=lambda: lark_type.MsgType(),
        metadata={"req_type": "json", "key": "msg_type"},
    )  # 消息类型，此处固定填 "text"
    content: SendRawMessageOldReqContent = attr.ib(
        default=None, metadata={"req_type": "json", "key": "content"}
    )  # 消息内容


@attr.s
class SendRawMessageOldResp(object):
    message_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "message_id"}
    )  # 消息 ID


def _gen_send_raw_message_old_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SendRawMessageOldResp,
        scope="Message",
        api="SendRawMessageOld",
        method="POST",
        url="https://open.feishu.cn/open-apis/message/v4/send/",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
