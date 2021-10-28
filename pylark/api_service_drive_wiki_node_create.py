# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateWikiNodeReq(object):
    space_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 知识空间id, 示例值："6704147935988285963"
    obj_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文档类型，对于快捷方式，该字段是对应的实体的obj_type, 示例值："doc/sheet/mindnote", 可选值有: `doc`：doc, `sheet`：sheet, `mindnote`：mindnote, `bitable`：bitable
    parent_node_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 节点的父亲token, 示例值："wikcnKQ1k3pcuo5uSK4t8VN6kVf"
    node_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 节点类型, 示例值："origin/shortcut", 可选值有: `origin`：实体, `shortcut`：快捷方式
    origin_node_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 快捷方式对应的实体node_token，当创建节点为快捷方式时，需要传该值, 示例值："wikcnKQ1k3pcuo5uSK4t8VN6kVf"


@attr.s
class CreateWikiNodeRespNode(object):
    space_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 知识库id
    node_token: str = attr.ib(default="", metadata={"req_type": "json"})  # 节点token
    obj_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文档token，可以根据obj_type判断是属于doc、sheet还是mindnote的token(对于快捷方式，该字段是对应的实体的obj_token)
    obj_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 文档类型，对于快捷方式，该字段是对应的实体的obj_type, 可选值有: `doc`：doc, `sheet`：sheet, `mindnote`：mindnote, `bitable`：bitable
    parent_node_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 节点的父亲token
    node_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 节点类型, 可选值有: `origin`：实体, `shortcut`：快捷方式
    origin_node_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 快捷方式对应的实体node_token，当创建节点为快捷方式时，需要传该值
    origin_space_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 快捷方式对应的实体所在的spaceid
    has_child: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否有子节点
    title: str = attr.ib(default="", metadata={"req_type": "json"})  # 文档标题


@attr.s
class CreateWikiNodeResp(object):
    node: CreateWikiNodeRespNode = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 节点


def _gen_create_wiki_node_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateWikiNodeResp,
        scope="Drive",
        api="CreateWikiNode",
        method="POST",
        url="https://open.feishu.cn/open-apis/wiki/v2/spaces/:space_id/nodes",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
