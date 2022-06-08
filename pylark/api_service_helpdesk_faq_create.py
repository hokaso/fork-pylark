# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class CreateHelpdeskFAQReqFAQ(object):
    category_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "category_id"}
    )  # 知识库分类ID, 示例值："6836004780707807251"
    question: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "question"}
    )  # 问题, 示例值："问题"
    answer: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "answer"}
    )  # 答案, 示例值："答案"
    answer_richtext: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "answer_richtext"}
    )  # 富文本答案和答案必须有一个必填。Json Array格式，富文本结构请见[了解更多: 富文本](https://open.feishu.cn/document/ukTMukTMukTM/uITM0YjLyEDN24iMxQjN), 示例值："[{,                        "content": "这只是一个测试，医保问题",,                        "type": "text",                    }]"
    tags: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "tags"}
    )  # 关联词


@attr.s
class CreateHelpdeskFAQReq(object):
    faq: CreateHelpdeskFAQReqFAQ = attr.ib(
        default=None, metadata={"req_type": "json", "key": "faq"}
    )  # 知识库详情


@attr.s
class CreateHelpdeskFAQRespFAQCreateUser(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # 用户ID
    avatar_url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "avatar_url"}
    )  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json", "key": "name"})  # 用户名


@attr.s
class CreateHelpdeskFAQRespFAQUpdateUser(object):
    id: str = attr.ib(default="", metadata={"req_type": "json", "key": "id"})  # 用户ID
    avatar_url: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "avatar_url"}
    )  # 用户头像url
    name: str = attr.ib(default="", metadata={"req_type": "json", "key": "name"})  # 用户名


@attr.s
class CreateHelpdeskFAQRespFAQ(object):
    faq_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "faq_id"}
    )  # 知识库ID
    id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "id"}
    )  # 知识库旧版ID，请使用faq_id
    helpdesk_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "helpdesk_id"}
    )  # 服务台ID
    question: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "question"}
    )  # 问题
    answer: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "answer"}
    )  # 答案
    answer_richtext: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "answer_richtext"}
    )  # 富文本答案
    create_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "create_time"}
    )  # 创建时间
    update_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "update_time"}
    )  # 修改时间
    categories: typing.List[lark_type.HelpdeskCategory] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "categories"}
    )  # 分类
    tags: typing.List[str] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json", "key": "tags"}
    )  # 关联词列表
    expire_time: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "expire_time"}
    )  # 失效时间
    update_user: CreateHelpdeskFAQRespFAQUpdateUser = attr.ib(
        default=None, metadata={"req_type": "json", "key": "update_user"}
    )  # 更新用户
    create_user: CreateHelpdeskFAQRespFAQCreateUser = attr.ib(
        default=None, metadata={"req_type": "json", "key": "create_user"}
    )  # 创建用户


@attr.s
class CreateHelpdeskFAQResp(object):
    faq: CreateHelpdeskFAQRespFAQ = attr.ib(
        default=None, metadata={"req_type": "json", "key": "faq"}
    )  # 知识库详情


def _gen_create_helpdesk_faq_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=CreateHelpdeskFAQResp,
        scope="Helpdesk",
        api="CreateHelpdeskFAQ",
        method="POST",
        url="https://open.feishu.cn/open-apis/helpdesk/v1/faqs",
        body=request,
        method_option=_new_method_option(options),
        need_user_access_token=True,
        need_helpdesk_auth=True,
    )
