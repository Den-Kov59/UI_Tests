from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Testing_Class:
    def test_Search(self):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://www.reddit.com/")
        browser.implicitly_wait(30)
        browser.find_element(By.ID, "header-search-bar").send_keys("cats")
        browser.find_element(By.ID, "header-search-bar").send_keys(Keys.RETURN)
        expected_text = "r/cats"
        found_text = browser.find_element(
            By.XPATH, "//*[contains(text(), '{0}')]".format(expected_text)
        ).text
        browser.close()
        assert expected_text == found_text

    def test_NightMode(self):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://www.reddit.com/")
        browser.implicitly_wait(30)
        browser.find_element(By.ID, "USER_DROPDOWN_ID").click()
        browser.find_elements(
            By.XPATH, "//*[contains(text(), '{0}')]".format("Night Mode")
        )[0].click()
        browser.find_element(By.ID, "USER_DROPDOWN_ID").click()
        res = browser.find_element(
            By.CSS_SELECTOR,
            "button[role='switch']",
        ).get_attribute("aria-checked")
        browser.close()
        assert res == "true"
