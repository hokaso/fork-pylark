# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class CreateDriveFolderReq(object):
    folder_token: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "folderToken"}
    )  # 文件夹的 token，获取方式见 [概述](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/files/guide/introduction)
    title: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "title"}
    )  # 文件夹标题


@attr.s
class CreateDriveFolderResp(object):
    url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "url"}
    )  # 新创建文件夹的 url
    revision: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "revision"}
    )  # 新创建文件夹的版本号
    token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "token"}
    )  # 新创建文件夹的 token


def _gen_create_drive_folder_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateDriveFolderResp,
        scope="Drive",
        api="CreateDriveFolder",
        method="POST",
        url="https://open.feishu.cn/open-apis/drive/explorer/v2/folder/:folderToken",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
