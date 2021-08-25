# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class ResendAppTicketReq(object):
    app_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 应用唯一标识，创建应用后获得, 示例值："cli_slkdjalasdkjasd"
    app_secret: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 应用秘钥，创建应用后获得, 示例值："dskLLdkasdjlasdKK"


@attr.s
class ResendAppTicketResp(object):
    pass


def _gen_resend_app_ticket_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=ResendAppTicketResp,
        scope="Auth",
        api="ResendAppTicket",
        method="POST",
        url="https://open.feishu.cn/open-apis/auth/v3/app_ticket/resend",
        body=request,
        method_option=_new_method_option(options),
    )
