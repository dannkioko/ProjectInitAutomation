from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from dotenv import load_dotenv

class Git():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

    def login(self):
        print("*********************** Logging in to Github **********************")
        self.driver.get("http://github.com/"+self.username)
        # self.driver.set_window_size()
        sign_in_elem = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
        if sign_in_elem:
            sign_in_elem.send_keys(Keys.ENTER)
            self.driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(self.username)
            self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
            self.driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()
    
    def createRepo(self, projectName):
        print("******************* Creating Github Repo ("+projectName+")*******************")
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/summary').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/details-menu/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="repository_name"]').send_keys(projectName)
        self.driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button').click()

