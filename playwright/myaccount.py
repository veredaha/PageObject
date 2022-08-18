import time

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from playwright.sync_api import Page
import homepage

class MyAccount:
  """
  function creates MyAccount class
  :param driver: the driver of the MyAccount Page
  """
  def __init__(self, driver) -> None:
   self._driver = driver

  locator_dict = {'account': 'class=account', "span": "tag=span",
                  'alert':"class=alert",'p':"tag=p"
                ,'search': 'id=search_query_top','click_search': 'xpath=//*[@id="searchbox"]/button'}

  def find_user(self)->str:
      """
      function finds user name after login
      :return: user name
      """
      account = self._driver.locator(self.locator_dict['account'])
      name = account.locator(self.locator_dict['p']).text()
      return name



  def search(self, keys:str):
      """
      "function searches keys on website
      :param keys: str
      """
      time.sleep(0.5)
      self._driver.locator(self.locator_dict['search']).fill(keys)
      self._driver.locator(self.locator_dict['click_search']).click()
      driver = homepage.HomePage(self._driver)
      return driver