from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Przypadek testowy sprawdzający działanie wyszukiwarki bez wpisywania wartości
def test_search_none_booking():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://booking.com/")
    cookie = driver.find_element(By.ID, "onetrust-reject-all-handler")
    cookie.click()
    search = driver.find_element(By.CLASS_NAME, "de576f5064")
    search.click()
    x = driver.find_element(By.ID, "b2indexPage")
    x.send_keys(Keys.ESCAPE)
    where_to_go = driver.find_element(By.ID, ":rh:")
    where_to_go.click()
    where_to_go.send_keys(Keys.ENTER)
    walidation = driver.find_element(By.CLASS_NAME, "b9b405fa52")
    assert walidation.text.startswith("Enter")
    driver.quit()

# Przypadek testowy sprawdzający działanie wyszukiwarki po uprzednim wpisaniu frazy
def test_search_completed_booking():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://booking.com/")
    cookie = driver.find_element(By.ID, "onetrust-reject-all-handler")
    cookie.click()
    where_to_go = driver.find_element(By.ID, ":rh:")
    where_to_go.click()
    where_to_go.send_keys("Gdańsk, pomorskie, Polska")
    sleep(1)
    where_to_go.send_keys(Keys.ARROW_DOWN)
    where_to_go.send_keys(Keys.ENTER)
    where_to_go.send_keys(Keys.ENTER)
    result = driver.find_element(By.CLASS_NAME, "d4a98186ec")
    assert result.text.startswith("Gdańsk")
    driver.quit()