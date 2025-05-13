from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Przypadek testowy sprawdzający działanie wyszukiwarki bez wpisywania wartości
def test_search_none_olx():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://olx.pl/")
    cookie_accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookie_accept.click()
    search = driver.find_element(By.NAME, "searchBtn")
    search.click()
    count = driver.find_element(By.CLASS_NAME, "css-1r6clzs")
    assert count.text.startswith("Znaleźliśmy")
    driver.quit()

# Przypadek testowy sprawdzający działanie wyszukiwarki po uprzednim wpisaniu frazy
def test_search_completed_olx():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://olx.pl")
    cookie_accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookie_accept.click()
    text_area = driver.find_element(By.ID, "search")
    text_area.click()
    text_area.send_keys("praca Warszawa")
    text_area.send_keys(Keys.ENTER)
    count = driver.find_element(By.CLASS_NAME, "css-1r6clzs")
    assert count.text.startswith("Znaleźliśmy")
    driver.quit()
