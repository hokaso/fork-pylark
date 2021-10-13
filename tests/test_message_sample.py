# Code generated by lark_sdk_gen. DO NOT EDIT.

import unittest
import pylark
import pytest
from tests.test_conf import app_all_permission, app_no_permission
from tests.test_helper import mock_get_tenant_access_token_failed


def mock(*args, **kwargs):
    raise pylark.PyLarkError(scope="scope", func="func", code=1, msg="mock-failed")


def mock_raw_request(*args, **kwargs):
    raise pylark.PyLarkError(
        scope="scope", func="func", code=1, msg="mock-raw-request-failed"
    )


# mock get token
class TestMessageSampleMockGetTokenFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMessageSampleMockGetTokenFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.cli.auth.get_tenant_access_token = mock_get_tenant_access_token_failed
        self.cli.auth.get_app_access_token = mock_get_tenant_access_token_failed
        self.module_cli = self.cli.message

    def test_mock_get_token_send_ephemeral_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_ephemeral_message(pylark.SendEphemeralMessageReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_send_urgent_app_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_urgent_app_message(pylark.SendUrgentAppMessageReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_send_urgent_sms_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_urgent_sms_message(pylark.SendUrgentSmsMessageReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_send_urgent_phone_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_urgent_phone_message(
                pylark.SendUrgentPhoneMessageReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_send_raw_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_raw_message(pylark.SendRawMessageReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_send_raw_message_old(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_raw_message_old(pylark.SendRawMessageOldReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_reply_raw_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.reply_raw_message(pylark.ReplyRawMessageReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_delete_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_message(pylark.DeleteMessageReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_update_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_message(pylark.UpdateMessageReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_message_read_user_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message_read_user_list(
                pylark.GetMessageReadUserListReq()
            )

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_message_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message_list(pylark.GetMessageListReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_message_file(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message_file(pylark.GetMessageFileReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_get_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message(pylark.GetMessageReq())

        assert "msg=failed" in f"{e}"

    def test_mock_get_token_delete_ephemeral_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_ephemeral_message(pylark.DeleteEphemeralMessageReq())

        assert "msg=failed" in f"{e}"


# mock mock self func
class TestMessageSampleMockSelfFuncFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMessageSampleMockSelfFuncFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.message

    def test_mock_self_func_send_ephemeral_message(self):
        origin_func = self.module_cli.send_ephemeral_message
        self.module_cli.send_ephemeral_message = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_ephemeral_message(pylark.SendEphemeralMessageReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.send_ephemeral_message = origin_func

    def test_mock_self_func_send_urgent_app_message(self):
        origin_func = self.module_cli.send_urgent_app_message
        self.module_cli.send_urgent_app_message = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_urgent_app_message(pylark.SendUrgentAppMessageReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.send_urgent_app_message = origin_func

    def test_mock_self_func_send_urgent_sms_message(self):
        origin_func = self.module_cli.send_urgent_sms_message
        self.module_cli.send_urgent_sms_message = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_urgent_sms_message(pylark.SendUrgentSmsMessageReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.send_urgent_sms_message = origin_func

    def test_mock_self_func_send_urgent_phone_message(self):
        origin_func = self.module_cli.send_urgent_phone_message
        self.module_cli.send_urgent_phone_message = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_urgent_phone_message(
                pylark.SendUrgentPhoneMessageReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.send_urgent_phone_message = origin_func

    def test_mock_self_func_send_raw_message(self):
        origin_func = self.module_cli.send_raw_message
        self.module_cli.send_raw_message = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_raw_message(pylark.SendRawMessageReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.send_raw_message = origin_func

    def test_mock_self_func_send_raw_message_old(self):
        origin_func = self.module_cli.send_raw_message_old
        self.module_cli.send_raw_message_old = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_raw_message_old(pylark.SendRawMessageOldReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.send_raw_message_old = origin_func

    def test_mock_self_func_reply_raw_message(self):
        origin_func = self.module_cli.reply_raw_message
        self.module_cli.reply_raw_message = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.reply_raw_message(pylark.ReplyRawMessageReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.reply_raw_message = origin_func

    def test_mock_self_func_delete_message(self):
        origin_func = self.module_cli.delete_message
        self.module_cli.delete_message = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_message(pylark.DeleteMessageReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.delete_message = origin_func

    def test_mock_self_func_update_message(self):
        origin_func = self.module_cli.update_message
        self.module_cli.update_message = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_message(pylark.UpdateMessageReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.update_message = origin_func

    def test_mock_self_func_get_message_read_user_list(self):
        origin_func = self.module_cli.get_message_read_user_list
        self.module_cli.get_message_read_user_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message_read_user_list(
                pylark.GetMessageReadUserListReq()
            )

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_message_read_user_list = origin_func

    def test_mock_self_func_get_message_list(self):
        origin_func = self.module_cli.get_message_list
        self.module_cli.get_message_list = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message_list(pylark.GetMessageListReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_message_list = origin_func

    def test_mock_self_func_get_message_file(self):
        origin_func = self.module_cli.get_message_file
        self.module_cli.get_message_file = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message_file(pylark.GetMessageFileReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_message_file = origin_func

    def test_mock_self_func_get_message(self):
        origin_func = self.module_cli.get_message
        self.module_cli.get_message = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message(pylark.GetMessageReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.get_message = origin_func

    def test_mock_self_func_delete_ephemeral_message(self):
        origin_func = self.module_cli.delete_ephemeral_message
        self.module_cli.delete_ephemeral_message = mock

        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_ephemeral_message(pylark.DeleteEphemeralMessageReq())

        assert "msg=mock-failed" in f"{e}"
        self.module_cli.delete_ephemeral_message = origin_func


# mock raw request
class TestMessageSampleMockRawRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMessageSampleMockRawRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_all_permission.ins()
        self.module_cli = self.cli.message
        self.cli.raw_request = mock_raw_request

    def test_mock_raw_request_send_ephemeral_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_ephemeral_message(pylark.SendEphemeralMessageReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_send_urgent_app_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_urgent_app_message(
                pylark.SendUrgentAppMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_send_urgent_sms_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_urgent_sms_message(
                pylark.SendUrgentSmsMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_send_urgent_phone_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_urgent_phone_message(
                pylark.SendUrgentPhoneMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_send_raw_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_raw_message(pylark.SendRawMessageReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_send_raw_message_old(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_raw_message_old(pylark.SendRawMessageOldReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_reply_raw_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.reply_raw_message(
                pylark.ReplyRawMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_delete_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_message(
                pylark.DeleteMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_update_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_message(
                pylark.UpdateMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_message_read_user_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message_read_user_list(
                pylark.GetMessageReadUserListReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_message_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message_list(pylark.GetMessageListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_message_file(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message_file(
                pylark.GetMessageFileReq(
                    message_id="x",
                    file_key="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_get_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message(
                pylark.GetMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg

    def test_mock_raw_request_delete_ephemeral_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_ephemeral_message(pylark.DeleteEphemeralMessageReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
        assert "mock-raw-request-failed" in e.value.msg


# real request
class TestMessageSampleRealRequestFailed(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMessageSampleRealRequestFailed, self).__init__(*args, **kwargs)
        self.cli = app_no_permission.ins()
        self.module_cli = self.cli.message

    def test_real_request_send_ephemeral_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_ephemeral_message(pylark.SendEphemeralMessageReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_send_urgent_app_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_urgent_app_message(
                pylark.SendUrgentAppMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_send_urgent_sms_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_urgent_sms_message(
                pylark.SendUrgentSmsMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_send_urgent_phone_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_urgent_phone_message(
                pylark.SendUrgentPhoneMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_send_raw_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_raw_message(pylark.SendRawMessageReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_send_raw_message_old(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.send_raw_message_old(pylark.SendRawMessageOldReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_reply_raw_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.reply_raw_message(
                pylark.ReplyRawMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_delete_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_message(
                pylark.DeleteMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_update_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.update_message(
                pylark.UpdateMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_message_read_user_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message_read_user_list(
                pylark.GetMessageReadUserListReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_message_list(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message_list(pylark.GetMessageListReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_message_file(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message_file(
                pylark.GetMessageFileReq(
                    message_id="x",
                    file_key="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_get_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.get_message(
                pylark.GetMessageReq(
                    message_id="x",
                )
            )

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0

    def test_real_request_delete_ephemeral_message(self):
        with pytest.raises(pylark.PyLarkError) as e:
            self.module_cli.delete_ephemeral_message(pylark.DeleteEphemeralMessageReq())

        assert e.type is pylark.PyLarkError
        assert e.value.code > 0
