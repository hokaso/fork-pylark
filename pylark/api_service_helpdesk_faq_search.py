# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class SearchHelpdeskFAQReq(object):
    query: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "query"}
    )  # 搜索query, 示例值："点餐"
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："6936004780707807251"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # 分页大小, 示例值：10, 最大值：`100`


@attr.s
class SearchHelpdeskFAQRespItem(object):
    faq_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "faq_id"}
    )  # 知识库ID
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 知识库旧版ID，请使用faq_id
    helpdesk_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "helpdesk_id"}
    )  # 服务台ID
    question: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "question"}
    )  # 问题
    answer: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "answer"}
    )  # 答案
    answer_richtext: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "answer_richtext"}
    )  # 富文本答案
    create_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "create_time"}
    )  # 创建时间
    update_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "update_time"}
    )  # 修改时间
    categories: typing.List[HelpdeskCategory] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "categories"}
    )  # 分类
    tags: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "tags"}
    )  # 关联词列表
    expire_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "expire_time"}
    )  # 失效时间


@attr.s
class SearchHelpdeskFAQResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 是否还有更多项
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    items: typing.List[SearchHelpdeskFAQRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "items"}
    )  # 知识库列表


def _gen_search_helpdesk_faq_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SearchHelpdeskFAQResp,
        scope="Helpdesk",
        api="SearchHelpdeskFAQ",
        method="GET",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/faqs/search",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_helpdesk_auth=True,
    )
