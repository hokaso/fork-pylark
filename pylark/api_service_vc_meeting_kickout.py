# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class KickoutVCMeetingReqKickoutUser(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户ID, 示例值："ou_3ec3f6a28a0d08c45d895276e8e5e19b"
    user_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 用户类型, 示例值：1, 可选值有: `1`：lark用户, `2`：rooms用户, `3`：文档用户, `4`：neo单品用户, `5`：neo单品游客用户, `6`：pstn用户, `7`：sip用户


@attr.s
class KickoutVCMeetingReqUserIDType(object):
    pass


@attr.s
class KickoutVCMeetingReq(object):
    user_id_type: KickoutVCMeetingReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    meeting_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 会议ID, 示例值："6911188411932033028"
    kickout_users: typing.List[KickoutVCMeetingReqKickoutUser] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 需踢出的用户列表


@attr.s
class KickoutVCMeetingRespKickoutResult(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    user_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 用户类型, 可选值有: `1`：lark用户, `2`：rooms用户, `3`：文档用户, `4`：neo单品用户, `5`：neo单品游客用户, `6`：pstn用户, `7`：sip用户
    result: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 邀请结果, 可选值有: `1`：邀请成功, `2`：邀请失败


@attr.s
class KickoutVCMeetingResp(object):
    kickout_results: typing.List[KickoutVCMeetingRespKickoutResult] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 踢出结果


def _gen_kickout_vc_meeting_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=KickoutVCMeetingResp,
        scope="VC",
        api="KickoutVCMeeting",
        method="POST",
        url="https://open.feishu.cn/open-apis/vc/v1/meetings/:meeting_id/kickout",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
