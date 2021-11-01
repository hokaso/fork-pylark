# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class JoinChatReq(object):
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "chat_id"}
    )  # 群 ID，详情参见[群ID 说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat-id-description), 示例值："oc_a0553eda9014c201e6969b478895c230"


@attr.s
class JoinChatResp(object):
    pass


def _gen_join_chat_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=JoinChatResp,
        scope="Chat",
        api="JoinChat",
        method="PATCH",
        url="https://open.feishu.cn/open-apis/im/v1/chats/:chat_id/members/me_join",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
