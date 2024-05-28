from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]")
print(f"OVERALL ARTICLE NUMBER = {articles.text}")
articles.click()

# one can find and click links By.Link_text

#typing -> send_keys("python")
search = driver.find_element(By.NAME, value="search")

search.send_keys("python", Keys.ENTER)

#returning key
driver.quit()

