import allure
from base.base_action import BaseAction
import base
# 主界面 中点击我的
class HomePage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    # 点击我的
    @allure.step("点击我的")
    def click_my_button(self):
        self.click_element(base.home_my_button)