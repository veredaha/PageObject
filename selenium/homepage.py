import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium. webdriver. chrome. options import Options
from selenium.webdriver.support.select import Select
from loginpage import LoginPage
from myaccount import  MyAccount
from buying import Buying


class HomePage:
 def __init__(self, driver) -> None:
    """
    function creates HomePage class
    :param driver: the driver of the HomePage
    """
    self._driver = driver



 locator_dict = { "sign_in" : (By.LINK_TEXT, 'Sign in')
     ,'search': (By.NAME, "search_query"),'click_search': (By.NAME, "submit_search"),
      "product_list":(By.CLASS_NAME, "product_list"),'product_container':(By.CLASS_NAME, "product-container"),
                  'right_block':(By.CLASS_NAME, "right-block"),'content_price':(By.CLASS_NAME, "content_price"),
                  'price':(By.TAG_NAME, "span"),'button':(By.CLASS_NAME, "button-container"),
                  'a':(By.TAG_NAME, "a"),'layer_cart':(By.ID, "layer_cart")}


 def clickSignIn(self):
    """
     function clicks on the sign in icon
     :return: LoginPage(self._driver)
    """
    self._driver.find_element(*self.locator_dict['sign_in']).click()
    return LoginPage(self._driver)

 def find_cheapest_dress(self):
     """
          function finds the cheapest dress and adds it to thr cart
          :return: Buying(self._driver)
     """
     product_list = self._driver.find_element(*self.locator_dict['product_list'])
     product_containers = product_list.find_elements(*self.locator_dict['product_container'])
     price_list = {}
     for product_container in product_containers:
         right_block = product_container.find_element(*self.locator_dict['right_block'])
         content_price = right_block.find_element(*self.locator_dict['content_price'])
         price = content_price.find_element(*self.locator_dict['price']).text
         price_list[price.strip()] = right_block
     cheapest = min(price_list.keys())
     price_list[cheapest].click()
     time.sleep(4)
     button = price_list[cheapest].find_element(*self.locator_dict['button'])
     time.sleep(5)
     button.find_element(*self.locator_dict['a']).click()
     time.sleep(3)
     return HomePage(self._driver)

 def add_to_cart(self):
     add_to_cart = self._driver.find_element(*self.locator_dict['layer_cart'])
     time.sleep(7)
     add_to_cart.find_element(*self.locator_dict['a']).click()
     return Buying(self._driver)
