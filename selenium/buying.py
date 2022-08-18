import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Buying():
 def __init__(self, driver) -> None:
    """
    function creates Buying class
    :param driver: the driver of the buying page
    """
    self._driver = driver

 locator_dict = {'center':(By.XPATH, "//*[@id='center_column']/p[2]/a[1]"),
                 'center_column':(By.ID, "center_column"),
                 'button':(By.TAG_NAME, "button"),
                 'cgv':(By.ID, "cgv"),'form':(By.ID, "form"),
                 'bank_wire':(By.CLASS_NAME, "bankwire"),
                 'cart_n':(By.ID, "cart_navigation"),
                 'confirm':(By.CLASS_NAME, "box")}
 def buy_dress(self):
     """
     function buys the dress
     """
     time.sleep(5)
     self._driver.find_element(*self.locator_dict['center']).click()
     time.sleep(4)
     center = self._driver.find_element(*self.locator_dict['center_column'])
     center.find_element(*self.locator_dict['button']).click()
     time.sleep(4)
     self._driver.find_element(*self.locator_dict['cgv']).click()
     time.sleep(10)
     center = self._driver.find_element(*self.locator_dict['form'])
     center.find_element(*self.locator_dict['button']).click()
     time.sleep(10)
     self._driver.find_element(*self.locator_dict['bank_wire']).click()
     time.sleep(10)
     cart_navigation = self._driver.find_element(*self.locator_dict['cart_n'])
     cart_navigation.find_element(*self.locator_dict['button']).click()
     order = self._driver.find_element(*self.locator_dict['confirm']).text
     return order