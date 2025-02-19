# Code generated by lark_sdk_gen. DO NOT EDIT.

import typing
from pylark.lark_request import Response
from pylark.api_service_auth_tenant_access_token_get import (
    _get_tenant_access_token,
    TokenExpire,
)
from pylark.api_service_auth_app_access_token_get import _get_app_access_token

from pylark.api_service_auth_app_ticket_resend import (
    ResendAppTicketReq,
    ResendAppTicketResp,
    _gen_resend_app_ticket_req,
)
from pylark.api_service_auth_access_token_get import (
    GetAccessTokenReq,
    GetAccessTokenResp,
    _gen_get_access_token_req,
)
from pylark.api_service_auth_access_token_refresh import (
    RefreshAccessTokenReq,
    RefreshAccessTokenResp,
    _gen_refresh_access_token_req,
)
from pylark.api_service_auth_user_info_get import (
    GetUserInfoReq,
    GetUserInfoResp,
    _gen_get_user_info_req,
)


if typing.TYPE_CHECKING:
    from lark import Lark


class LarkAuthService(object):
    cli: "Lark"

    def __init__(self, cli: "Lark"):
        self.cli = cli

    def get_app_ticket(self) -> str:
        # genISVAppTicketKey(r.cli.appSecret)
        return self.cli.store.get()

    def set_app_ticket(self):
        # genISVAppTicketKey(r.cli.appID), appTicket, time.Hour * 2
        self.cli.store.set()

    def resend_app_ticket(
        self, request: ResendAppTicketReq, options: typing.List[str] = None
    ) -> typing.Tuple[ResendAppTicketResp, Response]:
        return self.cli.raw_request(_gen_resend_app_ticket_req(request, options))

    def get_access_token(
        self, request: GetAccessTokenReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetAccessTokenResp, Response]:
        return self.cli.raw_request(_gen_get_access_token_req(request, options))

    def refresh_access_token(
        self, request: RefreshAccessTokenReq, options: typing.List[str] = None
    ) -> typing.Tuple[RefreshAccessTokenResp, Response]:
        return self.cli.raw_request(_gen_refresh_access_token_req(request, options))

    def get_user_info(
        self, request: GetUserInfoReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetUserInfoResp, Response]:
        return self.cli.raw_request(_gen_get_user_info_req(request, options))

    def get_tenant_access_token(self) -> typing.Tuple[TokenExpire, Response]:
        return _get_tenant_access_token(
            cli=self.cli,
            is_isv=False,
            app_id=self.cli.app_id,
            app_secret=self.cli.app_secret,
            tenant_key="",
        )

    def get_app_access_token(
            self,
            use_cache=True
    ) -> typing.Tuple[TokenExpire, Response]:
        return _get_app_access_token(
            cli=self.cli,
            is_isv=False,
            use_cache=use_cache,
        )
