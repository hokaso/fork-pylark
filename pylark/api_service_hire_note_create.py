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
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, `people_admin_id`：以people_admin_id来识别用户, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    talent_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 人才ID, 示例值："6916472453069883661"
    application_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 投递ID, 示例值："6891565253964859661"
    creator_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 创建人ID, 示例值："ou_f476cb099ac9227c9bae09ce46112579"
    content: str = attr.ib(default="", metadata={"req_type": "json"})  # 内容, 示例值："测试5"
    privacy: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 备注私密属性（默认为公开）, 示例值：1, 可选值有: `1`：私密, `2`：公开


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
    )  # 备注信息


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
