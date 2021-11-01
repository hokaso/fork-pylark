# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
from pylark import lark_type, lark_type_sheet, lark_type_approval
import attr
import typing
import io


@attr.s
class StopVCMeetingRecordingReq(object):
    meeting_id: str = attr.ib(
        default="", metadata={"req_type": "path", "key": "meeting_id"}
    )  # 会议ID（视频会议的唯一标识，视频会议开始后才会产生）, 示例值："6911188411932033028"


@attr.s
class StopVCMeetingRecordingResp(object):
    pass


def _gen_stop_vc_meeting_recording_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=StopVCMeetingRecordingResp,
        scope="VC",
        api="StopVCMeetingRecording",
        method="PATCH",
        url="https://open.feishu.cn/open-apis/vc/v1/meetings/:meeting_id/recording/stop",
        body=request,
        method_option=_new_method_option(options),
        need_user_access_token=True,
    )
