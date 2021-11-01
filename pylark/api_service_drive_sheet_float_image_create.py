# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class CreateSheetFloatImageReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "spreadsheet_token"}
    )  # 表格 token, 示例值："shtcnmBA*****yGehy8"
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "sheet_id"}
    )  # 子表 id, 示例值："0b**12"
    float_image_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "float_image_id"}
    )  # 浮动图片 id, 示例值："ye06SS14ph"
    float_image_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "float_image_token"}
    )  # 【更新时不用传，创建需要】浮动图片 token，需要先上传图片到表格获得此 token 之后再进行浮动图片的相关操作, 示例值："boxbcbQsaSqIXsxxxxx1HCPJFbh"
    range_: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "range"}
    )  # 浮动图片的左上角单元格定位，只支持一个单元格, 示例值："0b**12!A1:A1"
    width: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "width"}
    )  # 浮动图片的宽度，大于等于 20px, 示例值：100
    height: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "height"}
    )  # 浮动图片的高度，大于等于 20px, 示例值：100
    offset_x: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "offset_x"}
    )  # 浮动图片左上角所在位置相对于所在单元格左上角的横向偏移，大于等于0且小于所在单元格的宽度, 示例值：0
    offset_y: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "offset_y"}
    )  # 浮动图片左上角所在位置相对于所在单元格左上角的纵向偏移，大于等于0且小于所在单元格的高度, 示例值：0


@attr.s
class CreateSheetFloatImageRespFloatImage(object):
    float_image_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "float_image_id"}
    )  # 浮动图片 id
    float_image_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "float_image_token"}
    )  # 【更新时不用传，创建需要】浮动图片 token，需要先上传图片到表格获得此 token 之后再进行浮动图片的相关操作
    range_: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "range"}
    )  # 浮动图片的左上角单元格定位，只支持一个单元格
    width: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "width"}
    )  # 浮动图片的宽度，大于等于 20px
    height: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "height"}
    )  # 浮动图片的高度，大于等于 20px
    offset_x: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "offset_x"}
    )  # 浮动图片左上角所在位置相对于所在单元格左上角的横向偏移，大于等于0且小于所在单元格的宽度
    offset_y: float = attr.ib(
        default=None, metadata={"req_type": "json", "key": "offset_y"}
    )  # 浮动图片左上角所在位置相对于所在单元格左上角的纵向偏移，大于等于0且小于所在单元格的高度


@attr.s
class CreateSheetFloatImageResp(object):
    float_image: CreateSheetFloatImageRespFloatImage = attr.ib(
        default=None, metadata={"req_type": "json", "key": "float_image"}
    )  # 浮动图片返回值


def _gen_create_sheet_float_image_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateSheetFloatImageResp,
        scope="Drive",
        api="CreateSheetFloatImage",
        method="POST",
        url="https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/float_images",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
