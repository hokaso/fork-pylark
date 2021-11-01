# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class GetWikiNodeListReq(object):
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # 分页大小, 示例值：10, 最大值：`50`
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："6946843325487456878"
    parent_node_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "parent_node_token"}
    )  # 父节点token, 示例值："wikcnKQ1k3pcuo5uSK4t8VN6kVf"
    space_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "space_id"}
    )  # 知识空间id, 示例值："6946843325487906839"


@attr.s
class GetWikiNodeListRespItem(object):
    space_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "space_id"}
    )  # 知识库id
    node_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "node_token"}
    )  # 节点token
    obj_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "obj_token"}
    )  # 文档token，可以根据obj_type判断是属于doc、sheet还是mindnote的token(对于快捷方式，该字段是对应的实体的obj_token)
    obj_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "obj_type"}
    )  # 文档类型，对于快捷方式，该字段是对应的实体的obj_type, 可选值有: `doc`：doc, `sheet`：sheet, `mindnote`：mindnote, `bitable`：bitable
    parent_node_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "parent_node_token"}
    )  # 节点的父亲token
    node_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "node_type"}
    )  # 节点类型, 可选值有: `origin`：实体, `shortcut`：快捷方式
    origin_node_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "origin_node_token"}
    )  # 快捷方式对应的实体node_token，当创建节点为快捷方式时，需要传该值
    origin_space_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "origin_space_id"}
    )  # 快捷方式对应的实体所在的spaceid
    has_child: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_child"}
    )  # 是否有子节点
    title: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "title"}
    )  # 文档标题


@attr.s
class GetWikiNodeListResp(object):
    items: typing.List[GetWikiNodeListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "items"}
    )  # 数据列表
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 是否还有更多项


def _gen_get_wiki_node_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetWikiNodeListResp,
        scope="Drive",
        api="GetWikiNodeList",
        method="GET",
        url="https://open.feishu.cn/open-apis/wiki/v2/spaces/:space_id/nodes",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
