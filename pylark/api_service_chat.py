# Code generated by lark_sdk_gen. DO NOT EDIT.

import typing
from pylark.lark_request import Response

from pylark.api_service_chat_create import (
    CreateChatReq,
    CreateChatResp,
    _gen_create_chat_req,
)
from pylark.api_service_chat_get_old import (
    GetChatOldReq,
    GetChatOldResp,
    _gen_get_chat_old_req,
)
from pylark.api_service_chat_get import GetChatReq, GetChatResp, _gen_get_chat_req
from pylark.api_service_chat_update import (
    UpdateChatReq,
    UpdateChatResp,
    _gen_update_chat_req,
)
from pylark.api_service_chat_delete import (
    DeleteChatReq,
    DeleteChatResp,
    _gen_delete_chat_req,
)
from pylark.api_service_chat_get_list_of_self import (
    GetChatListOfSelfReq,
    GetChatListOfSelfResp,
    _gen_get_chat_list_of_self_req,
)
from pylark.api_service_chat_search import (
    SearchChatReq,
    SearchChatResp,
    _gen_search_chat_req,
)
from pylark.api_service_chat_member_get_list import (
    GetChatMemberListReq,
    GetChatMemberListResp,
    _gen_get_chat_member_list_req,
)
from pylark.api_service_chat_member_in import (
    IsInChatReq,
    IsInChatResp,
    _gen_is_in_chat_req,
)
from pylark.api_service_chat_member_add import (
    AddChatMemberReq,
    AddChatMemberResp,
    _gen_add_chat_member_req,
)
from pylark.api_service_chat_member_delete import (
    DeleteChatMemberReq,
    DeleteChatMemberResp,
    _gen_delete_chat_member_req,
)
from pylark.api_service_chat_join import JoinChatReq, JoinChatResp, _gen_join_chat_req
from pylark.api_service_chat_announcement_get import (
    GetChatAnnouncementReq,
    GetChatAnnouncementResp,
    _gen_get_chat_announcement_req,
)
from pylark.api_service_chat_announcement_update import (
    UpdateChatAnnouncementReq,
    UpdateChatAnnouncementResp,
    _gen_update_chat_announcement_req,
)


if typing.TYPE_CHECKING:
    from lark import Lark


class LarkChatService(object):
    cli: "Lark"

    def __init__(self, cli: "Lark"):
        self.cli = cli

    def create_chat(
        self, request: CreateChatReq, options: typing.List[str] = None
    ) -> typing.Tuple[CreateChatResp, Response]:
        return self.cli.raw_request(_gen_create_chat_req(request, options))

    def get_chat_old(
        self, request: GetChatOldReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetChatOldResp, Response]:
        return self.cli.raw_request(_gen_get_chat_old_req(request, options))

    def get_chat(
        self, request: GetChatReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetChatResp, Response]:
        return self.cli.raw_request(_gen_get_chat_req(request, options))

    def update_chat(
        self, request: UpdateChatReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdateChatResp, Response]:
        return self.cli.raw_request(_gen_update_chat_req(request, options))

    def delete_chat(
        self, request: DeleteChatReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeleteChatResp, Response]:
        return self.cli.raw_request(_gen_delete_chat_req(request, options))

    def get_chat_list_of_self(
        self, request: GetChatListOfSelfReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetChatListOfSelfResp, Response]:
        return self.cli.raw_request(_gen_get_chat_list_of_self_req(request, options))

    def search_chat(
        self, request: SearchChatReq, options: typing.List[str] = None
    ) -> typing.Tuple[SearchChatResp, Response]:
        return self.cli.raw_request(_gen_search_chat_req(request, options))

    def get_chat_member_list(
        self, request: GetChatMemberListReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetChatMemberListResp, Response]:
        return self.cli.raw_request(_gen_get_chat_member_list_req(request, options))

    def is_in_chat(
        self, request: IsInChatReq, options: typing.List[str] = None
    ) -> typing.Tuple[IsInChatResp, Response]:
        return self.cli.raw_request(_gen_is_in_chat_req(request, options))

    def add_chat_member(
        self, request: AddChatMemberReq, options: typing.List[str] = None
    ) -> typing.Tuple[AddChatMemberResp, Response]:
        return self.cli.raw_request(_gen_add_chat_member_req(request, options))

    def delete_chat_member(
        self, request: DeleteChatMemberReq, options: typing.List[str] = None
    ) -> typing.Tuple[DeleteChatMemberResp, Response]:
        return self.cli.raw_request(_gen_delete_chat_member_req(request, options))

    def join_chat(
        self, request: JoinChatReq, options: typing.List[str] = None
    ) -> typing.Tuple[JoinChatResp, Response]:
        return self.cli.raw_request(_gen_join_chat_req(request, options))

    def get_chat_announcement(
        self, request: GetChatAnnouncementReq, options: typing.List[str] = None
    ) -> typing.Tuple[GetChatAnnouncementResp, Response]:
        return self.cli.raw_request(_gen_get_chat_announcement_req(request, options))

    def update_chat_announcement(
        self, request: UpdateChatAnnouncementReq, options: typing.List[str] = None
    ) -> typing.Tuple[UpdateChatAnnouncementResp, Response]:
        return self.cli.raw_request(_gen_update_chat_announcement_req(request, options))
