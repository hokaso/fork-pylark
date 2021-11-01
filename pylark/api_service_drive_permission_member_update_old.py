# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class UpdateDriveMemberPermissionOldReq(object):
    token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "token"}
    )  # 文件的 token，获取方式见 [对接前说明](https://open.feishu.cn/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)的第 4 项
    type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "type"}
    )  # 文档类型  "doc"  or  "sheet" or "file"
    member_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "member_type"}
    )  # 用户类型，可选 **"openid"、"openchat"、"userid"**
    member_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "member_id"}
    )  # 用户类型下的值
    perm: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "perm"}
    )  # 权限，"view" or "edit"
    notify_lark: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "notify_lark"}
    )  # 修改权限后是否飞书/lark通知对方<br>true 通知 or false 不通知


@attr.s
class UpdateDriveMemberPermissionOldResp(object):
    is_success: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_success"}
    )  # 是否操作成功


def _gen_update_drive_member_permission_old_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateDriveMemberPermissionOldResp,
        scope="Drive",
        api="UpdateDriveMemberPermissionOld",
        method="POST",
        url="https://open.feishu.cn/open-apis/drive/permission/member/update",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
