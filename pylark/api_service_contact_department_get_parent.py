# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class GetParentDepartmentReq(object):
    user_id_type: lark_type.IDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    department_id_type: lark_type.DepartmentIDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "department_id_type"}
    )  # 此次调用中使用的部门ID的类型, 示例值："open_department_id", 可选值有: `department_id`：以自定义department_id来标识部门, `open_department_id`：以open_department_id来标识部门
    department_id: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "department_id"}
    )  # 部门ID, 示例值："od-4e6ac4d14bcd5071a37a39de902c7141"
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："AQD9/Rn9eij9Pm39ED40/RD/cIFmu77WxpxPB/2oHfQLZ%2BG8JG6tK7%2BZnHiT7COhD2hMSICh/eBl7cpzU6JEC3J7COKNe4jrQ8ExwBCR"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # 分页大小, 示例值：10, 最大值：`50`


@attr.s
class GetParentDepartmentRespItemStatus(object):
    is_deleted: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_deleted"}
    )  # 是否被删除


@attr.s
class GetParentDepartmentRespItemI18nName(object):
    zh_cn: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "zh_cn"}
    )  # 部门的中文名
    ja_jp: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "ja_jp"}
    )  # 部门的日文名
    en_us: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "en_us"}
    )  # 部门的英文名


@attr.s
class GetParentDepartmentRespItem(object):
    name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "name"}
    )  # 部门名称,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录
    i18n_name: GetParentDepartmentRespItemI18nName = attr.ib(
        default=None, metadata={"req_type": "json", "key": "i18n_name"}
    )  # 国际化的部门名称,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录
    parent_department_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "parent_department_id"}
    )  # 父部门的ID,* 创建根部门，该参数值为 “0”,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    department_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "department_id"}
    )  # 本部门的自定义部门ID,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录
    open_department_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "open_department_id"}
    )  # 部门的open_id
    leader_user_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "leader_user_id"}
    )  # 部门主管用户ID,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "chat_id"}
    )  # 部门群ID,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录
    order: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "order"}
    )  # 部门的排序，即部门在其同级部门的展示顺序,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    unit_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "unit_ids"}
    )  # 部门单位自定义ID列表，当前只支持一个,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    member_count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "member_count"}
    )  # 部门下用户的个数,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    status: GetParentDepartmentRespItemStatus = attr.ib(
        default=None, metadata={"req_type": "json", "key": "status"}
    )  # 部门状态,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录


@attr.s
class GetParentDepartmentResp(object):
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 是否还有更多项
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    items: typing.List[GetParentDepartmentRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "items"}
    )


def _gen_get_parent_department_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetParentDepartmentResp,
        scope="Contact",
        api="GetParentDepartment",
        method="GET",
        url="https://open.feishu.cn/open-apis/contact/v3/departments/parent",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
