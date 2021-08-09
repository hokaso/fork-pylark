# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing


@attr.s
class GetDriveCommentReqUserIDType(object):
    pass


@attr.s
class GetDriveCommentReqFileType(object):
    pass


@attr.s
class GetDriveCommentReq(object):
    file_type: GetDriveCommentReqFileType = attr.ib(
        factory=lambda: GetDriveCommentReqFileType(), metadata={"req_type": "query"}
    )  # 文档类型, 示例值："doc", 可选值有: `doc`：文档, `sheet`：表格, `file`：文件
    user_id_type: GetDriveCommentReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 userid
    file_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 文档token, 示例值："doccnHh7U87HOFpii5u5G*****"
    comment_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # 评论ID, 示例值："6916106822734578184"


@attr.s
class GetDriveCommentRespReplyListReplyContentElementPerson(object):
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 回复 at联系人


@attr.s
class GetDriveCommentRespReplyListReplyContentElementDocsLink(object):
    url: str = attr.ib(default="", metadata={"req_type": "json"})  # 回复 at云文档


@attr.s
class GetDriveCommentRespReplyListReplyContentElementTextRun(object):
    text: str = attr.ib(default="", metadata={"req_type": "json"})  # 回复 普通文本


@attr.s
class GetDriveCommentRespReplyListReplyContentElement(object):
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 回复的内容元素, 可选值有: `text_run`：普通文本, `docs_link`：at 云文档链接, `person`：at 联系人
    text_run: GetDriveCommentRespReplyListReplyContentElementTextRun = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文本内容
    docs_link: GetDriveCommentRespReplyListReplyContentElementDocsLink = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文本内容
    person: GetDriveCommentRespReplyListReplyContentElementPerson = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 文本内容


@attr.s
class GetDriveCommentRespReplyListReplyContent(object):
    elements: typing.List[GetDriveCommentRespReplyListReplyContentElement] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 回复的内容


@attr.s
class GetDriveCommentRespReplyListReply(object):
    reply_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 回复ID
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    create_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 创建时间
    update_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 更新时间
    content: GetDriveCommentRespReplyListReplyContent = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 回复内容


@attr.s
class GetDriveCommentRespReplyList(object):
    replies: typing.List[GetDriveCommentRespReplyListReply] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 回复列表


@attr.s
class GetDriveCommentResp(object):
    comment_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 评论ID
    user_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 用户ID
    create_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 创建时间
    update_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 更新时间
    is_solved: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否已解决
    solved_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 解决评论时间
    solver_user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 解决评论者的用户ID
    reply_list: GetDriveCommentRespReplyList = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 评论里的回复列表


def _gen_get_drive_comment_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetDriveCommentResp,
        scope="Drive",
        api="GetDriveComment",
        method="GET",
        url="https://open.feishu.cn/open-apis/drive/v1/files/:file_token/comments/:comment_id",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
