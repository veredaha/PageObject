class Buying():
 def __init__(self, driver) -> None:
    """
    function creates Buying class
    :param driver: the driver of the buying page
    """
    self._driver = driver

 locator_dict = {'center_checkout':"#center_column >> text=Proceed to checkout",
                 'text_checkout':"button:has-text('Proceed to checkout')",
                 'cgv':'//*[@id="cgv"]', 'bank_wire':'text=Pay by bank wire',
                 'confirm':'text=I confirm my order'}
 def buy_dress(self):
     """
     function buys the dress
     """
     self._driver.locator(self.locator_dict['center_checkout']).click()
     self._driver.wait_for_timeout(3000)
     self._driver.locator(self.locator_dict['center_checkout']).click()
     self._driver.wait_for_timeout(3000)
     self._driver.locator(self.locator_dict['text_checkout']).click()
     self._driver.wait_for_timeout(20000)
     self._driver.locator(self.locator_dict['cgv']).click()
     self._driver.wait_for_timeout(5000)
     self._driver.locator(self.locator_dict['text_checkout']).click()
     self._driver.locator(self.locator_dict['bank_wire']).last.click()
     self._driver.locator(self.locator_dict['confirm']).last.click()
     return self._driver.title()