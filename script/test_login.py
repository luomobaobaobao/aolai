import os,sys
sys.path.append(os.getcwd())
import time
import pytest
from base.init_driver import get_driver
from page.navigation_page import NavigationPage
from base.read_yaml_data import read_yaml_data


def get_read_data():
    data_list = []
    data = read_yaml_data("login_data.yaml")
    for i in data.keys():
        readdata = data.get(i)
        username = readdata.get("username")
        password = readdata.get("password")
        tag = readdata.get("tag")
        get_toast_msg = readdata.get("get_toast_msg")
        except_msg = readdata.get("except_msg")
        data_list.append((username,password,tag,get_toast_msg,except_msg))
        return data_list

class TestLogin:

    def setup_class(self):
        self.driver = get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        self.navigation_page = NavigationPage(self.driver)
    def teardown_class(self):
        time.sleep(1)
        self.driver.quit()
    @pytest.mark.parametrize("username,password,tag,get_toast_msg,except_msg",get_read_data())
    def test_login(self,username,password,tag,get_toast_msg,except_msg):
        # 点击我的
        self.navigation_page.get_home_page().click_my_button()
        # 点击已有账号去登录
        self.navigation_page.get_sign_in_page().click_exist_accout()
        # 输入用户名密码
        self.navigation_page.get_login_page().login_in(username,password)
        if tag == 1:
            try:
                login_state = self.navigation_page.get_person_center_page().is_login_sucess()
                self.navigation_page.get_person_center_page().click_person_center_setting()
                self.navigation_page.get_setting_page().logout_account()
                assert login_state,self.navigation_page.get_setting_page().get_screen()
            except:
                self.navigation_page.get_setting_page().get_screen()
                self.navigation_page.get_login_page().close_login_page()
        else:
            try:
                login_stata = self.navigation_page.get_login_page().get_toast_message(get_toast_msg)
                assert login_stata == except_msg,self.navigation_page.get_setting_page().get_screen()
            finally:
                self.navigation_page.get_login_page().close_login_page()




