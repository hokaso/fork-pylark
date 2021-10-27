# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class DeleteChatMemberReqMemberIDType(object):
    pass


@attr.s
class DeleteChatMemberReq(object):
    member_id_type: DeleteChatMemberReqMemberIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 出群成员 id 类型 open_id/user_id/union_id/app_id, 示例值："user_id", 可选值有: `user_id`：以 user_id 来识别成员, `union_id`：以 union_id 来识别成员, `open_id`：以 open_id 来识别成员, `app_id`：以 app_id 来识别成员
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 群 ID，详情参见[群ID 说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat-id-description), 示例值："oc_a0553eda9014c201e6969b478895c230"
    id_list: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 成员列表


@attr.s
class DeleteChatMemberResp(object):
    invalid_id_list: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 无效成员列表


def _gen_delete_chat_member_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteChatMemberResp,
        scope="Chat",
        api="DeleteChatMember",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/im/v1/chats/:chat_id/members",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
