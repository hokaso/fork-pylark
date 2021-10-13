# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateCalendarEventAttendeeReqAttendeeType(object):
    pass


@attr.s
class CreateCalendarEventAttendeeReqAttendee(object):
    type: CreateCalendarEventAttendeeReqAttendeeType = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 参与人类型；暂不支持创建邮箱参与人。, 示例值："user", 可选值有: `user`：用户, `chat`：群组, `resource`：会议室, `third_party`：邮箱
    is_optional: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 参与人是否为「可选参加」，无法编辑群参与人的此字段, 示例值：true, 默认值: `false`
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 参与人的用户id，依赖于user_id_type返回对应的取值，当is_external为true时，此字段只会返回open_id或者union_id, 示例值："ou_xxxxxxxx"
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # chat类型参与人的群组chat_id, 示例值："oc_xxxxxxxxx"
    room_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # resource类型参与人的会议室room_id, 示例值："omm_xxxxxxxx"
    third_party_email: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # third_party类型参与人的邮箱, 示例值："wangwu@email.com"
    operate_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 如果日程是使用应用身份创建的，在添加会议室的时候，用来指定会议室的联系人，在会议室视图展示。, 示例值："ou_xxxxxxxx"


@attr.s
class CreateCalendarEventAttendeeReqUserIDType(object):
    pass


@attr.s
class CreateCalendarEventAttendeeReq(object):
    user_id_type: CreateCalendarEventAttendeeReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    calendar_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 日历 ID, 示例值："feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn"
    event_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 日程 ID, 示例值："xxxxxxxxx_0"
    attendees: typing.List[CreateCalendarEventAttendeeReqAttendee] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 新增参与人列表
    need_notification: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 是否给参与人发送bot通知 默认为true, 示例值：false


@attr.s
class CreateCalendarEventAttendeeRespAttendeeChatMember(object):
    rsvp_status: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 参与人RSVP状态, 可选值有: `needs_action`：参与人尚未回复状态，或表示会议室预约中, `accept`：参与人回复接受，或表示会议室预约成功, `tentative`：参与人回复待定, `decline`：参与人回复拒绝，或表示会议室预约失败, `removed`：参与人或会议室已经从日程中被移除
    is_optional: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 参与人是否为「可选参加」
    display_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 参与人名称
    is_organizer: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 参与人是否为日程组织者
    is_external: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 参与人是否为外部参与人


@attr.s
class CreateCalendarEventAttendeeRespAttendeeType(object):
    pass


@attr.s
class CreateCalendarEventAttendeeRespAttendee(object):
    type: CreateCalendarEventAttendeeRespAttendeeType = attr.ib(
        factory=lambda: CreateCalendarEventAttendeeRespAttendeeType(),
        metadata={"req_type": "json"},
    )  # 参与人类型；暂不支持创建邮箱参与人。, 可选值有: `user`：用户, `chat`：群组, `resource`：会议室, `third_party`：邮箱
    attendee_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 参与人ID
    rsvp_status: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 参与人RSVP状态, 可选值有: `needs_action`：参与人尚未回复状态，或表示会议室预约中, `accept`：参与人回复接受，或表示会议室预约成功, `tentative`：参与人回复待定, `decline`：参与人回复拒绝，或表示会议室预约失败, `removed`：参与人或会议室已经从日程中被移除
    is_optional: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 参与人是否为「可选参加」，无法编辑群参与人的此字段
    is_organizer: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 参与人是否为日程组织者
    is_external: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 参与人是否为外部参与人；外部参与人不支持编辑
    display_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 参与人名称
    chat_members: typing.List[
        CreateCalendarEventAttendeeRespAttendeeChatMember
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 群中的群成员，当type为Chat时有效；群成员不支持编辑
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 参与人的用户id，依赖于user_id_type返回对应的取值，当is_external为true时，此字段只会返回open_id或者union_id
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # chat类型参与人的群组chat_id
    room_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # resource类型参与人的会议室room_id
    third_party_email: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # third_party类型参与人的邮箱
    operate_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 如果日程是使用应用身份创建的，在添加会议室的时候，用来指定会议室的联系人，在会议室视图展示。


@attr.s
class CreateCalendarEventAttendeeResp(object):
    attendees: typing.List[CreateCalendarEventAttendeeRespAttendee] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 新增参与人后的日程所有参与人列表


def _gen_create_calendar_event_attendee_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateCalendarEventAttendeeResp,
        scope="Calendar",
        api="CreateCalendarEventAttendee",
        method="POST",
        url="https://open.feishu.cn/open-apis/calendar/v4/calendars/:calendar_id/events/:event_id/attendees",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
