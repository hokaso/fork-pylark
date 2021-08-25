# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class BatchCreateBitableRecordReqRecordFieldValue(object):
    pass


@attr.s
class BatchCreateBitableRecordReqRecordField(object):
    key: str = attr.ib(default="", metadata={"req_type": "json"})  # 字段名, 示例值："多行文本"
    value: typing.Any = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 内容, 示例值：文本


@attr.s
class BatchCreateBitableRecordReqRecord(object):
    record_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 记录 id, 示例值："recqwIwhc6"
    fields: BatchCreateBitableRecordReqRecordField = attr.ib(
        factory=lambda: BatchCreateBitableRecordReqRecordField(),
        metadata={"req_type": "json"},
    )  # 记录字段


@attr.s
class BatchCreateBitableRecordReqUserIDType(object):
    pass


@attr.s
class BatchCreateBitableRecordReq(object):
    user_id_type: BatchCreateBitableRecordReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    app_token: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # bitable app token, 示例值："appbcbWCzen6D8dezhoCH2RpMAh"
    table_id: str = attr.ib(
        default="", metadata={"req_type": "path"}
    )  # table id, 示例值："tblsRc9GRRXKqhvW"
    records: typing.List[BatchCreateBitableRecordReqRecord] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 记录


@attr.s
class BatchCreateBitableRecordRespRecordFieldValue(object):
    pass


@attr.s
class BatchCreateBitableRecordRespRecordField(object):
    key: str = attr.ib(default="", metadata={"req_type": "json"})  # 字段名
    value: typing.Any = attr.ib(default=None, metadata={"req_type": "json"})  # 内容


@attr.s
class BatchCreateBitableRecordRespRecord(object):
    record_id: str = attr.ib(default="", metadata={"req_type": "json"})  # 记录 id
    fields: BatchCreateBitableRecordRespRecordField = attr.ib(
        factory=lambda: BatchCreateBitableRecordRespRecordField(),
        metadata={"req_type": "json"},
    )  # 记录字段


@attr.s
class BatchCreateBitableRecordResp(object):
    records: typing.List[BatchCreateBitableRecordRespRecord] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 记录


def _gen_batch_create_bitable_record_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=BatchCreateBitableRecordResp,
        scope="Bitable",
        api="BatchCreateBitableRecord",
        method="POST",
        url="https://open.feishu.cn/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/batch_create",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
        need_user_access_token=True,
    )
