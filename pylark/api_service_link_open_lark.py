# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class OpenLarkReq(object):
    pass


@attr.s
class OpenLarkResp(object):
    pass


def _gen_open_lark_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=OpenLarkResp,
        scope="AppLink",
        api="OpenLark",
        method="",
        url="https://applink.feishu.cn/client/op/open",
        body=request,
        method_option=_new_method_option(options),
    )
