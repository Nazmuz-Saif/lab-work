import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "http://localhost:5173"
CODE = "00" + str(int(time.time()))


class ProductPageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(URL)

    def tearDown(self):
        self.driver.quit()

    def fill_and_save(self, code, name, price):
        self.driver.find_element(By.ID, "product_code").send_keys(code)
        self.driver.find_element(By.ID, "product_name").send_keys(name)
        self.driver.find_element(By.ID, "price").send_keys(price)
        self.driver.find_element(By.ID, "save").click()

    def test_successful_insertion(self):
        self.fill_and_save(CODE, "Blue Pen", "12.50")

        self.wait.until(EC.text_to_be_present_in_element((By.ID, "list"), CODE))
        table_text = self.driver.find_element(By.ID, "list").text
        self.assertIn("Blue Pen", table_text)
        self.assertIn("12.50", table_text)

    def test_invalid_price_is_rejected(self):
        self.fill_and_save(CODE + "9", "Bad Price", "abc")

        self.wait.until(EC.presence_of_element_located((By.ID, "error")))
        self.assertIn("price", self.driver.find_element(By.ID, "error").text)
        self.assertNotIn(CODE + "9", self.driver.find_element(By.ID, "list").text)


if __name__ == "__main__":
    unittest.main()
