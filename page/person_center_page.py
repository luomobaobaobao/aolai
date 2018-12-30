import allure
from base.base_action import BaseAction
import base
"""
负责 个人中心页面逻辑
"""
class PersonCenterPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    @allure.step("个人中心页面逻辑")
    def click_person_center_setting(self):
        # 点击个人中心的设置按钮
        allure.attach('点击个人中心的设置按钮')
        self.click_element(base.ymtitlebar_left_btn_image)
    # 判断是否登录成功
    @allure.step("判断是否登录成功")
    def is_login_sucess(self):
        try:
            self.find_element(base.order_more_txt)
            return True
        except:
            return False