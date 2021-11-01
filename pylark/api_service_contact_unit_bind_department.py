# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class BindContactUnitDepartmentReq(object):
    unit_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "unit_id"}
    )  # 单位ID, 示例值："BU121"
    department_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "department_id"}
    )  # 单位关联的部门ID, 示例值："od-4e6ac4d14bcd5071a37a39de902c7141"
    department_id_type: lark_type.DepartmentIDType = attr.ib(
        default=None, metadata={"req_type": "json", "key": "department_id_type"}
    )  # 此次调用中使用的部门ID的类型, 示例值："open_department_id", 可选值有: `department_id`：以自定义department_id来标识部门, `open_department_id`：以open_department_id来标识部门, 默认值: `open_department_id`


@attr.s
class BindContactUnitDepartmentResp(object):
    pass


def _gen_bind_contact_unit_department_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=BindContactUnitDepartmentResp,
        scope="Contact",
        api="BindContactUnitDepartment",
        method="POST",
        url="https://open.feishu.cn/open-apis/contact/v3/unit/bind_department",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
