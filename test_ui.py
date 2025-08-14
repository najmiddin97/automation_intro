from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://funway.upgrow.uz/")


def test_batafsil():
    batafsil_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Batafsil']]"))
    )
    batafsil_button.click()


    title = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "span"))
    )
    assert title.text == "Tavsif"

    browser.quit()
test_batafsil()