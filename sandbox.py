# import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# making chrome stay open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# # driver.get("https://www.amazon.com")
# driver.get("https://www.amazon.de/-/en/6922621504290/dp/B0CCP8KYGG/ref=nav_signin?crid=B4YRUGW5XT2I&dib=eyJ2IjoiMSJ9.4-OBWNSxdiU0AHx5kku1ULnX-MlkkpT5UDXtVOjVuLdBpJzGA30p4H-fO9gk2qh4MOf3X4qX2vi4D43W-H3kQYla2G8S2PJc2QEK56MX1JVZdfI5kRAkOmJfKRlgjhvYfVbB0ZtfTR7bJqHlZXhBvOH62J3t3QQtGv-pJcARUNjE3G5Wwm1tTDtzt9RUfRe437lFpH1zSjQ1zEN_ShwRBVX9fynnV5zkv5whAhS8sKg.BrxAVrUxtjvgc1B4KQaYX7kJ6cAjZgCI-vpyFQRsRK4&dib_tag=se&keywords=8bitdo+keyboard&qid=1715958752&sprefix=keyboard+bi%2Caps%2C129&sr=8-2")
# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"THE PRICE IS: {price_whole.text}.{price_cents.text}")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# driver.get("https://www.amazon.com")
driver.get("https://www.python.org")

search_bar = driver.find_element(By.NAME, value="q")

button = driver.find_element(By.ID, value="submit")
print(button.size)
# print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")

print(doc_link.text)

# driver.find_element(By)

# close particular tab driver.close()
# shutdown browser driver.quit()
driver.quit()