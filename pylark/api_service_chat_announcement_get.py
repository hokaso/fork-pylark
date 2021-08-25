# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetChatAnnouncementReqUserIDType(object):
    pass


@attr.s
class GetChatAnnouncementReq(object):
    user_id_type: GetChatAnnouncementReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值: "open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`，字段权限要求: 获取用户 user ID
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 待获取公告的群 ID, 示例值: "oc_5ad11d72b830411d72b836c20"


@attr.s
class GetChatAnnouncementRespModifierIDType(object):
    pass


@attr.s
class GetChatAnnouncementRespOwnerIDType(object):
    pass


@attr.s
class GetChatAnnouncementResp(object):
    content: str = attr.ib(default="", metadata={"req_type": "json"})  # 云文档序列化信息
    revision: str = attr.ib(default="", metadata={"req_type": "json"})  # 文档当前版本号 纯数字
    create_time: str = attr.ib(default="", metadata={"req_type": "json"})  # 文档生成的时间戳（秒）
    update_time: str = attr.ib(default="", metadata={"req_type": "json"})  # 文档更新的时间戳（秒）
    owner_id_type: GetChatAnnouncementRespOwnerIDType = attr.ib(
        factory=lambda: GetChatAnnouncementRespOwnerIDType(),
        metadata={"req_type": "json"},
    )  # 文档所有者 ID 类型, open_id/user_id/union_id/app_id, 可选值有: `user_id`：以 user_id 来识别用户, `union_id`：以 union_id 来识别用户, `open_id`：以 open_id 来识别用户, `app_id`：以 app_id 来识别应用
    owner_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 文档所有者 ID
    modifier_id_type: GetChatAnnouncementRespModifierIDType = attr.ib(
        factory=lambda: GetChatAnnouncementRespModifierIDType(),
        metadata={"req_type": "json"},
    )  # 文档最新修改者 id 类型, open_id/user_id/union_id/app_id, 可选值有: `user_id`：以 user_id 来识别用户, `union_id`：以 union_id 来识别用户, `open_id`：以 open_id 来识别用户, `app_id`：以 app_id 来识别应用
    modifier_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 文档最新修改者 id


def _gen_get_chat_announcement_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetChatAnnouncementResp,
        scope="Chat",
        api="GetChatAnnouncement",
        method="GET",
        url="https://open.feishu.cn/open-apis/im/v1/chats/:chat_id/announcement",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
