import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_basket_button_check(browser):
    browser.get(link)
    time.sleep(2)

    add_to_basket_btn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-add-to-basket')))
    assert add_to_basket_btn, '"Add to basket" button was not found'