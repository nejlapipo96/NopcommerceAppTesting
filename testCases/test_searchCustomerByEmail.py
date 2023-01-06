import time

import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObject.SearchCustomerPage import SearchCustomer
from pageObject.LoginPage import LoginPage
from pageObject.AddcustomerPage import AddCustomer

class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("*** Test Add Customer ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)  # lp --> Login Page
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Successfuly logged in ***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomerButton()
        self.addcust.clickCustomersItem()

        self.logger.info("*** Starting to search customers by email ***")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setEmail("brenda_lindgren@nopCommerce.com")
        self.searchcust.clickSearchButton()
        time.sleep(5)
        status = self.searchcust.searchCustomerByEmail("brenda_lindgren@nopCommerce.com")
        assert True == status

        self.logger.info("*** Test Search Customer By Email Has Finished ***")

        self.driver.close()

