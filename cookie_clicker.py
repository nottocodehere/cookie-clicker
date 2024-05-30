from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import datetime
from datetime import timedelta
import time

class CookieClicker:

    def __init__(self):
        self.program_end = datetime.datetime.now() + timedelta(seconds=300)
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
        self.click_cookie()
        # self.buy_upgrades()

    def click_cookie(self):
        delay = datetime.datetime.now() + timedelta(seconds=3)

        while datetime.datetime.now() < delay:
            self.cookie.click()
        self.buy_upgrades()

        if datetime.datetime.now() <= self.program_end:
            self.click_cookie()
        else:
            self.stop_clicks()

    def get_balance(self):
       return int(self.driver.find_element(By.ID, value="money").text)

    def buy_upgrades(self):
        print("FUNCTION CALLED")
        prices_dict = {}

        for item in self.purchase_values:

            try:
                select = self.driver.find_element(By.ID, value=item)
                if select.get_attribute("class") == "":
                    prices_dict[item] = float(select.find_element(By.TAG_NAME, value="b").text.split("- ")[1].replace(",", ""))

                    if prices_dict[item] <= self.get_balance():
                        select.click()
                    break

            except StaleElementReferenceException as exc:
                print(f"EXCEPTION TRACKED {exc}")
                select = self.driver.find_element(By.ID, value=item)
                if select.get_attribute("class") == "":
                    prices_dict[item] = float(
                        select.find_element(By.TAG_NAME, value="b").text.split("- ")[1].replace(",", ""))

                    if prices_dict[item] <= self.get_balance():
                        select.click()
                    break

    def get_cookies_per_s(self):
        return self.driver.find_element(By.ID, value="cps").text


    def stop_clicks(self):

        return print(f"You have collected -> {self.get_balance()} cookies in 5 minutes "
                      f"\nCookies per second -> {self.get_cookies_per_s()}"), self.driver.quit()

