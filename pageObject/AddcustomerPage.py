import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerButton(self):
        self.driver.find_element(By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]").click()

    def clickCustomersItem(self):
        self.driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]").click()

    def clickAddNewButton(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Add new']").click()

    def addEmail(self, email):
        self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys(email)

    def addPassword(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)

    def addFirstName(self, firstname):
        self.driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys(firstname)

    def addLastName(self, lastname):
        self.driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys(lastname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, "//input[@id='Gender_Male']").click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, "//input[@id='Gender_Female']").click()
        else:
            self.driver.find_element(By.XPATH, "//input[@id='Gender_Female']").click()

    def setDateOfBirth(self, date):
        self.driver.find_element(By.ID, "DateOfBirth").send_keys(date)

    def setCompanyName(self, compname):
        self.driver.find_element(By.XPATH, "//input[@id='Company']").send_keys(compname)

    def addCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, "//div[@class='input-group-append input-group-required']//div[@role='listbox']").click()
        if role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, "//li[normalize-space()='Administrators']")
        elif role == "Registered":
            self.driver.find_element(By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, "//li[@id='5b568720-daea-44de-9be1-eb0c50d7bc53']")
        elif role == "Guests":
            self.listitem = self.driver.find_element(By.XPATH, "//li[normalize-space()='Guests']")
        elif role == "Forum Moderator":
            self.listitem = self.driver.find_element(By.XPATH, "//li[normalize-space()='Forum Moderators']")
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, "//li[contains(text(),'Vendors')]")
        else:
            self.listitem = self.driver.find_element(By.XPATH, "//li[normalize-space()='Guests']")
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setVendor(self, value):
        selectVendor = Select(self.driver.find_element(By.XPATH, "//select[@id='VendorId']"))
        selectVendor.select_by_visible_text(value)

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH, "//textarea[@id='AdminComment']").send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.XPATH, "//button[@name='save']").click()