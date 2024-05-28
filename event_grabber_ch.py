from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import datetime

event_dict = {}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.python.org")

events_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li")
print(f"EVENTS: {[x.text for x in events_list]}")

def dict_former(dict_to_write, position, **kwargs):
    """writes key-value pairs to dict for uploading. when everything is written, the file is being uploaded"""
    for key, value in kwargs.items():
        dict_to_write[position] = kwargs
    # print(dict_to_write)
    return dict_to_write

for number, element in enumerate(events_list):
    time_iso = element.find_element(By.TAG_NAME, value="time").get_attribute("datetime")
    time = datetime.datetime.fromisoformat(time_iso).strftime("%Y-%m-%d")
    name = element.find_element(By.TAG_NAME, value="a").text
    dict_former(event_dict, number, time=time, name=name)

print(f"DICT OF EVENTS => {event_dict}")
driver.quit()