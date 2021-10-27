# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class CreateDepartmentReqI18nName(object):
    zh_cn: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 部门的中文名, 示例值："Demo名称"
    ja_jp: str = attr.ib(default="", metadata={"req_type": "json"})  # 部门的日文名, 示例值："デモ名"
    en_us: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 部门的英文名, 示例值："Demo Name"


@attr.s
class CreateDepartmentReqDepartmentIDType(object):
    pass


@attr.s
class CreateDepartmentReqUserIDType(object):
    pass


@attr.s
class CreateDepartmentReq(object):
    user_id_type: CreateDepartmentReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    department_id_type: CreateDepartmentReqDepartmentIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 此次调用中使用的部门ID的类型, 示例值："open_department_id", 可选值有: `department_id`：以自定义department_id来标识部门, `open_department_id`：以open_department_id来标识部门
    client_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 根据client_token是否一致来判断是否为同一请求, 示例值："473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
    name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 部门名称, 示例值："DemoName", 最小长度：`1` 字符
    i18n_name: CreateDepartmentReqI18nName = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 国际化的部门名称
    parent_department_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 父部门的ID,* 创建根部门，该参数值为 “0”, 示例值："D067"
    department_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 本部门的自定义部门ID, 示例值："D096", 最大长度：`64` 字符, 正则校验：`^0|[^od][A-Za-z0-9]*`
    leader_user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 部门主管用户ID, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    order: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 部门的排序，即部门在其同级部门的展示顺序, 示例值："100"
    unit_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 部门单位自定义ID列表，当前只支持一个, 示例值：custom_unit_id
    create_group_chat: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 是否创建部门群，默认不创建, 示例值：false


@attr.s
class CreateDepartmentRespDepartmentStatus(object):
    is_deleted: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否被删除


@attr.s
class CreateDepartmentRespDepartmentI18nName(object):
    zh_cn: str = attr.ib(default="", metadata={"req_type": "json"})  # 部门的中文名
    ja_jp: str = attr.ib(default="", metadata={"req_type": "json"})  # 部门的日文名
    en_us: str = attr.ib(default="", metadata={"req_type": "json"})  # 部门的英文名


@attr.s
class CreateDepartmentRespDepartment(object):
    name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 部门名称,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录
    i18n_name: CreateDepartmentRespDepartmentI18nName = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 国际化的部门名称,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录
    parent_department_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 父部门的ID,* 创建根部门，该参数值为 “0”,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    department_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 本部门的自定义部门ID,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录
    open_department_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 部门的open_id
    leader_user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 部门主管用户ID,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    chat_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 部门群ID,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录
    order: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 部门的排序，即部门在其同级部门的展示顺序,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    unit_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 部门单位自定义ID列表，当前只支持一个,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    member_count: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 部门下用户的个数,**字段权限要求（满足任一）**：, 获取部门组织架构信息, 以应用身份读取通讯录
    status: CreateDepartmentRespDepartmentStatus = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 部门状态,**字段权限要求（满足任一）**：, 获取部门基础信息, 以应用身份读取通讯录


@attr.s
class CreateDepartmentResp(object):
    department: CreateDepartmentRespDepartment = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 部门信息


def _gen_create_department_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateDepartmentResp,
        scope="Contact",
        api="CreateDepartment",
        method="POST",
        url="https://open.feishu.cn/open-apis/contact/v3/departments",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
