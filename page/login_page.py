import allure
from base.base_action import BaseAction
import base
"""
负责登录页面的逻辑
"""


class LoginPage(BaseAction):

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    # 输入登录逻辑
    @allure.step("登录逻辑")
    def login_in(self,username,password):
        # 登录 输入账号
        allure.attach("登录","输入账号")
        self.send_element_content(base.input_account_id,username)
        # 登录 输入密码
        allure.attach("登录", "输入密码")
        self.send_element_content(base.input_password_id,password)
        # 点击登录按钮
        allure.attach("登录", "登录按钮")

        self.click_element(base.logon_button)


    # 关闭登录页面
    @allure.step("关闭登录页面")
    def close_login_page(self):
        self.click_element(base.left_btn_image)


