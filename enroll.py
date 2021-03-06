# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://portalsp.acs.ncsu.edu/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get(
            self.base_url + "/shibboleth-ds/?entityID=https%3A%2F%2Fportalsp.acs.ncsu.edu%2Fsp%2Fshibboleth&return=https%3A%2F%2Fportalsp.acs.ncsu.edu%2FShibboleth.sso%2FLogin%3FSAMLDS%3D1%26target%3Dss%253Amem%253Abf2250a2f15cb4f69f9b1553bb986eeaa2feb5cad02051e72e12fdf3b5fc7b6c")
        driver.find_element_by_css_selector("img[alt=\"NCSU Faculty/Staff/Students\"]").click()
        driver.find_element_by_id("j_username").clear()
        driver.find_element_by_id("j_username").send_keys("cwang25")
        driver.find_element_by_id("j_password").clear()
        driver.find_element_by_id("j_password").send_keys("")
        driver.find_element_by_id("formSubmit").click()

        time.sleep(5)

        driver.get("https://cs9prd.acs.ncsu.edu/psc/CS9PRD/EMPLOYEE/NCSIS/s/WEBLIB_JQUERYUI.ISCRIPT1.FieldFormula.IScript_Enrollment_Wizard")
        #time.sleep(10)
        driver.find_element_by_id("tabs-2-tab").click()
        #time.sleep(4)
        driver.find_element_by_id("enrollButton").click()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException, e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
