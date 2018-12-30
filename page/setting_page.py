import allure

from base.base_action import BaseAction
# 设置页面的退出等相关
import base



class SettingPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step("退出逻辑")
    def logout_account(self):
        self.swipe_screen(1)
        allure.attach('点击退出按钮')
        self.click_element(base.setting_logout)
        allure.attach('点击退出之后的确定按钮')
        self.click_element(base.ymdialog_right_button)