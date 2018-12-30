
from selenium.webdriver.common.by import By
# 主页的按钮  我
home_my_button = By.ID,"com.yunmall.lc:id/tab_me"
# 点击已有账号登录
sign_in_id = By.ID,"com.yunmall.lc:id/gotologon"
# 登录界面
    # 账号 密码
input_account_id = By.ID,"com.yunmall.lc:id/logon_account_textview"
input_password_id = By.ID,"com.yunmall.lc:id/logon_password_textview"
    # 登录按钮
logon_button = By.ID,"com.yunmall.lc:id/logon_button"
    # 登录左上角关闭按钮
left_btn_image = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"

# 登录成功后的个人中心页面
    # 左上角的设置按钮
ymtitlebar_left_btn_image = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
    # 全部订单按钮
order_more_txt = By.ID,"com.yunmall.lc:id/order_more_txt"


# 进入设置之后
    # 退出按钮
setting_logout = By.ID,"com.yunmall.lc:id/setting_logout"
    # 确认退出按钮
ymdialog_right_button = By.ID,"com.yunmall.lc:id/ymdialog_right_button"

