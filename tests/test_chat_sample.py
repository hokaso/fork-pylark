# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.log import logger
from tests.test_conf import app_all_permission
import unittest
import pylark
import pytest


class Test_Chat_Sample_RequestFailed(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.cli = app_all_permission.ins()
        # self.cli.mock().MockGetTenantAccessToken(mockGetTenantAccessTokenFailed)
        # self.cli.mock().MockGetAppAccessToken(mockGetTenantAccessTokenFailed)
        self.module_cli = self.cli.chat

    def test_request_failed_create_chat(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.CreateChat(pylark.CreateChatReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_get_chat(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.GetChat(pylark.GetChatReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_update_chat(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.UpdateChat(pylark.UpdateChatReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_delete_chat(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.DeleteChat(pylark.DeleteChatReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_get_chat_list_of_self(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.GetChatListOfSelf(
                pylark.GetChatListOfSelfReq()
            )
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_search_chat(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.SearchChat(pylark.SearchChatReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_get_chat_member_list(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.GetChatMemberList(
                pylark.GetChatMemberListReq()
            )
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_is_in_chat(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.IsInChat(pylark.IsInChatReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_add_chat_member(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.AddChatMember(pylark.AddChatMemberReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_delete_chat_member(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.DeleteChatMember(
                pylark.DeleteChatMemberReq()
            )
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_join_chat(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.JoinChat(pylark.JoinChatReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_get_chat_announcement(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.GetChatAnnouncement(
                pylark.GetChatAnnouncementReq()
            )
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_update_chat_announcement(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.UpdateChatAnnouncement(
                pylark.UpdateChatAnnouncementReq()
            )
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")
