from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

class TaoBao():

    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches',['enable-automation'])

        self.browser = webdriver.Chrome()
        self.wait =WebDriverWait(self.browser,10)

    def login(self):


        self.browser.get(self.url)

        self.browser.implicitly_wait(30)
        self.browser.find_element_by_xpath("//a[@class='forget-pwd J_Quick2Static']").click()
        #点击微博登录按钮
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_xpath("//li[@id='J_OtherLogin']/a").click()

        #输入微博账号
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_xpath("//div[@class='inp username']/input").send_keys(username)

        #输入微博密码
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_xpath("//div[@class='inp password']/input").send_keys(password)

        #点击确认按钮
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_xpath("//div[@class='btn_tip']/a").click()

        taobao_name = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='site-nav-user']/a")))

        print(taobao_name.text)
        self.browser.implicitly_wait(30)
        my_taobao = self.browser.find_element_by_xpath("//span[contains(text(),'我的淘宝')]")
        ActionChains(self.browser).move_to_element(my_taobao).perform()
        self.browser.implicitly_wait(30)
        my_buy_goods = self.browser.find_element_by_xpath("//div[@class='site-nav-menu-bd site-nav-menu-list']/div/a[1]").click()

        current_url = self.browser.current_url


    def save_cookies_and_url(self):
            cookies = self.browser.get_cookies()
 
            with open("cookies.txt","w") as f:
                f.write(str(cookies))
            time.sleep(10) #确保cookies写入

            # self.browser.close()




if __name__=='__main__':
        chromedriver_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe'
        #############是从微博模拟登陆,输入微博账号密码。###################
        username = input("username：")  # 这里换成你的账户
        password = input("password：") #这里换成你密码
        s=TaoBao()
        s.login()
        s.save_cookies_and_url()










