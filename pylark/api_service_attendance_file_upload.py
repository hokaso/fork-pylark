# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class UploadAttendanceFileReq(object):
    file_name: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "file_name"}
    )  # 文件名
    file: typing.Union[str, bytes, io.BytesIO] = attr.ib(
        default=None, metadata={"req_type": "json", "key": "file"}
    )  # 文件


@attr.s
class UploadAttendanceFileRespFile(object):
    file_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "file_id"}
    )  # 文件 ID


@attr.s
class UploadAttendanceFileResp(object):
    file: UploadAttendanceFileRespFile = attr.ib(
        default=None, metadata={"req_type": "json", "key": "file"}
    )  # 文件


def _gen_upload_attendance_file_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UploadAttendanceFileResp,
        scope="Attendance",
        api="UploadAttendanceFile",
        method="POST",
        url="https://open.feishu.cn/open-apis/attendance/v1/files/upload",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        is_file=True,
    )
