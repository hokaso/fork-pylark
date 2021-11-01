# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class DeleteMeetingRoomRoomReq(object):
    room_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "room_id"}
    )  # 要删除的会议室ID


@attr.s
class DeleteMeetingRoomRoomResp(object):
    pass


def _gen_delete_meeting_room_room_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteMeetingRoomRoomResp,
        scope="MeetingRoom",
        api="DeleteMeetingRoomRoom",
        method="POST",
        url="https://open.feishu.cn/open-apis/meeting_room/room/delete",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
