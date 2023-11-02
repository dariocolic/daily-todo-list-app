import unittest
from selenium import webdriver
import page

class CreateTodoList(unittest.TestCase): 
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://dailytodo.org/")
    
    # Test create Todo list feature
    def test_create_list(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.click_create_button()
        mainPage.fill_textarea_and_submit()
        assert mainPage.is_input_marches_results()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()