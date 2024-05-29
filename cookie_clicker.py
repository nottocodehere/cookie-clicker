from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
from datetime import timedelta

class CookieClicker:

    def __init__(self):
        #setting options and launching webdriver
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                       options=self.chrome_options)
        self.driver.get("https://orteil.dashnet.org/experiments/cookie/")
        self.cookie = self.driver.find_element(By.ID, value="cookie")

        # setting up class names for buying upgrades
        self.purchase_values = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab",
                           "buyPortal", "buyTime machine"][::-1]


        #running the clicker the recursive func that constantly hits the cookie button
        self.click_cookie()
        self.buy_upgrades()

    def click_cookie(self):
        while True:
            # cookie click
            self.cookie.click()

        # self.click_cookie()

    def get_balance(self):
        # getting balance
        # self.money = int(self.driver.find_element(By.ID, value="money").text)
        #TODO I suppose the last option is better
        return int(self.driver.find_element(By.ID, value="money").text)

    def buy_upgrades(self):
        # upgrades_dict = {
        #     "cursor":  self.driver.find_element(By.ID, value="buyCursor"),
        #     "grandma": self.driver.find_element(By.ID, value="buyGrandma"),
        #     "factory": self.driver.find_element(By.ID, value="buyFactory"),
        #     "mine": self.driver.find_element(By.ID, value="buyMine"),
        #     "shipment": self.driver.find_element(By.ID, value="buyShipment"),
        #     "alch_lab": self.driver.find_element(By.ID, value="buyAlchemy lab"),
        #     "portal": self.driver.find_element(By.ID, value="buyPortal"),
        #     "t_machine": self.driver.find_element(By.ID, value="buyTime machine")
        # }
        # prices_dict = {key: float(value.find_element(By.TAG_NAME, value="b").text.split("- ")[1].replace(",", ""))
        #                for (key, value) in upgrades_dict.items()}
        #
        # self.get_balance()
        prices_dict = {}
        for item in self.purchase_values:
            # print(item)
            select = self.driver.find_element(By.ID, value=item)
            print(f"SELECT -> {select.text}")
            print(select.get_attribute("class"))
            if select.get_attribute("class") == "":
                prices_dict[item] = float(select.find_element(By.TAG_NAME, value="b").text.split("- ")[1].replace(",", ""))
                if prices_dict[item] <= self.get_balance():
                    select.click()
