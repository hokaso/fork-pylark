# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetDriveDocContentReq(object):
    doc_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 获取方式详见 [云文档接口快速入门](https://open.feishu.cn/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)


@attr.s
class GetDriveDocContentResp(object):
    content: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 详情参考[文档数据结构](https://open.feishu.cn/document/ukTMukTMukTM/ukDM2YjL5AjN24SOwYjN)
    revision: int = attr.ib(default=0, metadata={"req_type": "json"})  # 文档当前版本号


def _gen_get_drive_doc_content_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetDriveDocContentResp,
        scope="Drive",
        api="GetDriveDocContent",
        method="GET",
        url="https://open.feishu.cn/open-apis/doc/v2/:docToken/content",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
