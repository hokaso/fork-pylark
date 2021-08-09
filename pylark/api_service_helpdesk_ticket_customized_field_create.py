# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class CreateHelpdeskTicketCustomizedFieldReqDropdownOptionsChildrenTagChildren(object):
    pass


@attr.s
class CreateHelpdeskTicketCustomizedFieldReqDropdownOptionsChildrenTag(object):
    display_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 展示名称
    children: CreateHelpdeskTicketCustomizedFieldReqDropdownOptionsChildrenTagChildren = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 同上：选项列表，只适用于多层下拉列表（最多可以设置三级下拉列表）


@attr.s
class CreateHelpdeskTicketCustomizedFieldReqDropdownOptionsChildren(object):
    tag: CreateHelpdeskTicketCustomizedFieldReqDropdownOptionsChildrenTag = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 选项ID


@attr.s
class CreateHelpdeskTicketCustomizedFieldReqDropdownOptions(object):
    children: CreateHelpdeskTicketCustomizedFieldReqDropdownOptionsChildren = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 选项列表


@attr.s
class CreateHelpdeskTicketCustomizedFieldReq(object):
    helpdesk_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 服务台ID, 示例值："1542164574896126"
    key_name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 键名, 示例值："test dropdown"
    display_name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 名称, 示例值："test dropdown"
    position: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段在列表后台管理列表中的位置, 示例值："3"
    field_type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 类型, 示例值："dropdown"
    description: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 描述, 示例值："下拉示例"
    visible: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否可见, 示例值：true
    editable: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否可以修改, 示例值：true
    required: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否必填, 示例值：false
    dropdown_options: CreateHelpdeskTicketCustomizedFieldReqDropdownOptions = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 下拉列表选项
    dropdown_allow_multiple: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 是否支持多选，仅在字段类型是dropdown的时候有效, 示例值：true


@attr.s
class CreateHelpdeskTicketCustomizedFieldResp(object):
    pass


def _gen_create_helpdesk_ticket_customized_field_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateHelpdeskTicketCustomizedFieldResp,
        scope="Helpdesk",
        api="CreateHelpdeskTicketCustomizedField",
        method="POST",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/ticket_customized_fields",
        body=request,
        method_option=_new_method_option(options),
    )
