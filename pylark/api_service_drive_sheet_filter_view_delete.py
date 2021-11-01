# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class DeleteSheetFilterViewReq(object):
    spreadsheet_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "spreadsheet_token"}
    )  # 表格 token, 示例值："shtcnmBA*****yGehy8"
    sheet_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "sheet_id"}
    )  # 子表 id, 示例值："0b**12"
    filter_view_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "filter_view_id"}
    )  # 筛选视图 id, 示例值："pH9hbVcCXA"


@attr.s
class DeleteSheetFilterViewResp(object):
    pass


def _gen_delete_sheet_filter_view_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=DeleteSheetFilterViewResp,
        scope="Drive",
        api="DeleteSheetFilterView",
        method="DELETE",
        url="https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
