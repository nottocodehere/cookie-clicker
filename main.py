from cookie_clicker import CookieClicker as cc

clicker = cc()

while True:
    cc.buy_upgrades()



# # timer part
# program_end = datetime.datetime.now() + timedelta(seconds=300)
#
#

#
# purchase_values = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab",
#                    "buyPortal", "buyTime machine"][::-1]
#
# # purchase_dict = {
# #     key: float(driver.find_element(By.CSS_SELECTOR, value=key).text.split("- ")[1]) for key in purchase_values
# # }
#
# # //div[not(contains(@class, "greyed"))]
# # here go purchases
# cursor = driver.find_element(By.ID, value="buyCursor")
# grandma = driver.find_element(By.ID, value="buyGrandma")
# factory = driver.find_element(By.ID, value="buyFactory")
# mine = driver.find_element(By.ID, value="buyMine")
# shipment = driver.find_element(By.ID, value="buyShipment")
# alch_lab = driver.find_element(By.ID, value="buyAlchemy lab")
# portal = driver.find_element(By.ID, value="buyPortal")
# t_machine = driver.find_element(By.ID, value="buyTime machine")
#
# upgrades_dict = {
#     "cursor":  driver.find_element(By.ID, value="buyCursor"),
#     "grandma": driver.find_element(By.ID, value="buyGrandma"),
#     "factory": driver.find_element(By.ID, value="buyFactory"),
#     "mine": driver.find_element(By.ID, value="buyMine"),
#     "shipment": driver.find_element(By.ID, value="buyShipment"),
#     "alch_lab": driver.find_element(By.ID, value="buyAlchemy lab"),
#     "portal": driver.find_element(By.ID, value="buyPortal"),
#     "t_machine": driver.find_element(By.ID, value="buyTime machine")
# }
#
# prices_dict = {key: float(value.find_element(By.TAG_NAME, value="b").text.split("- ")[1].replace(",", ""))
#                for (key, value) in upgrades_dict.items()}
# #<div id="buyCursor" onclick="Buy('Cursor');" style="background-image:url(cursoricon.png);" class=""><b>Cursor - <moni></moni> 27</b>Autoclicks every 5 seconds.<div class="amount">5</div></div>
#
# # how to take the price float(cursor.find_element(By.TAG_NAME, value="b").text.split("- ")[1])
# ### SCHEMA //div[@id="store"]//div[starts-with(@id,"buy") and not(@class="grayed")]
#
# while datetime.datetime.now() < program_end:
#     cookie.click()
#     money = int(driver.find_element(By.ID, value="money").text)
#
#     for item in purchase_values:
#         # print(item)
#         select = driver.find_element(By.ID, value=item)
#         print(f"SELECT -> {select.text}")
#         print(select.get_attribute("class"))
#         if select.get_attribute("class") == "":
#             prices_dict[item] = float(select.find_element(By.TAG_NAME, value="b").text.split("- ")[1].replace(",", ""))
#             if prices_dict[item] <= money:
#                 select.click()
#
# cookies_per_s = driver.find_element(By.ID, value="cps").text
# print(f"You have collected -> {money} cookies in 5 minutes\nCookies per second -> {cookies_per_s}")
#
# driver.quit()