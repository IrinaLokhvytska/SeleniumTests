import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPage404(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(
            executable_path="/usr/local/bin/chromedriver",
            chrome_options=chrome_options
        )
        self.driver.get("http://localhost:5000/?")

    def test_search_title(self):
        assert "SeleniumTests" in self.driver.title

    def test_status_code(self):
        status_code = self.driver.find_element_by_id('status-code').text
        self.assertEqual('404', status_code)

    def test_navigate_to_home_page(self):
        wait = WebDriverWait(self.driver, 5)
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Home page')))
        try:
            link.click()
        except Exception as e:
            print(e)
            self.driver.execute_script("document.getElementById('home-page').click()")
        self.assertTrue(self.driver.find_element_by_id('todo-list-example'))

    def tearDown(self):
        self.driver.close()


class TestToDoListsPage(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(
            executable_path="/usr/local/bin/chromedriver",
            chrome_options=chrome_options
        )
        self.driver.get("http://localhost:5000/")

    def test_search_title(self):
        assert "SeleniumTests" in self.driver.title

    def test_add_to_do(self):
        new_to_do = 'Add new todo in the list'
        input_area = self.driver.find_element_by_id('new-todo')
        input_area.send_keys(new_to_do)
        self.driver.find_element_by_id("todo-submit").submit()
        to_do_list = self.driver.find_element_by_class_name('list-group')
        items = to_do_list.find_elements_by_tag_name("li")
        self.assertEqual('Remove {}'.format(new_to_do), items[-1].text)
        self.assertEqual(4, len(items))

    def test_remove_to_do(self):
        to_do_list = self.driver.find_element_by_class_name('list-group')
        items = to_do_list.find_elements_by_tag_name("li")
        items[-1].find_element_by_tag_name("button").click()
        self.assertEqual(3, len(items))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
