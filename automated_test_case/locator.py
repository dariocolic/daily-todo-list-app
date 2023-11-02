from selenium.webdriver.common.by import By

class MainPageLocator(object):
    CREATE_BUTTON = (By.CLASS_NAME, "bigger")
    TEXTAREA_INPUT = (By.TAG_NAME, "textarea")
    SAVE_TASKS_BUTTON = (By.CLASS_NAME, 'big')
    TASK_LIST_ELEMENT = (By.TAG_NAME, 'tbody')
    TASK_ELEMENT = (By.CLASS_NAME, 'text')
