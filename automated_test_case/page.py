from locator import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    
    #Checks if actual page title matches the expected one
    def is_title_matches(self):
        return "Daily Todo" in self.driver.title
    
    #Clicks the "Create your Daily Todo list" button
    def click_create_button(self):
        element = self.driver.find_element(*MainPageLocator.CREATE_BUTTON)
        element.click()
    
    #Fills the textarea and submit
    def fill_textarea_and_submit(self):
        textarea = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocator.TEXTAREA_INPUT)
        )
        input_data = "task1\ntask2\ntask3\ntask4"
        textarea.send_keys(input_data)
        saveTasksButton = self.driver.find_element(*MainPageLocator.SAVE_TASKS_BUTTON)
        saveTasksButton.click() 
    
    #Check if actual taks matches excepted ones
    def is_input_marches_results(self):
        expectedResults = ['task1', 'task2', 'task3', 'task4']
        taskList = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocator.TASK_LIST_ELEMENT)
        )
        tasks = taskList.find_elements(*MainPageLocator.TASK_ELEMENT)
        actualResults = []
        for task in tasks:
            actualResults.append(task.text)

        return actualResults == expectedResults
