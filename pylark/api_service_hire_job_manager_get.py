# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetHireJobManagerReqUserIDType(object):
    pass


@attr.s
class GetHireJobManagerReq(object):
    user_id_type: GetHireJobManagerReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    job_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 职位ID, 示例值："1618209327096"
    manager_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 人员ID，目前传职位ID, 示例值："1618209327096"


@attr.s
class GetHireJobManagerRespInfo(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 职位ID
    recruiter_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 招聘负责人ID
    hiring_manager_id_list: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 用人经理ID列表
    assistant_id_list: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 协助人ID列表


@attr.s
class GetHireJobManagerResp(object):
    info: GetHireJobManagerRespInfo = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 职位负责人


def _gen_get_hire_job_manager_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHireJobManagerResp,
        scope="Hire",
        api="GetHireJobManager",
        method="GET",
        url="https://open.feishu.cn/open-apis/hire/v1/jobs/:job_id/managers/:manager_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
