# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class CreateMeetingRoomBuildingReq(object):
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 建筑名称
    floors: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "floors"}
    )  # 楼层列表
    country_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "country_id"}
    )  # 国家/地区ID
    district_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "district_id"}
    )  # 城市ID
    custom_building_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "custom_building_id"}
    )  # 租户自定义建筑ID


@attr.s
class CreateMeetingRoomBuildingResp(object):
    building_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "building_id"}
    )  # 成功创建的建筑ID


def _gen_create_meeting_room_building_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateMeetingRoomBuildingResp,
        scope="MeetingRoom",
        api="CreateMeetingRoomBuilding",
        method="POST",
        url="https://open.feishu.cn/open-apis/meeting_room/building/create",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
