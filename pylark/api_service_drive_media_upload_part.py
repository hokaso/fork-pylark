# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class PartUploadDriveMediaReq(object):
    upload_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "upload_id"}
    )  # 分片上传事务ID, 示例值："123456"
    seq: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "seq"}
    )  # 块号，从0开始计数, 示例值：0
    size: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "size"}
    )  # 块大小, 示例值：4194304
    checksum: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "checksum"}
    )  # 文件分块adler32校验和(可选), 示例值："12345678"
    file: typing.Union[str, bytes, io.BytesIO] = attr.ib(
        default=None, metadata={"req_type": "json", "key": "file"}
    )  # 文件分片内容, 示例值：file binary


@attr.s
class PartUploadDriveMediaResp(object):
    pass


def _gen_part_upload_drive_media_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=PartUploadDriveMediaResp,
        scope="Drive",
        api="PartUploadDriveMedia",
        method="POST",
        url="https://open.feishu.cn/open-apis/drive/v1/medias/upload_part",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
        is_file=True,
    )
