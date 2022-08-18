from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver. chrome. options import Options
from selenium.webdriver.support.select import Select
import homepage

class MyAccount:
  def __init__(self, driver) -> None:
   """
    function creates MyAccount class
    :param driver: the driver of the MyAccount Page
   """
   self._driver = driver

  locator_dict = {'account': (By.CLASS_NAME, "account"), "span": (By.TAG_NAME, "span"),
                  'alert':(By.CLASS_NAME, "alert"),'p':(By.TAG_NAME, "p")
                ,'search': (By.NAME, "search_query"),'click_search': (By.NAME, "submit_search")}
  def find_user(self):
      """
        function finds user name after login
        :return: user name
      """
      account = self._driver.find_element(*self.locator_dict['account'])
      name = account.find_element(*self.locator_dict['span']).text
      return name

  def check_alert(self):
      alert = self._driver.find_element(*self.locator_dict['alert'])
      p = alert.find_element(*self.locator_dict['p'])
      return p.text



  def search(self, keys:str):
      """
      function searches keys on website
      :param keys: str
      """
      self._driver.find_element(*self.locator_dict['search']).send_keys(keys)
      self._driver.find_element(*self.locator_dict['click_search']).click()
      driver = homepage.HomePage(self._driver)
      return driver