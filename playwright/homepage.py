import time
import pytest
from playwright.sync_api import sync_playwright
from loginpage import LoginPage
from myaccount import MyAccount
from buying import Buying


class HomePage():

 def __init__(self, driver) -> None:
    """
     function creates HomePage class
     :param driver: the driver of the homepage
    """
    self._driver = driver



 locator_dict = { "sign_in" : '.login'
     ,'search': "name=search_query",
      'click_search': "name=submit_search",
      "product_list":"class=product_list",
      'product_container':".product-container",
      'right_block':"class=right-block",
      'product_price':".product-price",
      'price':"tag=span",
      'add_to_cart':'.ajax_add_to_cart_button',
      'checkout':"text=Proceed to checkout"}


 def clickSignIn(self)->LoginPage:
    """
     function clicks on the sign in icon
     :return: LoginPage(self._driver)
    """
    self._driver.query_selector(self.locator_dict["sign_in"]).click()
    return LoginPage(self._driver)

 def find_cheapest_dress(self)->Buying:
     """
     function finds the cheapest dress and adds it to thr cart
     :return: Buying(self._driver)
     """
     self._driver.wait_for_timeout(3000)
     product_list = self._driver.query_selector_all(self.locator_dict['product_container'])
     price_list = {}
     for product in product_list:
         price = product.query_selector(self.locator_dict['product_price']).text_content().strip()
         price_list[price] = product
     self._driver.wait_for_timeout(3000)
     cheapest = min(price_list.keys())
     self._driver.wait_for_timeout(3000)
     price_list[cheapest].click()
     price_list[cheapest].query_selector(self.locator_dict['add_to_cart']).click()
     return HomePage(self._driver)

 def add_to_cart(self):
     self._driver.locator(self.locator_dict['checkout']).click()
     return Buying(self._driver)
