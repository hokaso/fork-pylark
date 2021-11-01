# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class UncompleteTaskReq(object):
    task_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "task_id"}
    )  # 任务 ID, 示例值："bb54ab99-d360-434f-bcaa-a4cc4c05840e"


@attr.s
class UncompleteTaskResp(object):
    pass


def _gen_uncomplete_task_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UncompleteTaskResp,
        scope="Task",
        api="UncompleteTask",
        method="POST",
        url="https://open.feishu.cn/open-apis/task/v1/tasks/:task_id/uncomplete",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
