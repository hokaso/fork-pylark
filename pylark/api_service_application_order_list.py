# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class GetApplicationOrderListReq(object):
    status: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "status"}
    )  # 获取用户购买套餐信息设置的过滤条件, normal为正常状态，refunded为已退款，该字段为空或者all表示所有，未支付的订单无法查到
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query", "key": "page_size"}
    )  # `每页显示的订单数量`
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "page_token"}
    )  # 翻页标识，可以从上次请求的响应中获取，不填或者为空时表示从开头获取
    tenant_key: str = attr.ib(
        default="", metadata={"req_type": "query", "key": "tenant_key"}
    )  # 购买应用的租户唯一标识，为空表示获取应用下所有订单，有值表示获取应用下该租户购买的订单


@attr.s
class GetApplicationOrderListRespOrderList(object):
    order_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "order_id"}
    )  # 订单ID，唯一标识
    price_plan_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "price_plan_id"}
    )  # 价格方案ID，唯一标识
    price_plan_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "price_plan_type"}
    )  # 价格方案类型 "trial" -试用；"permanent"-一次性付费；"per_year"-企业年付费；"per_month"-企业月付费；"per_seat_per_year"-按人按年付费；"per_seat_per_month"-按人按月付费；"permanent_count"-按次付费；
    seats: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "seats"}
    )  # 实际购买人数 仅对price_plan_type为per_seat_per_year和per_seat_per_month 有效
    buy_count: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "buy_count"}
    )  # 购买数量 总是为1
    create_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "create_time"}
    )  # 订单创建时间戳
    pay_time: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "pay_time"}
    )  # 订单支付时间戳
    status: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "status"}
    )  # 订单当前状态，"normal" -正常；"refund"-已退款；
    buy_type: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "buy_type"}
    )  # 购买类型，"buy" - 普通购买;"upgrade"-为升级购买(仅price_plan_type 为per_year，per_month，per_seat_per_year，per_seat_per_month时可升级购买);"renew" - 续费购买；
    src_order_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "src_order_id"}
    )  # 源订单ID，当前订单为升级购买时，即buy_type为upgrade时，此字段记录源订单等ID
    dst_order_id: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "dst_order_id"}
    )  # 升级后的新订单ID，当前订单如果做过升级购买，此字段记录升级购买后生成的新订单ID，当前订单仍然有效
    order_pay_price: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "order_pay_price"}
    )  # 订单实际支付金额, 单位分
    tenant_key: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "tenant_key"}
    )  # 租户唯一标识


@attr.s
class GetApplicationOrderListResp(object):
    total: int = attr.ib(
        default=0, metadata={"req_type": "json", "key": "total"}
    )  # 总订单数
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json", "key": "has_more"}
    )  # 是否还有数据，true还有数据，false没有数据
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json", "key": "page_token"}
    )  # 下一页数据的标识，可作为请求下一页数据的参数，当has_more为false时该字段为空
    order_list: GetApplicationOrderListRespOrderList = attr.ib(
        default=None, metadata={"req_type": "json", "key": "order_list"}
    )  # 订单信息列表


def _gen_get_application_order_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetApplicationOrderListResp,
        scope="Application",
        api="GetApplicationOrderList",
        method="GET",
        url="https://open.feishu.cn/open-apis/pay/v1/order/list",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
