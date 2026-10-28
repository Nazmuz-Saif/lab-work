"""Browser (Selenium) smoke test. Run with both servers up:
   backend:  python manage.py runserver
   frontend: npm run dev
   then:     python -m unittest ui_tests.ui_smoke -v
"""
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

FRONTEND_URL = "http://localhost:5173"


class SmokeTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1280,900")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_home_page_loads(self):
        self.driver.get(FRONTEND_URL)
        heading = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        self.assertIn("Lab Project", heading.text)


if __name__ == "__main__":
    unittest.main()
