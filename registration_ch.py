from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element(By.XPATH, value="/html/body/form/input[1]")
# or
# name = driver.find_element(By.NAME, value="fName")
name.send_keys("Lemmy")
last_name = driver.find_element(By.XPATH, value="/html/body/form/input[2]")
last_name.send_keys("Kilmister")
email = driver.find_element(By.XPATH, value="/html/body/form/input[3]")
email.send_keys("razor@motorhead.com")

button = driver.find_element(By.CSS_SELECTOR, value="form button")
# button.send_keys(Keys.ENTER)
button.click()
