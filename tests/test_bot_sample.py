# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.log import logger
from tests.test_conf import app_all_permission
import unittest
import pylark
import pytest


class Test_Bot_Sample_RequestFailed(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.cli = app_all_permission.ins()
        # self.cli.mock().MockGetTenantAccessToken(mockGetTenantAccessTokenFailed)
        # self.cli.mock().MockGetAppAccessToken(mockGetTenantAccessTokenFailed)
        self.module_cli = self.cli.bot

    def test_request_failed_get_bot_info(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.GetBotInfo(pylark.GetBotInfoReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_add_bot_to_chat(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.AddBotToChat(pylark.AddBotToChatReq())
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")
