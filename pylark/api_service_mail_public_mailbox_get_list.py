# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class GetPublicMailboxListReq(object):
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："xxx"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # 分页大小, 示例值：10, 最大值：`200`


@attr.s
class GetPublicMailboxListRespItem(object):
    public_mailbox_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "public_mailbox_id"}
    )  # 公共邮箱唯一标识
    email: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "email"}
    )  # 公共邮箱地址
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 公共邮箱名称


@attr.s
class GetPublicMailboxListResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 是否还有更多项
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    items: typing.List[GetPublicMailboxListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "items"}
    )  # 公共邮箱列表


def _gen_get_public_mailbox_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetPublicMailboxListResp,
        scope="Mail",
        api="GetPublicMailboxList",
        method="GET",
        url="https://open.feishu.cn/open-apis/mail/v1/public_mailboxes",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
