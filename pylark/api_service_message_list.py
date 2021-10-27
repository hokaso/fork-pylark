# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetMessageListReqContainerIDType(object):
    pass


@attr.s
class GetMessageListReq(object):
    container_id_type: GetMessageListReqContainerIDType = attr.ib(
        factory=lambda: GetMessageListReqContainerIDType(),
        metadata={"req_type": "query"},
    )  # 容器类型 ，目前可选值仅有"chat", 示例值："chat"
    container_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 容器的id，即chat的id, 示例值："oc_234jsi43d3ssi993d43545f"
    start_time: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 历史信息的起始时间, 示例值："1609296809"
    end_time: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 历史信息的结束时间, 示例值："1608594809"
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："GxmvlNRvP0NdQZpa7yIqf_Lv_QuBwTQ8tXkX7w-irAghVD_TvuYd1aoJ1LQph86O-XImC4X9j9FhUPhXQDvtrQ=="
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10, 最大值：`50`


@attr.s
class GetMessageListRespItemMentionIDType(object):
    pass


@attr.s
class GetMessageListRespItemMention(object):
    key: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 被@的用户或机器人的序号。例如，第3个被@到的成员，值为“@_user_3”
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 被@的用户或者机器人的open_id
    id_type: GetMessageListRespItemMentionIDType = attr.ib(
        factory=lambda: GetMessageListRespItemMentionIDType(),
        metadata={"req_type": "json"},
    )  # 被@的用户或机器人 id 类型，目前仅支持 `open_id` ([什么是 Open ID？](https://open.feishu.cn/document/home/user-identity-introduction/open-id))
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 被@的用户或机器人的姓名
    tenant_key: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 为租户在飞书上的唯一标识，用来换取对应的tenant_access_token，也可以用作租户在应用里面的唯一标识


@attr.s
class GetMessageListRespItemBody(object):
    content: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息类型 包括：text、post、image、file、audio、media、sticker、interactive、share_chat、share_user等，类型定义请参考：[发送消息content说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json)


@attr.s
class GetMessageListRespItemSenderIDType(object):
    pass


@attr.s
class GetMessageListRespItemSender(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 该字段标识发送者的id
    id_type: GetMessageListRespItemSenderIDType = attr.ib(
        factory=lambda: GetMessageListRespItemSenderIDType(),
        metadata={"req_type": "json"},
    )  # 该字段标识发送者的id类型
    sender_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 该字段标识发送者的类型
    tenant_key: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 为租户在飞书上的唯一标识，用来换取对应的tenant_access_token，也可以用作租户在应用里面的唯一标识


@attr.s
class GetMessageListRespItemMsgType(object):
    pass


@attr.s
class GetMessageListRespItem(object):
    message_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息id，说明参见：[消息ID说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/intro#ac79c1c2)
    root_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 根消息id，说明参见：[消息ID说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/intro#ac79c1c2)
    parent_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 父消息的id，说明参见：[消息ID说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/intro#ac79c1c2)
    msg_type: GetMessageListRespItemMsgType = attr.ib(
        factory=lambda: GetMessageListRespItemMsgType(), metadata={"req_type": "json"}
    )  # 消息类型 包括：text、post、image、file、audio、media、sticker、interactive、share_chat、share_user等，类型定义请参考[发送消息content说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json)
    create_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息生成的时间戳（毫秒）
    update_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 消息更新的时间戳（毫秒）
    deleted: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 消息是否被撤回
    updated: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 消息是否被更新
    chat_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 所属的群
    sender: GetMessageListRespItemSender = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 发送者，可以是用户或应用
    body: GetMessageListRespItemBody = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 消息内容
    mentions: typing.List[GetMessageListRespItemMention] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 被@的用户或机器人的id列表
    upper_message_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 合并转发消息中，上一层级的消息id message_id，说明参见：[消息ID说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/intro#ac79c1c2)


@attr.s
class GetMessageListResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    items: typing.List[GetMessageListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # message[]


def _gen_get_message_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetMessageListResp,
        scope="Message",
        api="GetMessageList",
        method="GET",
        url="https://open.feishu.cn/open-apis/im/v1/messages",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
