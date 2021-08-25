# Code generated by lark_sdk_gen. DO NOT EDIT.

from pylark.lark_request import RawRequestReq, _new_method_option
import attr
import typing
import io


@attr.s
class GetEHREmployeeListReqUserIDType(object):
    pass


@attr.s
class GetEHREmployeeListReq(object):
    view: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 返回数据类型, 示例值："basic", 可选值有: `basic`：概览，只返回 id、name 等基本信息, `full`：明细，返回系统标准字段和自定义字段集合
    status: typing.List[int] = attr.ib(
        factory=lambda: [], metadata={"req_type": "query"}
    )  # 员工状态，不传代表查询所有员工状态,实际在职 = 2&4, 示例值：1
    type: typing.List[int] = attr.ib(
        factory=lambda: [], metadata={"req_type": "query"}
    )  # 雇员类型，不传代表查询所有雇员类型, 示例值：1
    start_time: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 查询开始时间（创建时间 &gt;= 此时间）, 示例值：1608690517811
    end_time: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 查询结束时间（创建时间 &lt;= 此时间）, 示例值：1608690517811
    user_id_type: GetEHREmployeeListReqUserIDType = attr.ib(
        default=None, metadata={"req_type": "query"}
    )  # 用户 ID 类型, 示例值："open_id", 可选值有: `open_id`：用户的 open id, `union_id`：用户的 union id, `user_id`：用户的 user id, 默认值: `open_id`,, 当值为 `user_id`, 字段权限要求: 获取用户 user ID
    user_ids: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # user_id、open_id 或 union_id，默认为 open_id。,如果传入的值不是 open_id，需要一并传入 user_id_type 参数。, 示例值："ou_8ebd4f35d7101ffdeb4771d7c8ec517e"
    page_token: str = attr.ib(
        default="", metadata={"req_type": "query"}
    )  # 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果, 示例值："10"
    page_size: int = attr.ib(
        default=0, metadata={"req_type": "query"}
    )  # 分页大小, 示例值：10, 最大值：`100`


@attr.s
class GetEHREmployeeListRespItemCustomField(object):
    key: str = attr.ib(default="", metadata={"req_type": "json"})  # 自定义字段key
    label: str = attr.ib(default="", metadata={"req_type": "json"})  # 自定义字段名称
    type: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 自定义字段类型, 可选值有: `text`：文本类型, `date`：日期类型，如 2020-01-01, `option`：枚举类型, `file`：附件类型
    value: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 根据 type 不同，结构不同，不同 type 对应的数据结构在 type 的枚举值中有描述


@attr.s
class GetEHREmployeeListRespItemSystemFieldsOffboardingFile(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 下载文件所需要的 Token
    mime_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 文件类型
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    size: int = attr.ib(default=0, metadata={"req_type": "json"})  # 大小


@attr.s
class GetEHREmployeeListRespItemSystemFieldsCertOfMerit(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 下载文件所需要的 Token
    mime_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 文件类型
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    size: int = attr.ib(default=0, metadata={"req_type": "json"})  # 大小


@attr.s
class GetEHREmployeeListRespItemSystemFieldsGraduationCert(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 下载文件所需要的 Token
    mime_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 文件类型
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    size: int = attr.ib(default=0, metadata={"req_type": "json"})  # 大小


@attr.s
class GetEHREmployeeListRespItemSystemFieldsDiplomaPhoto(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 下载文件所需要的 Token
    mime_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 文件类型
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    size: int = attr.ib(default=0, metadata={"req_type": "json"})  # 大小


@attr.s
class GetEHREmployeeListRespItemSystemFieldsIDPhoto(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 下载文件所需要的 Token
    mime_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 文件类型
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    size: int = attr.ib(default=0, metadata={"req_type": "json"})  # 大小


@attr.s
class GetEHREmployeeListRespItemSystemFieldsIDPhotoEmSide(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 下载文件所需要的 Token
    mime_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 文件类型
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    size: int = attr.ib(default=0, metadata={"req_type": "json"})  # 大小


@attr.s
class GetEHREmployeeListRespItemSystemFieldsIDPhotoPoSide(object):
    id: str = attr.ib(default="", metadata={"req_type": "json"})  # 下载文件所需要的 Token
    mime_type: str = attr.ib(default="", metadata={"req_type": "json"})  # 文件类型
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称
    size: int = attr.ib(default=0, metadata={"req_type": "json"})  # 大小


@attr.s
class GetEHREmployeeListRespItemSystemFieldsWorkExp(object):
    company: str = attr.ib(default="", metadata={"req_type": "json"})  # 公司
    department: str = attr.ib(default="", metadata={"req_type": "json"})  # 部门
    job: str = attr.ib(default="", metadata={"req_type": "json"})  # 职位
    start: str = attr.ib(default="", metadata={"req_type": "json"})  # 开始日期
    end: str = attr.ib(default="", metadata={"req_type": "json"})  # 截止日期
    description: str = attr.ib(default="", metadata={"req_type": "json"})  # 工作描述


@attr.s
class GetEHREmployeeListRespItemSystemFieldsFormerWorkExp(object):
    company: str = attr.ib(default="", metadata={"req_type": "json"})  # 公司
    department: str = attr.ib(default="", metadata={"req_type": "json"})  # 部门
    job: str = attr.ib(default="", metadata={"req_type": "json"})  # 职位
    start: str = attr.ib(default="", metadata={"req_type": "json"})  # 开始日期
    end: str = attr.ib(default="", metadata={"req_type": "json"})  # 截止日期
    description: str = attr.ib(default="", metadata={"req_type": "json"})  # 工作描述


@attr.s
class GetEHREmployeeListRespItemSystemFieldsEducation(object):
    level: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 学历, 可选值有: `1`：小学, `2`：初中, `3`：高中, `4`：职业高级中学, `5`：中等专业学校, `6`：大专, `7`：本科, `8`：硕士, `9`：博士
    school: str = attr.ib(default="", metadata={"req_type": "json"})  # 毕业学校
    major: str = attr.ib(default="", metadata={"req_type": "json"})  # 专业
    degree: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 学位, 可选值有: `1`：学士, `2`：硕士, `3`：博士
    start: str = attr.ib(default="", metadata={"req_type": "json"})  # 开始日期
    end: str = attr.ib(default="", metadata={"req_type": "json"})  # 结束日期


@attr.s
class GetEHREmployeeListRespItemSystemFieldsHighestLevelOfEdu(object):
    level: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 学历, 可选值有: `1`：小学, `2`：初中, `3`：高中, `4`：职业高级中学, `5`：中等专业学校, `6`：大专, `7`：本科, `8`：硕士, `9`：博士
    school: str = attr.ib(default="", metadata={"req_type": "json"})  # 毕业学校
    major: str = attr.ib(default="", metadata={"req_type": "json"})  # 专业
    degree: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 学位, 可选值有: `1`：学士, `2`：硕士, `3`：博士
    start: str = attr.ib(default="", metadata={"req_type": "json"})  # 开始日期
    end: str = attr.ib(default="", metadata={"req_type": "json"})  # 结束日期


@attr.s
class GetEHREmployeeListRespItemSystemFieldsEmergencyContact(object):
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 紧急联系人姓名
    relationship: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 与紧急联系人的关系, 可选值有: `1`：父母, `2`：配偶, `3`：子女, `4`：兄弟姐妹, `5`：朋友, `6`：其他
    mobile: str = attr.ib(default="", metadata={"req_type": "json"})  # 手机号


@attr.s
class GetEHREmployeeListRespItemSystemFieldsPrimaryEmergencyContact(object):
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 紧急联系人姓名
    relationship: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 与紧急联系人的关系, 可选值有: `1`：父母, `2`：配偶, `3`：子女, `4`：兄弟姐妹, `5`：朋友, `6`：其他
    mobile: str = attr.ib(default="", metadata={"req_type": "json"})  # 手机号


@attr.s
class GetEHREmployeeListRespItemSystemFieldsContractCompany(object):
    id: int = attr.ib(default=0, metadata={"req_type": "json"})  # 公司 ID
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 公司名称


@attr.s
class GetEHREmployeeListRespItemSystemFieldsProbationMonths(object):
    pass


@attr.s
class GetEHREmployeeListRespItemSystemFieldsIDType(object):
    pass


@attr.s
class GetEHREmployeeListRespItemSystemFieldsNativeRegion(object):
    iso_code: str = attr.ib(default="", metadata={"req_type": "json"})  # ISO 编码
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 名称


@attr.s
class GetEHREmployeeListRespItemSystemFieldsWorkLocation(object):
    id: int = attr.ib(default=0, metadata={"req_type": "json"})  # 工作地点 ID
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 工作地点名称


@attr.s
class GetEHREmployeeListRespItemSystemFieldsJobLevel(object):
    id: int = attr.ib(default=0, metadata={"req_type": "json"})  # 职级 ID
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 职级名称


@attr.s
class GetEHREmployeeListRespItemSystemFieldsJob(object):
    id: int = attr.ib(default=0, metadata={"req_type": "json"})  # 职位 ID
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 职位名称


@attr.s
class GetEHREmployeeListRespItemSystemFieldsManager(object):
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 上级的用户 ID（user_id）
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 中文名
    en_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文名


@attr.s
class GetEHREmployeeListRespItemSystemFields(object):
    name: str = attr.ib(default="", metadata={"req_type": "json"})  # 中文姓名
    en_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 英文姓名
    email: str = attr.ib(default="", metadata={"req_type": "json"})  # 邮箱
    mobile: str = attr.ib(default="", metadata={"req_type": "json"})  # 手机号码
    department_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 部门的飞书 open_department_id
    manager: GetEHREmployeeListRespItemSystemFieldsManager = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 上级
    job: GetEHREmployeeListRespItemSystemFieldsJob = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 职位
    job_level: GetEHREmployeeListRespItemSystemFieldsJobLevel = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 职级
    work_location: GetEHREmployeeListRespItemSystemFieldsWorkLocation = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 工作地点
    gender: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 性别, 可选值有: `1`：男, `2`：女
    birthday: str = attr.ib(default="", metadata={"req_type": "json"})  # 出生日期
    native_region: GetEHREmployeeListRespItemSystemFieldsNativeRegion = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 籍贯
    ethnicity: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 民族, 可选值有: `1`：汉族, `2`：蒙古族, `3`：回族, `4`：藏族, `5`：维吾尔族, `6`：苗族, `7`：彝族, `8`：壮族, `9`：布依族, `10`：朝鲜族, `11`：满族, `12`：侗族, `13`：瑶族, `14`：白族, `15`：土家族, `16`：哈尼族, `17`：哈萨克族, `18`：傣族, `19`：黎族, `20`：傈僳族, `21`：佤族, `22`：畲族, `23`：高山族, `24`：拉祜族, `25`：水族, `26`：东乡族, `27`：纳西族, `28`：景颇族, `29`：阿昌族, `30`：柯尔克孜族, `31`：土族, `32`：达斡尔族, `33`：仫佬族, `34`：羌族, `35`：布朗族, `36`：撒拉族, `37`：毛南族, `38`：仡佬族, `39`：锡伯族, `40`：普米族, `41`：塔吉克族, `42`：怒族, `43`：乌孜别克族, `44`：俄罗斯族, `45`：鄂温克族, `46`：德昂族, `47`：保安族, `48`：裕固族, `49`：京族, `50`：塔塔尔族, `51`：独龙族, `52`：鄂伦春族, `53`：赫哲族, `54`：门巴族, `55`：珞巴族, `56`：基诺族, `57`：其他
    marital_status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 婚姻状况, 可选值有: `1`：未婚, `2`：已婚, `3`：离异, `4`：其他
    political_status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 政治面貌, 可选值有: `1`：中共党员, `2`：中国农工民主党, `3`：中国国民党革命委员会, `4`：中国民主促进会会员, `5`：中国民主同盟成员, `6`：中国民主建国会, `7`：中国致公党党员, `8`：九三学社社员, `9`：共青团员, `10`：其它党派成员, `11`：民主人士, `12`：群众
    entered_workforce_date: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 参加工作日期
    id_type: GetEHREmployeeListRespItemSystemFieldsIDType = attr.ib(
        factory=lambda: GetEHREmployeeListRespItemSystemFieldsIDType(),
        metadata={"req_type": "json"},
    )  # 证件类型, 可选值有: `1`：居民身份证, `2`：港澳居民来往内地通行证, `3`：台湾居民来往大陆通行证, `4`：护照, `5`：其他
    id_number: str = attr.ib(default="", metadata={"req_type": "json"})  # 证件号
    hukou_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 户口类型, 可选值有: `1`：本市城镇, `2`：外埠城镇, `3`：本市农村, `4`：外埠农村
    hukou_location: str = attr.ib(default="", metadata={"req_type": "json"})  # 户口所在地
    bank_account_number: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 银行卡号
    bank_name: str = attr.ib(default="", metadata={"req_type": "json"})  # 开户行
    social_security_account: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 社保账号
    provident_fund_account: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 公积金账号
    employee_no: str = attr.ib(default="", metadata={"req_type": "json"})  # 工号
    employee_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 雇员类型, 可选值有: `1`：全职, `2`：实习, `3`：顾问, `4`：外包, `5`：劳务
    status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 员工状态, 可选值有: `1`：待入职, `2`：在职, `3`：已取消入职, `4`：待离职, `5`：已离职
    hire_date: str = attr.ib(default="", metadata={"req_type": "json"})  # 入职日期
    probation_months: float = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 试用期（月）
    conversion_date: str = attr.ib(default="", metadata={"req_type": "json"})  # 转正日期
    application: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 转正申请, 可选值有: `1`：未申请, `2`：审批中, `3`：被驳回, `4`：已通过
    application_status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 转正状态, 可选值有: `1`：无需转正, `2`：待转正, `3`：已转正
    last_day: str = attr.ib(default="", metadata={"req_type": "json"})  # 离职日期
    departure_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 离职类型, 可选值有: `1`：主动, `2`：被动
    departure_reason: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 离职原因, 可选值有: `1`：身体、家庭原因, `2`：职业发展, `3`：薪资福利不满意, `4`：工作压力大, `5`：合同到期不续签, `6`：其他, `7`：无法胜任工作, `8`：组织业务调整和岗位优化, `9`：违反公司条例, `10`：试用期未通过, `11`：其他
    departure_notes: str = attr.ib(default="", metadata={"req_type": "json"})  # 离职备注
    contract_company: GetEHREmployeeListRespItemSystemFieldsContractCompany = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 合同公司
    contract_type: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 合同类型, 可选值有: `1`：固定期限劳动合同, `2`：无固定期限劳动合同, `3`：实习协议, `4`：外包协议, `5`：劳务派遣合同, `6`：返聘协议, `7`：其他
    contract_start_date: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 合同开始日期
    contract_expiration_date: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 合同到期日期
    contract_sign_times: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 劳动合同签订次数
    personal_email: str = attr.ib(default="", metadata={"req_type": "json"})  # 个人邮箱
    family_address: str = attr.ib(default="", metadata={"req_type": "json"})  # 家庭地址
    primary_emergency_contact: GetEHREmployeeListRespItemSystemFieldsPrimaryEmergencyContact = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 主要紧急联系人
    emergency_contact: typing.List[
        GetEHREmployeeListRespItemSystemFieldsEmergencyContact
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 紧急联系人
    highest_level_of_edu: GetEHREmployeeListRespItemSystemFieldsHighestLevelOfEdu = (
        attr.ib(default=None, metadata={"req_type": "json"})
    )  # 最高学历
    education: typing.List[GetEHREmployeeListRespItemSystemFieldsEducation] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 教育经历
    former_work_exp: GetEHREmployeeListRespItemSystemFieldsFormerWorkExp = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 前工作经历
    work_exp: typing.List[GetEHREmployeeListRespItemSystemFieldsWorkExp] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 工作经历
    id_photo_po_side: typing.List[
        GetEHREmployeeListRespItemSystemFieldsIDPhotoPoSide
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 身份证照片（人像面）
    id_photo_em_side: typing.List[
        GetEHREmployeeListRespItemSystemFieldsIDPhotoEmSide
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 身份证照片（国徽面）
    id_photo: typing.List[GetEHREmployeeListRespItemSystemFieldsIDPhoto] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 证件照
    diploma_photo: typing.List[
        GetEHREmployeeListRespItemSystemFieldsDiplomaPhoto
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 学位证书
    graduation_cert: typing.List[
        GetEHREmployeeListRespItemSystemFieldsGraduationCert
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 毕业证书
    cert_of_merit: typing.List[
        GetEHREmployeeListRespItemSystemFieldsCertOfMerit
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 奖励证明
    offboarding_file: typing.List[
        GetEHREmployeeListRespItemSystemFieldsOffboardingFile
    ] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 离职证明
    cancel_onboarding_reason: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 取消入职原因, 可选值有: `1`：个人原因, `2`：原单位留任, `3`：接受其他 Offer, `4`：其他
    cancel_onboarding_notes: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 取消入职备注
    employee_form_status: int = attr.ib(
        default=0, metadata={"req_type": "json"}
    )  # 入职登记表状态, 可选值有: `1`：未发送, `2`：待提交, `3`：已提交
    create_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 创建时间
    update_time: int = attr.ib(default=0, metadata={"req_type": "json"})  # 更新时间


@attr.s
class GetEHREmployeeListRespItem(object):
    user_id: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 员工的用户 ID,user_id_type 为 user_id 时返回 user_id；,user_id_type 为 open_id 时返回 open_id；,user_id_type 为 union_id 时返回 uion_id；,「待入职」和「已取消入职」的员工，此字段值为 null
    system_fields: GetEHREmployeeListRespItemSystemFields = attr.ib(
        default=None, metadata={"req_type": "json"}
    )  # 系统字段
    custom_fields: typing.List[GetEHREmployeeListRespItemCustomField] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 自定义字段


@attr.s
class GetEHREmployeeListResp(object):
    items: typing.List[GetEHREmployeeListRespItem] = attr.ib(
        factory=lambda: [], metadata={"req_type": "json"}
    )  # 员工列表
    page_token: str = attr.ib(
        default="", metadata={"req_type": "json"}
    )  # 分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token
    has_more: bool = attr.ib(
        factory=lambda: bool(), metadata={"req_type": "json"}
    )  # 是否还有更多项


def _gen_get_ehr_employee_list_req(request, options) -> RawRequestReq:
    return RawRequestReq(
        dataclass=GetEHREmployeeListResp,
        scope="EHR",
        api="GetEHREmployeeList",
        method="GET",
        url="https://open.feishu.cn/open-apis/ehr/v1/employees",
        body=request,
        method_option=_new_method_option(options),
        need_tenant_access_token=True,
    )
