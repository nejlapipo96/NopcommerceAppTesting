import string

import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObject.LoginPage import LoginPage
from pageObject.AddcustomerPage import AddCustomer
import random
from selenium.webdriver.common.by import By

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*** Test Add Customer ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)              # lp --> Login Page
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Successfuly logged in ***")

        self.logger.info("*** Starting Add Customer Test ***")
        self.addcust = AddCustomer(self.driver)       # addcust --> Add Customer
        self.addcust.clickCustomerButton()
        self.addcust.clickCustomersItem()
        self.addcust.clickAddNewButton()

        self.logger.info("*** Providing Customer Info ***")

        email = random_generator() + "@gmail.com"
        self.addcust.addEmail(email)
        self.addcust.addPassword("test123")
        self.addcust.addFirstName("Admin")
        self.addcust.addLastName("Brown")
        self.addcust.setGender("Female")
        self.addcust.setDateOfBirth("3/10/2000")
        self.addcust.setCompanyName("Tech123")
        self.addcust.addCustomerRoles("Forum Moderator")
        self.addcust.setVendor("Vendor 1")
        self.addcust.setAdminComment("This is for testing...")
        self.addcust.clickSave()

        self.logger.info("*** Saving New Customer ***")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("*** Passed ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\ + addCustomer.png")
            self.logger.error("*** Not Passed ***")
            assert True == False

        self.driver.close()



def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
