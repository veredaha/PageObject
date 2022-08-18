import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium. webdriver. chrome. options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from myaccount import MyAccount



class LoginPage:
  def __init__(self, driver) -> None:
   """
         function creates LoginPage class
         :param driver: the driver of the Login Page
    """
   self._driver = driver

  locator_dict = {'email':(By.NAME, "email"),'passwd':(By.NAME, "passwd"),
                 'click_login':(By.NAME, "SubmitLogin"),'account':(By.CLASS_NAME, "account"),
                  'tag_span':(By.TAG_NAME, "span"),'forgat_pass':(By.LINK_TEXT, "Forgot your password?")}

  def login(self,user,passwd):
   """
         function logs into the account
         :param user: str
         :param passwd: str
   """
   self._driver.find_element(*self.locator_dict['email']).send_keys(user)
   self._driver.find_element(*self.locator_dict['passwd']).send_keys(passwd)
   self._driver.implicitly_wait(30)
   self._driver.find_element(*self.locator_dict['click_login']).click()
   return MyAccount(self._driver)




  def click_forgat_passwd(self):
      """
      function clicks on forgot password
       """
      self._driver.find_element(*self.locator_dict['forgat_pass']).click()
      return self._driver.title

