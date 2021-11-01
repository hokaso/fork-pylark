# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class GetAttendanceUserAllowedRemedyReq(object):
    employee_type: lark_type.EmployeeType = attr.ib(
        factory=lambda: lark_type.EmployeeType(),
        metadata={"req_type": "query", "key": "employee_type"},
    )  # 请求体中的 user_id 的员工工号类型，必选字段，可用值：【employee_id（员工employeeId），employee_no（员工工号）】，示例值："employee_id"
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 用户 ID
    remedy_date: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "remedy_date"}
    )  # 查询补卡的日期


@attr.s
class GetAttendanceUserAllowedRemedyRespUserAllowedRemedys(object):
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "user_id"}
    )  # 用户 ID
    remedy_date: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "remedy_date"}
    )  # 补卡日期
    is_free_punch: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_free_punch"}
    )  # 是否为自由班次，若为自由班次，则不用选择考虑第几次上下班，直接选择补卡时间即可
    punch_no: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "punch_no"}
    )  # 第几次上下班，可用值：【0（第 1 次上下班），1（第 2 次上下班），2（第 3 次上下班）】
    work_type: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "work_type"}
    )  # 上班/下班，1：上班，2：下班
    punch_status: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "punch_status"}
    )  # 打卡状态，可用值【Early（早退），Late（迟到），Lack（缺卡）】
    normal_punch_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "normal_punch_time"}
    )  # 正常的应打卡时间，时间格式为 yyyy-MM-dd HH:mm
    remedy_start_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "remedy_start_time"}
    )  # 可选的补卡时间的最小值，时间格式为 yyyy-MM-dd HH:mm
    remedy_end_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "remedy_end_time"}
    )  # 可选的补卡时间的最大值，时间格式为 yyyy-MM-dd HH:mm


@attr.s
class GetAttendanceUserAllowedRemedyResp(object):
    user_allowed_remedys: GetAttendanceUserAllowedRemedyRespUserAllowedRemedys = (
        attr.ib(
            default=None, metadata={"req_type": "json", "key": "user_allowed_remedys"}
        )
    )


def _gen_get_attendance_user_allowed_remedy_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetAttendanceUserAllowedRemedyResp,
        scope="Attendance",
        api="GetAttendanceUserAllowedRemedy",
        method="POST",
        url="https://open.feishu.cn/open-apis/attendance/v1/user_task_remedys/query_user_allowed_remedys",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
