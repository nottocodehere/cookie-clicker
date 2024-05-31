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
                           "buyPortal", "buyTime machine", "buyElder Pledge"][::-1]

        self.cookie_speed = {
            "buyCursor": 0.2,
            "buyGrandma": 0.8,
            "buyFactory": 4,
            "buyMine": 10,
            "buyShipment": 20,
            "buyAlchemy lab": 100,
            "buyPortal": 1333.2,
            "buyTime machine": 24691.2,
        }

        self.click_cookie()
        # self.buy_upgrades()

    def click_cookie(self):
        delay = datetime.datetime.now() + timedelta(seconds=6)

        while datetime.datetime.now() < delay:
            self.cookie.click()
        # initiating to buy
        self.get_upgrades_list()

        if datetime.datetime.now() <= self.program_end:
            self.click_cookie()
        else:
            self.stop_clicks()

    def get_balance(self):
       return int(self.driver.find_element(By.ID, value="money").text.replace(",", ""))


    def get_upgrades_list(self):
        print(f"looking for upgrades...")
        available_upgrades = self.driver.find_elements(
            By.XPATH, value='//div[@id="store"]//div[starts-with(@id,"buy") and not(@class="grayed")]')

        if len(available_upgrades) >= 1:
            #call function
            self.buy_upgrades(available_upgrades=available_upgrades)
        # elif len(available_upgrades) == 1 and available_upgrades[0].get_attribute("id") != "buyCursor":
        #     print("Only option, buying")
        #     available_upgrades[0].click()
        else:
            print("Nothing to buy yet")
            pass

    def buy_upgrades(self, available_upgrades):
        upgrades_dict = {}
        # get price of the item
        try:
            for item in available_upgrades:

                # getting price
                item_price = float(item.find_element(By.TAG_NAME, value="b").text.split("- ")[1].replace(",", ""))
                # calculating the value of the upgrade how many cookies per second will give us one spent coin #cps / price
                item_true_value = self.cookie_speed[item.get_attribute("id")] / item_price
                upgrades_dict[item.get_attribute("id")] = item_true_value


            if max(upgrades_dict.values()) < 0.0035:
                print("No reason to spend money, saving")
            else:
                print(f"UPGRADES_DICT {upgrades_dict}")
                purchase_key = list(upgrades_dict.keys())[list(upgrades_dict.values()).index(max(upgrades_dict.values()))]
                self.driver.find_element(By.ID, value=purchase_key).click()
            # here's the experiment, we are setting threshold to 0.0015


        except StaleElementReferenceException as exc:
            print(f"EXCEPTION TRACKED, refreshing {exc}")
            self.get_upgrades_list()



    # def buy_upgrade(self):
    #     list(d.keys())[list(d.values()).index(max(d.values()))]
    #     65
    #
    #     for item in available_upgrades:
    #         self.cookie_speed[item.get_attribute("id")] / item_price
    #

            # getting the key of the value list(mydict.keys())[list(mydict.values()).index(16)]



    def buy_upgrades2(self):
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


# _____________________________________ info __________________________________________________________#

    # these are very basic coefficients for calculating gain
    # cps += Times * 123456 / 5; (24691.2)
    # cps += Portals * 6666 / 5; (1333.2)
    # cps += Labs * 500 / 5; (100)
    # cps += Shipments * 100 / 5; (20)
    # cps += Mines * 50 / 5; (10)
    # cps += Factories * 20 / 5; (4)
    # cps += Grandmas * grandmaGain / 5; (0.8)
    # cps += Cursors * cursorGain / 5; (0.2)

    # value = speed / cps

    # self.cookie_speed = {
    #     "buyCursor": 0.2,
    #     "buyGrandma": 0.8,
    #     "buyFactory": 4,
    #     "buyMine": 10,
    #     "buyShipment": 20,
    #     "buyAlchemy lab": 100,
    #     "buyPortal": 1333.2,
    #     "buyTime machine": 24691.2
    # }


# record without threshold -> 50.4
# with threshold -> 50.2
# updated threshold - 54.6
# updated threshold + lowered delay to 3 secs 50.6
# updated threshold (0.003)+ lowered delay to 3 - 52.8
# updated threshold (0.003)+ lowered delay to 6 - 56.8
# updated threshold (0.003)+ lowered delay to 6 - 61.2