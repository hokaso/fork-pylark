# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class CreateTaskReqOriginHref(object):
    url: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 具体链接地址, 示例值："https://support.feishu.com/internal/foo-bar", 长度范围：`0` ～ `1024` 字符
    title: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 链接对应的标题, 示例值："反馈一个问题，需要协助排查", 长度范围：`0` ～ `512` 字符


@attr.s
class CreateTaskReqOrigin(object):
    platform_i18n_name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 任务导入来源的名称，用于在任务中心详情页展示。请提供一个字典，多种语言名称映射。支持的各地区语言名：it_it, th_th, ko_kr, es_es, ja_jp, zh_cn, id_id, zh_hk, pt_br, de_de, fr_fr, zh_tw, ru_ru, en_us, hi_in, vi_vn, 示例值：""{\"zh_cn\": \"IT 工作台\", \"en_us\": \"IT Workspace\"}"", 长度范围：`0` ～ `1024` 字符
    href: CreateTaskReqOriginHref = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 任务关联的来源平台详情页链接


@attr.s
class CreateTaskReqDue(object):
    time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 截止时间的时间戳（单位为秒）, 示例值："1623124318"
    timezone: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 截止时间对应的时区，完整的时区名称列表可参考：https://docs.aws.amazon.com/zh_cn/redshift/latest/dg/time-zone-names.html, 示例值："Asia/Shanghai", 默认值: `Asia/Shanghai`
    is_all_day: bool = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 标记任务是否为全天任务（全天任务的截止时间为当天 UTC 时间的 0 点）, 示例值：false, 默认值: `false`


@attr.s
class CreateTaskReqUserIDType(object):
    pass


@attr.s
class CreateTaskReq(object):
    user_id_type: CreateTaskReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`,, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    summary: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 任务标题。创建任务时，如果没有标题填充，飞书服务器会将其视为无主题的任务, 示例值："每天喝八杯水，保持身心愉悦", 长度范围：`1` ～ `256` 字符
    description: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 任务备注, 示例值："多吃水果，多运动，健康生活，快乐工作。", 长度范围：`0` ～ `65536` 字符
    extra: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 接入方可以自定义的附属信息二进制格式，采用 base64 编码，解析方式由接入方自己决定, 示例值："dGVzdA==", 长度范围：`0` ～ `65536` 字符
    due: CreateTaskReqDue = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 任务的截止时间设置
    origin: CreateTaskReqOrigin = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 任务关联的第三方平台来源信息


@attr.s
class CreateTaskRespTaskOriginHref(object):
    url: str = attr.ib(default="", metadata={"req_type": "json"})  # 具体链接地址
    title: str = attr.ib(default="", metadata={"req_type": "json"})  # 链接对应的标题


@attr.s
class CreateTaskRespTaskOrigin(object):
    platform_i18n_name: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 任务导入来源的名称，用于在任务中心详情页展示。请提供一个字典，多种语言名称映射。支持的各地区语言名：it_it, th_th, ko_kr, es_es, ja_jp, zh_cn, id_id, zh_hk, pt_br, de_de, fr_fr, zh_tw, ru_ru, en_us, hi_in, vi_vn
    href: CreateTaskRespTaskOriginHref = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 任务关联的来源平台详情页链接


@attr.s
class CreateTaskRespTaskDue(object):
    time: str = attr.ib(default="", metadata={"req_type": "json"})  # 截止时间的时间戳（单位为秒）
    timezone: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 截止时间对应的时区，完整的时区名称列表可参考：https://docs.aws.amazon.com/zh_cn/redshift/latest/dg/time-zone-names.html
    is_all_day: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 标记任务是否为全天任务（全天任务的截止时间为当天 UTC 时间的 0 点）


@attr.s
class CreateTaskRespTask(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 任务 ID，由飞书任务服务器发号
    summary: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 任务标题。创建任务时，如果没有标题填充，飞书服务器会将其视为无主题的任务
    description: str = attr.ib(default="", metadata={"req_type": "json"})  # 任务备注
    complete_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 任务的完成时间戳（单位为秒），如果完成时间为 0，则表示任务尚未完成
    creator_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 任务的创建者 ID。在创建任务时无需填充该字段
    extra: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 接入方可以自定义的附属信息二进制格式，采用 base64 编码，解析方式由接入方自己决定
    create_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 任务的创建时间戳（单位为秒）
    update_time: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 任务的更新时间戳（单位为秒）
    due: CreateTaskRespTaskDue = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 任务的截止时间设置
    origin: CreateTaskRespTaskOrigin = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 任务关联的第三方平台来源信息


@attr.s
class CreateTaskResp(object):
    task: CreateTaskRespTask = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 返回创建好的任务


def _gen_create_task_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateTaskResp,
        scope="Task",
        api="CreateTask",
        method="POST",
        url="https://open.feishu.cn/open-apis/task/v1/tasks",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
