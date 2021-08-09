# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.log import logger
from tests.test_conf import app_all_permission
import unittest
import pylark
import pytest


class Test_EHR_Sample_RequestFailed(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.cli = app_all_permission.ins()
        # self.cli.mock().MockGetTenantAccessToken(mockGetTenantAccessTokenFailed)
        # self.cli.mock().MockGetAppAccessToken(mockGetTenantAccessTokenFailed)
        self.module_cli = self.cli.ehr

    def test_request_failed_get_ehr_employee_list(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.GetEHREmployeeList(
                pylark.GetEHREmployeeListReq()
            )
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")

    def test_request_failed_download_ehr_attachments(self):
        with pytest.raises(ZeroDivisionError) as e:
            res, response = self.module_cli.DownloadEHRAttachments(
                pylark.DownloadEHRAttachmentsReq()
            )
            print("e", e)

            # as.NotNil(err)
            # as.Equal(err.Error(), "failed")
