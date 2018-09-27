import unittest
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import HOST_NAME, PORT_NUMBER, executable_path

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


class TestToDoListsPage(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(
            executable_path=executable_path['prod'],
            options=chrome_options,
        )
        self.driver.get("http://{0}:{1}/".format(HOST_NAME, PORT_NUMBER))

    def test_add_to_do(self):
        new_to_do = 'Add new todo in the list'
        input_area = self.driver.find_element_by_id('new-todo')
        input_area.send_keys(new_to_do)
        self.driver.find_element_by_id("todo-submit").submit()
        to_do_list = self.driver.find_element_by_class_name('list-group')
        items = to_do_list.find_elements_by_tag_name("li")
        self.assertEqual('Remove {}'.format(new_to_do), items[-1].text)
        self.assertEqual(4, len(items))

    def test_search_title(self):
        assert "SeleniumTests" in self.driver.title

    def test_remove_to_do(self):
        to_do_list = self.driver.find_element_by_class_name('list-group')
        items = to_do_list.find_elements_by_tag_name("li")
        items[-1].find_element_by_tag_name("button").click()
        self.assertEqual(3, len(items))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
