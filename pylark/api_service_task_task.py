# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class GetTaskReq(object):
    user_id_type: lark_type.IDType = attr.ib(
        default=None, metadata={"req_type": "query", "key": "user_id_type"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求:  获取用户 user ID
    task_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "task_id"}
    )  # 任务 ID, 示例值："83912691-2e43-47fc-94a4-d512e03984fa"


@attr.s
class GetTaskRespTaskOriginHref(object):
    url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "url"}
    )  # 具体链接地址
    title: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "title"}
    )  # 链接对应的标题


@attr.s
class GetTaskRespTaskOrigin(object):
    platform_i18n_name: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "platform_i18n_name"}
    )  # 任务导入来源的名称，用于在任务中心详情页展示。请提供一个字典，多种语言名称映射。支持的各地区语言名：it_it, th_th, ko_kr, es_es, ja_jp, zh_cn, id_id, zh_hk, pt_br, de_de, fr_fr, zh_tw, ru_ru, en_us, hi_in, vi_vn
    href: GetTaskRespTaskOriginHref = attr.ib(
        default=None, metadata={"req_type": "json", "key": "href"}
    )  # 任务关联的来源平台详情页链接


@attr.s
class GetTaskRespTaskDue(object):
    time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "time"}
    )  # 截止时间的时间戳（单位为秒）
    timezone: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "timezone"}
    )  # 截止时间对应的时区，使用IANA Time Zone Database标准，如Asia/Shanghai
    is_all_day: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "is_all_day"}
    )  # 标记任务是否为全天任务（全天任务的截止时间为当天 UTC 时间的 0 点）


@attr.s
class GetTaskRespTask(object):
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 任务 ID，由飞书任务服务器发号
    summary: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "summary"}
    )  # 任务标题。创建任务时，如果没有标题填充，飞书服务器会将其视为无主题的任务
    description: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "description"}
    )  # 任务备注
    complete_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "complete_time"}
    )  # 任务的完成时间戳（单位为秒），如果完成时间为 0，则表示任务尚未完成
    creator_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "creator_id"}
    )  # 任务的创建者 ID。在创建任务时无需填充该字段
    extra: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "extra"}
    )  # 接入方可以自定义的附属信息二进制格式，采用 base64 编码，解析方式由接入方自己决定
    create_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "create_time"}
    )  # 任务的创建时间戳（单位为秒）
    update_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "update_time"}
    )  # 任务的更新时间戳（单位为秒）
    due: GetTaskRespTaskDue = attr.ib(
        default=None, metadata={"req_type": "json", "key": "due"}
    )  # 任务的截止时间设置
    origin: GetTaskRespTaskOrigin = attr.ib(
        default=None, metadata={"req_type": "json", "key": "origin"}
    )  # 任务关联的第三方平台来源信息
    can_edit: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "can_edit"}
    )  # 此字段用于控制该任务在飞书任务中心是否可编辑，默认为false，若为true则第三方需考虑是否需要接入事件来接收任务在任务中心的变更信息
    custom: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "custom"}
    )  # 此字段用于存储第三方需透传到端上的自定义数据，Json格式。取值举例中custom_complete字段存储「完成」按钮的跳转链接（href）或提示信息（tip），pc、ios、android三端均可自定义，其中tip字段的key为语言类型，value为提示信息，可自行增加或减少语言类型，支持的各地区语言名：it_it, th_th, ko_kr, es_es, ja_jp, zh_cn, id_id, zh_hk, pt_br, de_de, fr_fr, zh_tw, ru_ru, en_us, hi_in, vi_vn。href的优先级高于tip，href和tip同时不为空时只跳转不提示。链接和提示信息可自定义，其余的key需按举例中的结构传递


@attr.s
class GetTaskResp(object):
    task: GetTaskRespTask = attr.ib(
        default=None, metadata={"req_type": "json", "key": "task"}
    )  # 返回任务资源详情


def _gen_get_task_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetTaskResp,
        scope="Task",
        api="GetTask",
        method="GET",
        url="https://open.feishu.cn/open-apis/task/v1/tasks/:task_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
