# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class TerminateHireApplicationReq(object):
    application_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "application_id"}
    )  # 投递ID, 示例值："12312312312"
    termination_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "termination_type"}
    )  # 终止原因的类型, 示例值：1, 可选值有: `1`：我们拒绝了候选人, `22`：候选人拒绝了我们, `27`：其他
    termination_reason_list: typing.List[str] = attr.ib(
        factory=lambda: [],
        metadata={"req_type": "json", "key": "termination_reason_list"},
    )  # 终止的具体原因的id列表
    termination_reason_note: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "termination_reason_note"}
    )  # 终止备注, 示例值："不符合期望"


@attr.s
class TerminateHireApplicationResp(object):
    pass


def _gen_terminate_hire_application_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=TerminateHireApplicationResp,
        scope="Hire",
        api="TerminateHireApplication",
        method="POST",
        url="https://open.feishu.cn/open-apis/hire/v1/applications/:application_id/terminate",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
