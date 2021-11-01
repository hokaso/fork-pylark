# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class GetACSDeviceListReq(object):
    pass


@attr.s
class GetACSDeviceListRespItem(object):
    device_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "device_id"}
    )  # 门禁设备 ID
    device_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "device_name"}
    )  # 设备名称
    device_sn: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "device_sn"}
    )  # 设备 SN 码


@attr.s
class GetACSDeviceListResp(object):
    items: typing.List[GetACSDeviceListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "items"}
    )  # -


def _gen_get_acs_device_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetACSDeviceListResp,
        scope="ACS",
        api="GetACSDeviceList",
        method="GET",
        url="https://open.feishu.cn/open-apis/acs/v1/devices",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
