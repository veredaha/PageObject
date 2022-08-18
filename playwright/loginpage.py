import time
import pytest
from selenium import webdriver
from playwright.sync_api import sync_playwright
from myaccount import MyAccount



class LoginPage:
  def __init__(self, driver) -> None:
   """
   function creates LoginPage class
   :param driver: the driver of the Login Page
   """
   self._driver = driver

  locator_dict = {'email':'id=email','passwd':'id=passwd',
                 'click_login':'id=SubmitLogin','account':"class=account",
                  'tag_span':"tag=span",'forgat_pass':'text="Forgot your password?"'}

  def login(self,user:str,passwd:str):
   """
   function logs into the account
   :param user: str
   :param passwd: str
   """
   self._driver.locator(self.locator_dict['email']).fill(user)
   self._driver.locator(self.locator_dict['passwd']).fill(passwd)
   self._driver.locator(self.locator_dict['click_login']).click()
   time.sleep(0.3)
   return self._driver


  def click_forgat_passwd(self):
      """
      function clicks on forgat password
      """
      self._driver.locator(self.locator_dict['forgat_pass']).click()
      time.sleep(0.2)
      return self._driver.title()
