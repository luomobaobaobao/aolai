import allure
from base.base_action import BaseAction
import base
# 登录界面点击已有账号去登录
class SingInPage(BaseAction):

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    @allure.step("点击已有账户去登录")
    # 点击已有账户去登录
    def click_exist_accout(self):
        self.click_element(base.sign_in_id)