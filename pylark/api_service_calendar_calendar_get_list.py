# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class GetCalendarListReq(object):
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # 一次请求要求返回最大数量，默认500，取值范围为[50. 1000], 示例值：10, 默认值: `500`, 取值范围：`50` ～ `1000`
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 上次请求Response返回的分页标记，首次请求时为空, 示例值："xxxxx"
    sync_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "sync_token"}
    )  # 上次请求Response返回的增量同步标记，分页请求未结束时为空, 示例值："ListCalendarsSyncToken_xxx"


@attr.s
class GetCalendarListRespCalendar(object):
    calendar_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "calendar_id"}
    )  # 日历ID
    summary: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "summary"}
    )  # 日历标题, 最大长度：`255` 字符
    description: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "description"}
    )  # 日历描述, 最大长度：`255` 字符
    permissions: lark_type.CalendarPermission = attr.ib(
        factory=lambda: lark_type.CalendarPermission(),
        metadata={"req_type": "json", "key": "permissions"},
    )  # 日历公开范围, 可选值有: `private`：私密, `show_only_free_busy`：仅展示忙闲信息, `public`：他人可查看日程详情
    color: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "color"}
    )  # 日历颜色，颜色RGB值的int32表示。客户端展示时会映射到色板上最接近的一种颜色。仅对当前身份生效
    type: lark_type.CalendarType = attr.ib(
        factory=lambda: lark_type.CalendarType(),
        metadata={"req_type": "json", "key": "type"},
    )  # 日历类型, 可选值有: `unknown`：未知类型, `primary`：用户或应用的主日历, `shared`：由用户或应用创建的共享日历, `google`：用户绑定的谷歌日历, `resource`：会议室日历, `exchange`：用户绑定的Exchange日历
    summary_alias: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "summary_alias"}
    )  # 日历备注名，修改或添加后仅对当前身份生效, 最大长度：`255` 字符
    is_deleted: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_deleted"}
    )  # 对于当前身份，日历是否已经被标记为删除, 默认值: `false`
    is_third_party: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_third_party"}
    )  # 当前日历是否是第三方数据；三方日历及日程只支持读，不支持写入, 默认值: `false`
    role: lark_type.CalendarRole = attr.ib(
        factory=lambda: lark_type.CalendarRole(),
        metadata={"req_type": "json", "key": "role"},
    )  # 当前身份对于该日历的访问权限, 可选值有: `unknown`：未知权限, `free_busy_reader`：游客，只能看到忙碌/空闲信息, `reader`：订阅者，查看所有日程详情, `writer`：编辑者，创建及修改日程, `owner`：管理员，管理日历及共享设置


@attr.s
class GetCalendarListResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 是否有下一页数据
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 下次请求需要带上的分页标记，90 天有效期
    sync_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "sync_token"}
    )  # 下次请求需要带上的增量同步标记，90 天有效期
    calendar_list: typing.List[GetCalendarListRespCalendar] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "calendar_list"}
    )  # 分页加载的日历数据列表


def _gen_get_calendar_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetCalendarListResp,
        scope="Calendar",
        api="GetCalendarList",
        method="GET",
        url="https://open.feishu.cn/open-apis/calendar/v4/calendars",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
