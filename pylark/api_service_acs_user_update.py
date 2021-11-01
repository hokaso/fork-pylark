# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class UpdateACSUserReqFeature(object):
    card: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "card"}
    )  # 卡号, 示例值：123456


@attr.s
class UpdateACSUserReq(object):
    user_id_type: lark_type.IDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`,, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    user_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "user_id"}
    )  # 用户 ID, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    feature: UpdateACSUserReqFeature = attr.ib(
        default=None, metadata={"req_type": "json", "key": "feature"}
    )  # 用户特征


@attr.s
class UpdateACSUserResp(object):
    pass


def _gen_update_acs_user_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateACSUserResp,
        scope="ACS",
        api="UpdateACSUser",
        method="PATCH",
        url="https://open.feishu.cn/open-apis/acs/v1/users/:user_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
