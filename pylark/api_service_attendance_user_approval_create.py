# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class CreateAttendanceUserApprovalReqUserApprovalTrip(object):
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 开始时间，时间格式为 yyyy-MM-dd HH:mm:ss
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss
    reason: str = attr.ib(default="", metadata={"req_type": "json"})  # 出差理由
    approve_pass_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批通过时间，时间格式为 yyyy-MM-dd HH:mm:ss
    approve_apply_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批申请时间，时间格式为 yyyy-MM-dd HH:mm:ss


@attr.s
class CreateAttendanceUserApprovalReqUserApprovalOvertimeWorkDuration(object):
    pass


@attr.s
class CreateAttendanceUserApprovalReqUserApprovalOvertimeWork(object):
    duration: float = attr.ib(default=None, metadata={"req_type": "json"})  # 加班时长
    unit: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 加班时长单位，可用值：【1（天），2（小时）】
    category: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 加班日期类型，可用值：【1（工作日），2（休息日），3（节假日）】
    type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 加班规则类型，可用值：【0（不关联加班规则），1（调休），2（加班费）】
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 开始时间，时间格式为 yyyy-MM-dd HH:mm:ss
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss


@attr.s
class CreateAttendanceUserApprovalReqUserApprovalLeaveI18nNames(object):
    ch: str = attr.ib(default="", metadata={"req_type": "json"})  # 中文描述
    en: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文描述
    ja: str = attr.ib(default="", metadata={"req_type": "json"})  # 日文描述


@attr.s
class CreateAttendanceUserApprovalReqUserApprovalLeave(object):
    uniq_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 假期类型唯一 ID，代表一种假期类型，长度小于 14
    unit: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 假期时长单位，可用值：【1（天），2（小时），3（半天），4（半小时）】
    interval: int = attr.ib(default=0, metadata={"req_type": "json"})  # 假期时长（单位秒）
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 开始时间，时间格式为 yyyy-MM-dd HH:mm:ss
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss
    i18n_names: CreateAttendanceUserApprovalReqUserApprovalLeaveI18nNames = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 假期多语言展示，格式为 map，key 为["ch"、"en"、"ja"]，其中 ch 代表中文，en 代表英文、ja 代表日文
    default_locale: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 默认语言类型，由于飞书客户端支持中、英、日三种语言，当用户切换语言时，如果假期名称没有所对应语言的名称，则会使用默认语言的名称，可用值：【ch（中文），en（英文），ja（日文）】
    reason: str = attr.ib(default="", metadata={"req_type": "json"})  # 请假理由，必选字段


@attr.s
class CreateAttendanceUserApprovalReqUserApprovalOutI18nNamesJa(object):
    pass


@attr.s
class CreateAttendanceUserApprovalReqUserApprovalOutI18nNames(object):
    ch: str = attr.ib(default="", metadata={"req_type": "json"})  # 中文描述
    en: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文描述
    ja: CreateAttendanceUserApprovalReqUserApprovalOutI18nNamesJa = attr.ib(
        factory=lambda: CreateAttendanceUserApprovalReqUserApprovalOutI18nNamesJa(),
        metadata={"req_type": "json"},
    )  # 日文描述


@attr.s
class CreateAttendanceUserApprovalReqUserApprovalOut(object):
    uniq_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 外出类型唯一 ID，代表一种外出类型，长度小于 14
    unit: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 外出时长单位，可用值：【1（天），2（小时），3（半天），4（半小时）】
    interval: int = attr.ib(default=0, metadata={"req_type": "json"})  # 假期时长（单位秒）
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 开始时间，时间格式为 yyyy-MM-dd HH:mm:ss
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss
    i18n_names: CreateAttendanceUserApprovalReqUserApprovalOutI18nNames = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 外出多语言展示，格式为 map，key 为["ch"、"en"、"ja"]，其中 ch 代表中文，en 代表英文、ja 代表日文
    default_locale: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 默认语言类型，由于飞书客户端支持中、英、日三种语言，当用户切换语言时，如果外出名称没有所对应语言的名称，则会使用默认语言的名称
    reason: str = attr.ib(default="", metadata={"req_type": "json"})  # 外出理由


@attr.s
class CreateAttendanceUserApprovalReqUserApproval(object):
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批用户
    date: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批作用时间
    outs: typing.List[CreateAttendanceUserApprovalReqUserApprovalOut] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 外出信息
    leaves: typing.List[CreateAttendanceUserApprovalReqUserApprovalLeave] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 请假信息
    overtime_works: typing.List[
        CreateAttendanceUserApprovalReqUserApprovalOvertimeWork
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 加班信息
    trips: typing.List[CreateAttendanceUserApprovalReqUserApprovalTrip] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 出差信息


@attr.s
class CreateAttendanceUserApprovalReqEmployeeType(object):
    pass


@attr.s
class CreateAttendanceUserApprovalReq(object):
    employee_type: CreateAttendanceUserApprovalReqEmployeeType = attr.ib(
        factory=lambda: CreateAttendanceUserApprovalReqEmployeeType(),
        metadata={"req_type": "query"},
    )  # 请求体中的 user_id 的员工工号类型，必选字段，可用值：【employee_id（员工employeeId），employee_no（员工工号）】，示例值："employee_id"
    user_approval: CreateAttendanceUserApprovalReqUserApproval = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 审批信息


@attr.s
class CreateAttendanceUserApprovalRespUserApprovalTrip(object):
    approval_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例ID
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 开始时间，时间格式为 yyyy-MM-dd HH:mm:ss
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss
    reason: str = attr.ib(default="", metadata={"req_type": "json"})  # 出差理由
    approve_pass_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批通过时间，时间格式为 yyyy-MM-dd HH:mm:ss
    approve_apply_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批申请时间，时间格式为 yyyy-MM-dd HH:mm:ss


@attr.s
class CreateAttendanceUserApprovalRespUserApprovalOvertimeWorkDuration(object):
    pass


@attr.s
class CreateAttendanceUserApprovalRespUserApprovalOvertimeWork(object):
    approval_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例ID
    duration: float = attr.ib(default=None, metadata={"req_type": "json"})  # 加班时长
    unit: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 加班时长单位，可用值：【1（天），2（小时）】
    category: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 加班日期类型，可用值：【1（工作日），2（休息日），3（节假日）】
    type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 加班规则类型，可用值：【0（不关联加班规则），1（调休），2（加班费），3（关联加班规则，没有调休或加班费）】
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 开始时间，时间格式为 yyyy-MM-dd HH:mm:ss
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss


@attr.s
class CreateAttendanceUserApprovalRespUserApprovalLeaveI18nNames(object):
    ch: str = attr.ib(default="", metadata={"req_type": "json"})  # 中文描述
    en: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文描述
    ja: str = attr.ib(default="", metadata={"req_type": "json"})  # 日文描述


@attr.s
class CreateAttendanceUserApprovalRespUserApprovalLeave(object):
    approval_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例ID
    uniq_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 假期类型唯一 ID，代表一种假期类型，长度小于 14
    unit: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 假期时长单位，可用值：【1（天），2（小时），3（半天），4（半小时）】
    interval: int = attr.ib(default=0, metadata={"req_type": "json"})  # 假期时长（单位秒）
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 开始时间，时间格式为 yyyy-MM-dd HH:mm:ss
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss
    i18n_names: CreateAttendanceUserApprovalRespUserApprovalLeaveI18nNames = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 假期多语言展示，格式为 map，key 为["ch"、"en"、"ja"]，其中 ch 代表中文，en 代表英文、ja 代表日文
    default_locale: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 默认语言类型，由于飞书客户端支持中、英、日三种语言，当用户切换语言时，如果假期名称没有所对应语言的名称，则会使用默认语言的名称，可用值：【ch（中文），en（英文），ja（日文）】
    reason: str = attr.ib(default="", metadata={"req_type": "json"})  # 请假理由
    approve_pass_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批通过时间，时间格式为 yyyy-MM-dd HH:mm:ss
    approve_apply_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批申请时间，时间格式为 yyyy-MM-dd HH:mm:ss


@attr.s
class CreateAttendanceUserApprovalRespUserApprovalOutI18nNames(object):
    ch: str = attr.ib(default="", metadata={"req_type": "json"})  # 中文描述
    en: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文描述
    ja: str = attr.ib(default="", metadata={"req_type": "json"})  # 日文描述


@attr.s
class CreateAttendanceUserApprovalRespUserApprovalOut(object):
    approval_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批实例ID
    uniq_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 外出类型唯一 ID，代表一种外出类型，长度小于 14
    unit: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 外出时长单位，可用值：【1（天），2（小时），3（半天），4（半小时）】
    interval: int = attr.ib(default=0, metadata={"req_type": "json"})  # 假期时长（单位秒）
    start_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 开始时间，时间格式为 yyyy-MM-dd HH:mm:ss
    end_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 结束时间，时间格式为 yyyy-MM-dd HH:mm:ss
    i18n_names: CreateAttendanceUserApprovalRespUserApprovalOutI18nNames = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 外出多语言展示，格式为 map，key 为["ch"、"en"、"ja"]，其中 ch 代表中文，en 代表英文、ja 代表日文
    default_locale: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 默认语言类型，由于飞书客户端支持中、英、日三种语言，当用户切换语言时，如果外出名称没有所对应语言的名称，则会使用默认语言的名称
    reason: str = attr.ib(default="", metadata={"req_type": "json"})  # 外出理由
    approve_pass_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批通过时间
    approve_apply_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 审批申请时间


@attr.s
class CreateAttendanceUserApprovalRespUserApproval(object):
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批用户 ID
    date: str = attr.ib(default="", metadata={"req_type": "json"})  # 审批作用时间
    outs: typing.List[CreateAttendanceUserApprovalRespUserApprovalOut] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 外出信息
    leaves: typing.List[CreateAttendanceUserApprovalRespUserApprovalLeave] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 请假信息
    overtime_works: typing.List[
        CreateAttendanceUserApprovalRespUserApprovalOvertimeWork
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 加班信息
    trips: typing.List[CreateAttendanceUserApprovalRespUserApprovalTrip] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 出差信息


@attr.s
class CreateAttendanceUserApprovalResp(object):
    user_approvals: typing.List[CreateAttendanceUserApprovalRespUserApproval] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 审批结果列表


def _gen_create_attendance_user_approval_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateAttendanceUserApprovalResp,
        scope="Attendance",
        api="CreateAttendanceUserApproval",
        method="POST",
        url="https://open.feishu.cn/open-apis/attendance/v1/user_approvals",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
