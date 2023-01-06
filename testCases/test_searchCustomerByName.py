import time

import pytest
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObject.LoginPage import LoginPage
from pageObject.SearchCustomerPage import SearchCustomer
from pageObject.AddcustomerPage import AddCustomer

class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Successfuly logged in ***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomerButton()
        self.addcust.clickCustomersItem()

        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setFirstName("James")
        self.searchcust.setLastName("Pan")
        self.searchcust.clickSearchButton()
        time.sleep(5)
        status = self.searchcust.searchCustomerByName("James Pan")
        if status == True:
            assert True
        else:
            assert False

        self.logger.info("*** Testing by customer name has finished ***")

        self.driver.close()