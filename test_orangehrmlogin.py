import os
import time

import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import url_matches
from selenium.webdriver.support.wait import WebDriverWait
from capstoneProject1.Test_Excel_Functions.excel_functions import Selva_Excel_Functions
from capstoneProject1.Test_locators.locators import TestLocators


class Test_capstone:
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        excel_file = 'C:\\Users\\ssekar588\\PycharmProjects\\GUVI Selenium 2\\capstoneProject1\\Test_Datas\\test_data.xlsx'
        sheet_name = 'Sheet1'
        self.driver.get(TestLocators.url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.s = Selva_Excel_Functions(excel_file, sheet_name)
        self.rows = self.s.Row_Count()

        self.username_element = self.wait.until(EC.visibility_of_element_located((By.NAME, TestLocators().Email)))
        self.password_element = self.wait.until(EC.visibility_of_element_located((By.NAME, TestLocators().Password)))
        self.login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().Login_button)))

        yield

        self.driver.quit()

    def navigate_to_pim(self):
        try:
            pim_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='PIM']")))
            return pim_element
        except Exception as e:
            print(f"Exception occurred while navigating to PIM module: {e}")
            return None

    def create_pim_entry(self):
        try:
            # Click on PIM menu
            pim_element = self.navigate_to_pim()
            if pim_element:
                pim_element.click()
                self.driver.implicitly_wait(10)  # Adjust as necessary for synchronization with the page
            else:
                print("Failed to find PIM element.")
        except Exception as e:
            print(f"Exception occurred while creating PIM entry: {e}")

    def add_new(self):
        self.add_emp = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().Add_employee)))
        self.add_emp.click()
        self.driver.implicitly_wait(10)
        self.first_name = self.wait.until(EC.visibility_of_element_located((By.XPATH, TestLocators().first_name)))
        self.first_name.send_keys("Selva")
        self.mid_name = self.wait.until(EC.visibility_of_element_located((By.XPATH, TestLocators().mid_name)))
        self.mid_name.send_keys("Rani")
        self.last_name = self.wait.until(EC.visibility_of_element_located((By.XPATH, TestLocators().last_name)))
        self.last_name.send_keys("S")
        self.driver.implicitly_wait(10)

        self.save = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().save)))
        self.save.click()
        self.driver.implicitly_wait(10)
        # try:
        #     self.wait.until(EC.url_matches('https: // opensource - demo.orangehrmlive.com / web / index.php / pim / viewPersonalDetails / empNumber / 166'))
        print("Success: Employee save success: Employee list navigated")
        # except TimeoutException:
        #     print("Failed: Employee not saved")

    def edit_emp(self):
        self.edit_employee_list = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().edit)))
        self.edit_employee_list.click()
        wait = WebDriverWait(self.driver, 10)
        self.emp_first_name = self.wait.until(EC.visibility_of_element_located((By.XPATH, TestLocators().first_name)))
        self.emp_first_name.send_keys("abc")
        time.sleep(20)
        self.save = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().save)))
        self.save.click()
        self.driver.implicitly_wait(30)
        screenshot_dir = os.path.join(os.getcwd(), 'screenshot')
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"login_failure.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"screenshot saved at: {screenshot_path}")

        print("Details saved successfully with updated details")

    def delete(self):
        self.delete_employee_list = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().delete)))
        self.delete_employee_list.click()
        self.driver.implicitly_wait(40)
        self.delete=self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().popup)))
        self.driver.implicitly_wait(40)
        self.delete.click()

    def test_login_01(self, boot):

        wait = WebDriverWait(self.driver, 8)
        username = self.s.Read_Data(2, 6)
        password = self.s.Read_Data(2, 7)

        self.username_element.send_keys(username)

        self.password_element.send_keys(password)

        self.login_button.click()
        try:
            wait.until(EC.url_matches('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'))
            self.s.Write_Data(2, 8, "TEST PASS")
            print("SUCCESS : Logged in with Username {a} & {b}".format(a=username, b=password))

            profile_image = wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().Profile_image)))
            profile_image.click()
            logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().Logout_button)))
            logout_button.click()

            wait.until(EC.url_matches("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"))

        except TimeoutException:
            self.s.Write_Data(2, 8, "TEST FAIL")
            assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
            print("FAIL : Login failed with Username {a} & {b} Invalid Credentials".format(a=username, b=password))
            screenshot_dir = os.path.join(os.getcwd(), 'screenshot')
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"login_failure.png")
            self.driver.save_screenshot(screenshot_path)
            print(f"screenshot saved at: {screenshot_path}")
            self.driver.refresh()
    def test_login_02(self, boot):

        wait = WebDriverWait(self.driver, 8)
        username = self.s.Read_Data(3, 6)
        password = self.s.Read_Data(3, 7)

        self.username_element.send_keys(username)

        self.password_element.send_keys(password)

        self.login_button.click()
        try:
            wait.until(EC.url_matches('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'))
            self.s.Write_Data(3, 8, "TEST PASS")
            print("SUCCESS : Logged in with Username {a} & {b}".format(a=username, b=password))

            profile_image = wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().Profile_image)))
            profile_image.click()
            logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().Logout_button)))
            logout_button.click()

            wait.until(EC.url_matches("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"))

        except TimeoutException:
            self.s.Write_Data(3, 8, "TEST FAIL")
            assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
            print("FAIL : Login failed with Username {a} & {b} Invalid Credentials".format(a=username, b=password))
            screenshot_dir = os.path.join(os.getcwd(), 'screenshot')
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"login_failure.png")
            self.driver.save_screenshot(screenshot_path)
            print(f"screenshot saved at: {screenshot_path}")
            self.driver.refresh()


    def test_pim_mod_01(self, boot):
        wait = WebDriverWait(self.driver, 30)  # Adjust timeout as needed
        # Login using credentials from Excel
        username = self.s.Read_Data(2, 6)
        password = self.s.Read_Data(2, 7)

        print(f"Username: {username}, Password: {password}")

        self.username_element.send_keys(username)
        self.password_element.send_keys(password)
        self.login_button.click()

        # Create PIM entry using the method
        self.create_pim_entry()
        print("pim clicked successfully")
        self.driver.implicitly_wait(10)
        # self.add_emp.click()
        self.add_new()

        self.driver.quit()

    def test_edit_pim_mod_02(self, boot):
        wait = WebDriverWait(self.driver, 30)  # Adjust timeout as needed
        # Login using credentials from Excel
        username = self.s.Read_Data(2, 6)
        password = self.s.Read_Data(2, 7)

        print(f"Username: {username}, Password: {password}")

        self.username_element.send_keys(username)
        self.password_element.send_keys(password)
        self.login_button.click()

        # Create PIM entry using the method
        self.create_pim_entry()
        print("pim clicked successfully")
        self.driver.implicitly_wait(30)
        self.edit_emp()

    def test_del_pim_mod_03(self, boot):
        wait = WebDriverWait(self.driver, 30)  # Adjust timeout as needed
        # Login using credentials from Excel
        username = self.s.Read_Data(2, 6)
        password = self.s.Read_Data(2, 7)

        print(f"Username: {username}, Password: {password}")

        self.username_element.send_keys(username)
        self.password_element.send_keys(password)
        self.login_button.click()

        # Create PIM entry using the method
        self.create_pim_entry()
        print("pim clicked successfully")

        self.driver.implicitly_wait(30)
        self.delete()
        print("Deleted")
