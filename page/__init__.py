from selenium.webdriver.common.by import By

"""以下为个人中心配置数据"""
# 同意免责声明
disclaimer = By.ID, "com.xraybot.jiujiutouyan:id/tv_confirm"
# 我的
my = By.XPATH, "//*[contains(@text,'我的')]"
# 推荐自选
close_optional = By.ID, "com.xraybot.jiujiutouyan:id/iv_cancel"
# 个人中心
personal_center = By.ID, "com.xraybot.jiujiutouyan:id/iv_user_center"
# 去登录
to_login = By.ID, "com.xraybot.jiujiutouyan:id/iv_image"
# 手机号
input_phone = By.ID, "com.xraybot.jiujiutouyan:id/cce_phone"
# 图片验证码
input_img_code = By.ID, "com.xraybot.jiujiutouyan:id/cce_imgcode"
# 短信验证码
input_note_code = By.ID, "com.xraybot.jiujiutouyan:id/cce_sms"
# 登录按钮
login_btn = By.ID, "com.xraybot.jiujiutouyan:id/btn_login"
# 软件设置
software_setting = By.ID, "com.xraybot.jiujiutouyan:id/tv_setting"
# 个人信息
personal_information = By.XPATH, "//*[contains(@text,'个人信息')]"
# 昵称
nickname = By.ID, "com.xraybot.jiujiutouyan:id/rl_name"
# 编辑昵称
edit_nickname = By.ID, "com.xraybot.jiujiutouyan:id/et_name"
# 确定按钮
confirm_btn = By.ID, "com.xraybot.jiujiutouyan:id/btn_done"
# 性别
Sex = By.ID, "com.xraybot.jiujiutouyan:id/rl_sex"
# 选择性别
sex_selection = By.XPATH, "//*[contains(@text,'男')]"
# 职业
profession = By.ID, "com.xraybot.jiujiutouyan:id/rl_profession"
# 输入职业
input_profession = By.ID, "com.xraybot.jiujiutouyan:id/et_name"
# 通信地址
mailing_address = By.ID, "com.xraybot.jiujiutouyan:id/tv_address"
# 输入通信地址
input_address = By.ID, "com.xraybot.jiujiutouyan:id/et_name"
# 邮箱
email = By.ID, "com.xraybot.jiujiutouyan:id/tv_email"
# 输入邮箱
input_email = By.ID, "com.xraybot.jiujiutouyan:id/et_name"
# 个性签名
introduction = By.ID, "com.xraybot.jiujiutouyan:id/tv_introduction"
# 输入个人简介
input_introduction = By.ID, "com.xraybot.jiujiutouyan:id/et_introduction"
# 个人简介页确定
confirm_personal = By.XPATH, "//*[contains(@text,'确定')]"
# 个人中心返回按钮
personal_center_back_btn = By.CLASS_NAME, "android.widget.TextView"
# 验证昵称
verify_nickname = By.ID, "com.xraybot.jiujiutouyan:id/tv_name"
# 性别验证
verify_sex = By.ID, "com.xraybot.jiujiutouyan:id/tv_sex"
# 验证职业
verify_profession = By.ID, "com.xraybot.jiujiutouyan:id/tv_profession"
# 验证通信地址
verify_mailing_address = By.ID, "com.xraybot.jiujiutouyan:id/tv_address"
# 验证邮箱
verify_email = By.ID, "com.xraybot.jiujiutouyan:id/tv_email"
# 验证个性签名
verify_introduction = By.ID, "com.xraybot.jiujiutouyan:id/tv_introduction"

"""以下为个股详情现价检查配置数据"""
# 首页搜索框
search_index = By.ID, "com.xraybot.jiujiutouyan:id/tv_search"
# 搜索按钮
search_btn = By.ID, "com.xraybot.jiujiutouyan:id/buttonback"
# 个股详情
stock_detail = By.ID, "com.xraybot.jiujiutouyan:id/iv_up"
# 现价或收盘价
current_price = By.ID, "com.xraybot.jiujiutouyan:id/main_tv_close"
# 返回到搜索框按钮
back_btn = By.CLASS_NAME, "android.widget.TextView"
# 搜索框
search_box = By.ID, "com.xraybot.jiujiutouyan:id/et_searchtext_search"
# 综合表盘
Comprehensive_dial = By.ID, "com.xraybot.jiujiutouyan:id/clock_view_zonghe"
# 基本面表盘
Base_face_dial = By.ID, "com.xraybot.jiujiutouyan:id/clock_view_base_face"
# 财报可信度表盘
Report_reliable_dial = By.ID, "com.xraybot.jiujiutouyan:id/clock_view_caibao_kexindu"
# 估现差率表盘
Now_the_rate_dial = By.ID, "com.xraybot.jiujiutouyan:id/clock_view_guxiancha_rate"
# 波动风险表盘
Fluctuation_risk_dial = By.ID, "com.xraybot.jiujiutouyan:id/clock_view_bodong_fengxian"

"""以下为估值工具核心科目检查配置数据"""
# 工具
tools = By.XPATH, "//*[contains(@text,'工具')]"
# 估值工具
valuation_tools = By.ID, "com.xraybot.jiujiutouyan:id/tv_btn_woyao_guzhi"
# 估值搜索框
valuation_search = By.ID, "com.xraybot.jiujiutouyan:id/et_searchtext_search"
# 搜索按钮 (上面有)

# 增速选择
select_growth_rate = By.XPATH, "//*[contains(@text,'请选择')]"
# 最近1年增速
one_year_growth_rate = By.XPATH, "//*[contains(@text,'最近1年增速')]"
# 最近2年增速
two_year_growth_rate = By.XPATH, "//*[contains(@text,'最近2年增速')]"
# 最近3年增速
three_year_growth_rate = By.XPATH, "//*[contains(@text,'最近3年增速')]"
# 我的估值结果
valuation_result = By.ID, "com.xraybot.jiujiutouyan:id/tv_pb_result"
# 2019
year2020 = By.XPATH, "//*[contains(@text,'2020')]"
# 2020
year2021 = By.XPATH, "//*[contains(@text,'2021')]"
# 2021
year2022 = By.XPATH, "//*[contains(@text,'2022')]"
# PB估值
valuation_pb = By.XPATH, "//*[contains(@text,'PB估值')]"
# PE估值
valuation_pe = By.XPATH, "//*[contains(@text,'PE估值')]"
# PS估值
valuation_ps = By.XPATH, "//*[contains(@text,'PS估值')]"

"""以下为估值工具结果科目检查配置数据"""
# 结果科目
result_subject = By.XPATH, "//*[contains(@text,'结果科目')]"
# 每股净利润
every_profit = By.XPATH, "//*[contains(@text,'每股净利润')]"
# 每股净资产
every_property = By.XPATH, "//*[contains(@text,'每股净资产')]"
# 每股净销售
every_market = By.XPATH, "//*[contains(@text,'每股净销售')]"

"""以下为暂停上市、退市、重大资产重组、新上市股票估值工具检查配置数据"""
# 重要提示
important_note = By.ID, "com.xraybot.jiujiutouyan:id/tv_content"
# 确定
important_confirm = By.XPATH, "//*[contains(@text,'确定')]"
