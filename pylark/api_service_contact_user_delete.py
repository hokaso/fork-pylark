# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class DeleteUserReq(object):
    user_id_type: lark_type.IDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    user_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "user_id"}
    )  # 用户ID，需要与查询参数中的user_id_type类型保持一致。, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    department_chat_acceptor_user_id: str = attr.ib(
        default="",
        metadata={"req_type": "json", "key": "department_chat_acceptor_user_id"},
    )  # 部门群接收者。被删除用户为部门群群主时，转让群主给指定接收者，不指定接收者则默认转让给群内第一个入群的人, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    external_chat_acceptor_user_id: str = attr.ib(
        default="",
        metadata={"req_type": "json", "key": "external_chat_acceptor_user_id"},
    )  # 外部群接收者。被删除用户为外部群群主时，转让群主给指定接收者，不指定接收者则默认转让给群内与被删除用户在同一组织的第一个入群的人，如果组织内只有该用户在群里，则解散外部群, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    docs_acceptor_user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "docs_acceptor_user_id"}
    )  # 文档接收者。用户被删除时，其拥有的文档转让给接收者，不指定接收者则默认转让给直接领导，如果无直接领导则直接删除文档资源, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    calendar_acceptor_user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "calendar_acceptor_user_id"}
    )  # 日程接收者。用户被删除时，其拥有的日程转让给接收者，不指定接收者则默认转让给直接领导，如果无直接领导则直接删除日程资源, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    application_acceptor_user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "application_acceptor_user_id"}
    )  # 应用接收者。用户被删除时，其创建的应用转让给接收者，不指定接收者则默认转让给直接领导，如果无直接领导则不会转移应用，会造成应用不可用, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    helpdesk_acceptor_user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "helpdesk_acceptor_user_id"}
    )  # 用户超文本帮助信息接收者, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"


@attr.s
class DeleteUserResp(object):
    pass


def _gen_delete_user_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteUserResp,
        scope="Contact",
        api="DeleteUser",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/contact/v3/users/:user_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
