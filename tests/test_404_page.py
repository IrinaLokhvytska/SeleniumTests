import unittest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


class TestPage404(unittest.TestCase):
    config = Config()
    host_name = config.host_name
    port_number = config.port_number
    path = 'dev'

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(
            executable_path=self.config.get_executable_path(self.path),
            options=chrome_options
        )
        self.driver.get("http://{0}:{1}/?".format(self.host_name, self.port_number))

    def test_navigate_to_home_page(self):
        wait = WebDriverWait(self.driver, 5)
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Home page')))
        try:
            link.click()
        except Exception as e:
            print(e)
            self.driver.execute_script("document.getElementById('home-page').click()")
        self.assertTrue(self.driver.find_element_by_id('todo-list-example'))

    def test_search_title(self):
        assert "SeleniumTests" in self.driver.title

    def test_status_code(self):
        status_code = self.driver.find_element_by_id('status-code').text
        self.assertEqual('404', status_code)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        TestPage404.path = sys.argv.pop()
    unittest.main()
