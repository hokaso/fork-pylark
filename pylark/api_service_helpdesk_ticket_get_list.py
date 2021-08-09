# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetHelpdeskTicketListReqCustomizedFields(object):
    pass


@attr.s
class GetHelpdeskTicketListReq(object):
    ticket_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 搜索条件：工单ID, 示例值："123456"
    agent_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 搜索条件: 客服id, 示例值："ou_b5de90429xxx"
    closed_by_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 搜索条件: 关单客服id, 示例值："ou_b5de90429xxx"
    type: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 搜索条件: 工单类型 1:bot 2:人工, 示例值：1
    channel: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 搜索条件: 工单渠道, 示例值：0
    solved: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 搜索条件: 工单是否解决 1:没解决 2:已解决, 示例值：1
    score: int = attr.ib(default=0, metadata={"req_type": "query"})  # 搜索条件: 工单评分, 示例值：1
    status_list: typing.List[int] = attr.ib(
        factory=lambda: [], metadata={"req_type": "query"}
    )  # 搜索条件: 工单状态列表
    guest_name: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 搜索条件: 用户名称, 示例值："abc"
    guest_id: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 搜索条件: 用户id, 示例值："ou_b5de90429xxx"
    customized_fields: typing.List[GetHelpdeskTicketListReqCustomizedFields] = attr.ib(
        factory=lambda: [], metadata={"req_type": "query"}
    )  # 搜索条件: 自定义字段列表
    tags: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "query"}
    )  # 搜索条件: 用户标签列表
    page: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 页数, 从1开始, 默认为1, 示例值：1
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 当前页大小，最大为200, 默认为20。分页查询最多累计返回一万条数据，超过一万条请更改查询条件，推荐通过时间查询。, 示例值：20
    create_time_start: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 搜索条件: 工单创建起始时间 ms (也需要填上create_time_end)，相当于>=create_time_start, 示例值：1616920429000
    create_time_end: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 搜索条件: 工单创建结束时间 ms (也需要填上create_time_start)，相当于<=create_time_end, 示例值：1616920429000
    update_time_start: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 搜索条件: 工单修改起始时间 ms (也需要填上update_time_end), 示例值：1616920429000
    update_time_end: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 搜索条件: 工单修改结束时间 ms(也需要填上update_time_start), 示例值：1616920429000


@attr.s
class GetHelpdeskTicketListRespTicketCustomizedField(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 自定义字段ID
    value: str = attr.ib(default="", metadata={"req_type": "json"})  # 自定义字段值
    key_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 键名
    display_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 展示名称
    position: int = attr.ib(default=0, metadata={"req_type": "json"})  # 展示位置
    required: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否必填
    editable: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否可修改


@attr.s
class GetHelpdeskTicketListRespTicketCollaborator(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户名
    email: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户邮箱


@attr.s
class GetHelpdeskTicketListRespTicketClosedBy(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户名
    email: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户邮箱


@attr.s
class GetHelpdeskTicketListRespTicketAgent(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户名
    email: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户邮箱


@attr.s
class GetHelpdeskTicketListRespTicketGuest(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    avatar_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户名
    email: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户邮箱


@attr.s
class GetHelpdeskTicketListRespTicket(object):
    ticket_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 工单ID
    helpdesk_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 服务台ID
    guest: GetHelpdeskTicketListRespTicketGuest = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 工单创建用户
    stage: int = attr.ib(default=0, metadata={"req_type": "json"})  # 工单阶段，1：bot，2：人工
    status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 工单状态，1：已创建 2: 处理中 3: 排队中 4：待定 5：待用户响应 50: 被机器人关闭 51: 被人工关闭
    score: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 工单评分，1：不满意，2:一般，3:满意
    created_at: int = attr.ib(default=0, metadata={"req_type": "json"})  # 工单创建时间
    updated_at: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 工单更新时间，没有值时为-1
    closed_at: int = attr.ib(default=0, metadata={"req_type": "json"})  # 工单结束时间
    agents: typing.List[GetHelpdeskTicketListRespTicketAgent] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 工单客服
    channel: int = attr.ib(default=0, metadata={"req_type": "json"})  # 工单渠道
    solve: int = attr.ib(default=0, metadata={"req_type": "json"})  # 工单是否解决 1:没解决 2:已解决
    closed_by: GetHelpdeskTicketListRespTicketClosedBy = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 关单用户ID
    collaborators: typing.List[GetHelpdeskTicketListRespTicketCollaborator] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 工单协作者
    customized_fields: typing.List[
        GetHelpdeskTicketListRespTicketCustomizedField
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 自定义字段列表，没有值时不设置


@attr.s
class GetHelpdeskTicketListResp(object):
    total: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 工单总数 (单次请求最大为10000条)
    tickets: typing.List[GetHelpdeskTicketListRespTicket] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 工单


def _gen_get_helpdesk_ticket_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetHelpdeskTicketListResp,
        scope="Helpdesk",
        api="GetHelpdeskTicketList",
        method="GET",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/tickets",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
