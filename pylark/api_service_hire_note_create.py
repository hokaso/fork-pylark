# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateHireNoteReqUserIDType(object):
    pass


@attr.s
class CreateHireNoteReq(object):
    user_id_type: CreateHireNoteReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    talent_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 人才ID, 示例值："6891522620127185159"
    application_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 投递ID, 示例值："6891565231751825671"
    creator_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 创建人ID, 示例值："ou_0ab5d69b3848d44f4bf0751bffaa31db"
    content: str = attr.ib(default="", metadata={"req_type": "json"})  # 内容, 示例值："111"


@attr.s
class CreateHireNoteRespNote(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # ID备注
    talent_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 人才ID
    application_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 投递ID
    is_private: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否私密
    create_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 创建时间
    modify_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 更新时间
    creator_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 创建人ID
    content: str = attr.ib(default="", metadata={"req_type": "json"})  # 内容


@attr.s
class CreateHireNoteResp(object):
    note: CreateHireNoteRespNote = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 备注数据


def _gen_create_hire_note_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateHireNoteResp,
        scope="Hire",
        api="CreateHireNote",
        method="POST",
        url="https://open.feishu.cn/open-apis/hire/v1/notes",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
