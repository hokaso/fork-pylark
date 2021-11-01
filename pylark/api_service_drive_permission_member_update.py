# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class UpdateDriveMemberPermissionReq(object):
    need_notification: bool = attr.ib(
        default=None, metadata={"req_type": "query", "key": "need_notification"}
    )  # 更新权限后是否通知对方, 示例值：false, 默认值: `false`
    type: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "type"}
    )  # 文件类型，放于query参数中，如：`?type=doc`, 示例值："doc", 可选值有: `doc`：文档, `sheet`：电子表格, `file`：云空间文件, `wiki`：知识库节点, `bitable`：多维表格, `docx`：文档（暂不支持）
    token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "token"}
    )  # 文件的 token，获取方式见 [概述](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/files/guide/introduction), 示例值："doccnBKgoMyY5OMbUG6FioTXuBe"
    member_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "member_id"}
    )  # 权限成员的openID，获取方式见 [如何获得 User ID、Open ID 和 Union ID？](https://open.feishu.cn/document/home/user-identity-introduction/how-to-get), 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    member_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "member_type"}
    )  # 用户类型，与路径参数中的`member_id`要对应，可选值有：, `email`: 飞书企业邮箱, `openid`: 开放平台ID, `openchat`: 开放平台群组, `opendepartmentid`: 开放平台部门ID, `userid`: 用户自定义ID, 示例值："openid"
    perm: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "perm"}
    )  # 需要更新的权限，可选值有：, `view`: 可阅读, `edit`: 可编辑, `full_access`: 所有权限, 示例值："view"


@attr.s
class UpdateDriveMemberPermissionRespMember(object):
    member_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "member_type"}
    )  # 用户类型，与路径参数中的`member_id`要对应，可选值有：, `email`: 飞书企业邮箱, `openid`: 开放平台ID, `openchat`: 开放平台群组, `opendepartmentid`: 开放平台部门ID, `userid`: 用户自定义ID
    member_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "member_id"}
    )  # 用户类型下的值
    perm: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "perm"}
    )  # 需要更新的权限，可选值有：, `view`: 可阅读, `edit`: 可编辑, `full_access`: 所有权限


@attr.s
class UpdateDriveMemberPermissionResp(object):
    member: UpdateDriveMemberPermissionRespMember = attr.ib(
        default=None, metadata={"req_type": "json", "key": "member"}
    )  # 本次更新权限的用户信息


def _gen_update_drive_member_permission_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateDriveMemberPermissionResp,
        scope="Drive",
        api="UpdateDriveMemberPermission",
        method="PUT",
        url="https://open.feishu.cn/open-apis/drive/v1/permissions/:token/members/:member_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
