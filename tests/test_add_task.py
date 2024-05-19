import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestAddTask:

    def test_add_task(self):
        self.driver.get("http://127.0.0.1:8080/") 
        task_input = self.driver.find_element(By.ID, 'taskInput')
        add_task_btn = self.driver.find_element(By.ID, 'addTaskBtn')

        task_input.send_keys('New Task')
        add_task_btn.click()

        time.sleep(1)  # Wait for task to be added

        task_list = self.driver.find_element(By.ID, 'taskList')
        assert 'New Task' in task_list.text
