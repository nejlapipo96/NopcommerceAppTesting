from selenium.webdriver.common.by import By


class SearchCustomer:

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, "SearchEmail").send_keys(email)

    def setFirstName(self,firstname):
        self.driver.find_element(By.ID, "SearchFirstName").send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, "SearchLastName").send_keys(lastname)

    def clickSearchButton(self):
        self.driver.find_element(By.ID, "search-customers").click()

    def getNoOfRows(self):
        rows = self.driver.find_elements(By.XPATH, "//table[@id='customers-grid']//tbody/tr")
        return len(rows)

    def getNoOfColumns(self):
        columns = self.driver.find_elements(By.XPATH, "//table[@id='customers-grid']//tbody/tr/td")
        return len(columns)

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']")
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']")
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag










