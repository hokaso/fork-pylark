# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class UpdateHelpdeskCategoryReq(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "id"}
    )  # category id, 示例值："6948728206392295444"
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 名称, 示例值："创建团队和邀请成员"
    parent_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "parent_id"}
    )  # 父知识库分类ID, 示例值："0"


@attr.s
class UpdateHelpdeskCategoryResp(object):
    pass


def _gen_update_helpdesk_category_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateHelpdeskCategoryResp,
        scope="Helpdesk",
        api="UpdateHelpdeskCategory",
        method="PATCH",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/categories/:id",
        body=request,
        method_option=_new_method_option(options),
        need_user_access_token=True,
        need_helpdesk_auth=True,
    )
