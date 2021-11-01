# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class SubscribeCalendarEventReq(object):
    calendar_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "calendar_id"}
    )  # 日历ID, 示例值："feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn"


@attr.s
class SubscribeCalendarEventResp(object):
    pass


def _gen_subscribe_calendar_event_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=SubscribeCalendarEventResp,
        scope="Calendar",
        api="SubscribeCalendarEvent",
        method="POST",
        url="https://open.feishu.cn/open-apis/calendar/v4/calendars/:calendar_id/events/subscription",
        body=request,
        method_option=_new_method_option(options),
        need_user_access_token=True,
    )
