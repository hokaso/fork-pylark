# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class UpdateUserReqCustomAttrValueGenericUser(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的user_id, 示例值："9b2fabg5"
    type: int = attr.ib(default=0, metadata={"req_type": "json"})  # 用户类型    1：用户, 示例值：1


@attr.s
class UpdateUserReqCustomAttrValue(object):
    text: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段类型为 TEXT 时该参数定义字段值，字段类型为 HREF 时该参数定义网页标题, 示例值："DemoText"
    url: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段类型为 HREF 时，该参数定义默认 URL, 示例值："http://www.feishu.cn"
    pc_url: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段类型为 HREF 时，该参数定义PC端 URL, 示例值："http://www.feishu.cn"
    option_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段类型为 ENUMERATION 或 PICTURE_ENUM 时，该参数定义选项值, 示例值："edcvfrtg"
    generic_user: UpdateUserReqCustomAttrValueGenericUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 字段类型为 GENERIC_USER 时，该参数定义引用人员


@attr.s
class UpdateUserReqCustomAttr(object):
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 自定义字段类型   , `TEXT`, `HREF`, `ENUMERATION`, `PICTURE_ENUM`, `GENERIC_USER`, 示例值："TEXT"
    id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 自定义字段ID, 示例值："DemoId"
    value: UpdateUserReqCustomAttrValue = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 自定义字段取值


@attr.s
class UpdateUserReqOrder(object):
    department_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 排序信息对应的部门ID, ID值与查询参数中的department_id_type 对应。,不同 ID 的说明参见 [部门ID说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview#23857fe0), 示例值："od-4e6ac4d14bcd5071a37a39de902c7141"
    user_order: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 用户在其直属部门内的排序，数值越大，排序越靠前, 示例值：100
    department_order: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 用户所属的多个部门间的排序，数值越大，排序越靠前, 示例值：100


@attr.s
class UpdateUserReqDepartmentIDType(object):
    pass


@attr.s
class UpdateUserReqUserIDType(object):
    pass


@attr.s
class UpdateUserReq(object):
    user_id_type: UpdateUserReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`,, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    department_id_type: UpdateUserReqDepartmentIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 此次调用中使用的部门ID的类型, 示例值："open_department_id", 可选值有: `department_id`：以自定义department_id来标识部门, `open_department_id`：以open_department_id来标识部门, 默认值: `open_department_id`
    user_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 用户ID，需要与查询参数中的user_id_type类型保持一致。, 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户名, 示例值："张三", 最小长度：`1` 字符,**字段权限要求（满足任一）**：, 获取用户基本信息, 以应用身份访问通讯录（历史版本）
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 英文名, 示例值："San Zhang",**字段权限要求（满足任一）**：, 获取用户基本信息, 以应用身份访问通讯录（历史版本）
    email: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 邮箱, 示例值："zhangsan@gmail.com", 字段权限要求:  获取用户邮箱信息
    mobile: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 手机号, 示例值："13011111111", 字段权限要求:  获取用户手机号
    mobile_visible: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 手机号码可见性，true 为可见，false 为不可见，目前默认为 true。不可见时，组织员工将无法查看该员工的手机号码, 示例值：false
    gender: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 性别, 示例值：1, 可选值有: `0`：保密, `1`：男, `2`：女,**字段权限要求（满足任一）**：, 获取用户性别, 以应用身份访问通讯录（历史版本）
    avatar_key: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 头像的文件Key，可通过“消息与群组/消息/图片信息”中的“上传图片”接口上传并获取头像文件 Key, 示例值："2500c7a9-5fff-4d9a-a2de-3d59614ae28g"
    department_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 用户所属部门的ID列表，一个用户可属于多个部门。,ID值与查询参数中的department_id_type 对应。,不同 ID 的说明参见 [部门ID说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview#23857fe0), 示例值：od-4e6ac4d14bcd5071a37a39de902c7141
    leader_user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的直接主管的用户ID，ID值与查询参数中的user_id_type 对应。,不同 ID 的说明参见 [用户相关的 ID 概念](https://open.feishu.cn/document/home/user-identity-introduction/introduction), 示例值："ou_7dab8a3d3cdcc9da365777c7ad535d62"
    city: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 城市, 示例值："杭州",**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    country: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 国家或地区, 示例值："中国",**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    work_station: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 工位, 示例值："北楼-H34",**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    join_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 入职时间, 示例值：2147483647,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    employee_no: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 工号, 示例值："1",**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    employee_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 员工类型，可选值有：, 1：正式员工, 2：实习生, 3：外包, 4：劳务, 5：顾问   ,同时可读取到自定义员工类型的 int 值，可通过下方接口获取到该租户的自定义员工类型的名称   ,[获取人员类型](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list), 示例值：1
    orders: typing.List[UpdateUserReqOrder] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 用户排序信息
    custom_attrs: typing.List[UpdateUserReqCustomAttr] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 自定义字段，请确保你的组织管理员已在管理后台/组织架构/成员字段管理/自定义字段管理/全局设置中开启了“允许开放平台 API 调用“，否则该字段不会生效/返回。,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    enterprise_email: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 企业邮箱，请先确保已在管理后台启用飞书邮箱服务, 示例值："demo@mail.com",**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    job_title: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 职务, 示例值："xxxxx",**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    is_frozen: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 是否暂停用户, 示例值：false


@attr.s
class UpdateUserRespUserNotificationOption(object):
    channels: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 通道列表，枚举值：,sms（短信邀请），email（邮件邀请）
    language: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 语言类型, 可选值有: `zh-CN`：中文, `en-US`：英文, `ja-JP`：日文


@attr.s
class UpdateUserRespUserCustomAttrValueGenericUser(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户的user_id
    type: int = attr.ib(default=0, metadata={"req_type": "json"})  # 用户类型    1：用户


@attr.s
class UpdateUserRespUserCustomAttrValue(object):
    text: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段类型为 TEXT 时该参数定义字段值，字段类型为 HREF 时该参数定义网页标题
    url: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段类型为 HREF 时，该参数定义默认 URL
    pc_url: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段类型为 HREF 时，该参数定义PC端 URL
    option_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 字段类型为 ENUMERATION 或 PICTURE_ENUM 时，该参数定义选项值
    option_value: str = attr.ib(default="", metadata={"req_type": "json"})  # 选项值
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    picture_url: str = attr.ib(default="", metadata={"req_type": "json"})  # 图片链接
    generic_user: UpdateUserRespUserCustomAttrValueGenericUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 字段类型为 GENERIC_USER 时，该参数定义引用人员


@attr.s
class UpdateUserRespUserCustomAttr(object):
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 自定义字段类型   , `TEXT`, `HREF`, `ENUMERATION`, `PICTURE_ENUM`, `GENERIC_USER`
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 自定义字段ID
    value: UpdateUserRespUserCustomAttrValue = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 自定义字段取值


@attr.s
class UpdateUserRespUserOrder(object):
    department_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 排序信息对应的部门ID, ID值与查询参数中的department_id_type 对应。,不同 ID 的说明参见 [部门ID说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview#23857fe0)
    user_order: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 用户在其直属部门内的排序，数值越大，排序越靠前
    department_order: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 用户所属的多个部门间的排序，数值越大，排序越靠前


@attr.s
class UpdateUserRespUserStatus(object):
    is_frozen: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否暂停
    is_resigned: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否离职
    is_activated: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否激活


@attr.s
class UpdateUserRespUserAvatar(object):
    avatar_72: str = attr.ib(default="", metadata={"req_type": "json"})  # 72*72像素头像链接
    avatar_240: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 240*240像素头像链接
    avatar_640: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 640*640像素头像链接
    avatar_origin: str = attr.ib(default="", metadata={"req_type": "json"})  # 原始头像链接


@attr.s
class UpdateUserRespUser(object):
    union_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的union_id，不同ID的说明参见 [用户相关的 ID 概念](https://open.feishu.cn/document/home/user-identity-introduction/introduction)
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 租户内用户的唯一标识，ID值与查询参数中的user_id_type 对应。,不同 ID 的说明参见 [用户相关的 ID 概念](https://open.feishu.cn/document/home/user-identity-introduction/introduction), 字段权限要求:  获取用户 user ID
    open_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的open_id，不同ID的说明参见 [用户相关的 ID 概念](https://open.feishu.cn/document/home/user-identity-introduction/introduction)
    name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户名, 最小长度：`1` 字符,**字段权限要求（满足任一）**：, 获取用户基本信息, 以应用身份访问通讯录（历史版本）
    en_name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 英文名,**字段权限要求（满足任一）**：, 获取用户基本信息, 以应用身份访问通讯录（历史版本）
    email: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 邮箱, 字段权限要求:  获取用户邮箱信息
    mobile: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 手机号, 字段权限要求:  获取用户手机号
    mobile_visible: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 手机号码可见性，true 为可见，false 为不可见，目前默认为 true。不可见时，组织员工将无法查看该员工的手机号码
    gender: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 性别, 可选值有: `0`：保密, `1`：男, `2`：女,**字段权限要求（满足任一）**：, 获取用户性别, 以应用身份访问通讯录（历史版本）
    avatar_key: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 头像的文件Key，可通过“消息与群组/消息/图片信息”中的“上传图片”接口上传并获取头像文件 Key
    avatar: UpdateUserRespUserAvatar = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 用户头像信息,**字段权限要求（满足任一）**：, 获取用户基本信息, 以应用身份访问通讯录（历史版本）
    status: UpdateUserRespUserStatus = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 用户状态,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    department_ids: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 用户所属部门的ID列表，一个用户可属于多个部门。,ID值与查询参数中的department_id_type 对应。,不同 ID 的说明参见 [部门ID说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/field-overview#23857fe0),**字段权限要求（满足任一）**：, 获取用户组织架构信息, 以应用身份访问通讯录（历史版本）
    leader_user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 用户的直接主管的用户ID，ID值与查询参数中的user_id_type 对应。,不同 ID 的说明参见 [用户相关的 ID 概念](https://open.feishu.cn/document/home/user-identity-introduction/introduction),**字段权限要求（满足任一）**：, 获取用户组织架构信息, 以应用身份访问通讯录（历史版本）
    city: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 城市,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    country: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 国家或地区,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    work_station: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 工位,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    join_time: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 入职时间,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    is_tenant_manager: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否是租户管理员,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    employee_no: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 工号,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    employee_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 员工类型，可选值有：, 1：正式员工, 2：实习生, 3：外包, 4：劳务, 5：顾问   ,同时可读取到自定义员工类型的 int 值，可通过下方接口获取到该租户的自定义员工类型的名称   ,[获取人员类型](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list),**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    orders: typing.List[UpdateUserRespUserOrder] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 用户排序信息,**字段权限要求（满足任一）**：, 获取用户组织架构信息, 以应用身份访问通讯录（历史版本）
    custom_attrs: typing.List[UpdateUserRespUserCustomAttr] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 自定义字段，请确保你的组织管理员已在管理后台/组织架构/成员字段管理/自定义字段管理/全局设置中开启了“允许开放平台 API 调用“，否则该字段不会生效/返回。,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    enterprise_email: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 企业邮箱，请先确保已在管理后台启用飞书邮箱服务,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    job_title: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 职务,**字段权限要求（满足任一）**：, 获取用户雇佣信息, 以应用身份访问通讯录（历史版本）
    need_send_notification: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否发送提示消息
    notification_option: UpdateUserRespUserNotificationOption = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 创建用户的邀请方式
    is_frozen: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否暂停用户


@attr.s
class UpdateUserResp(object):
    user: UpdateUserRespUser = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 用户信息


def _gen_update_user_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=UpdateUserResp,
        scope="Contact",
        api="UpdateUser",
        method="PUT",
        url="https://open.feishu.cn/open-apis/contact/v3/users/:user_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
