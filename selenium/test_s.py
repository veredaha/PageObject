import pytest
from homepage import HomePage
import logging
from loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver. chrome. options import Options
from selenium.webdriver.support.select import Select
from myaccount import MyAccount

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()
chrome_options = Options()

chrome_driver_path = r"C:\Users\vered\Desktop\chromedriver.exe"

@pytest.fixture()
def open(url='http://automationpractice.com/index.php')->HomePage:
    """opens the clothing store site
    :param url -> str
    :return HomePage
    """
    driver = webdriver.Chrome(chrome_driver_path,chrome_options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    yield HomePage(driver)
    driver.close()


def test_correct_details(open)->None:
    """test for correct details"""
    mylogger.info("test for correct details")
    login_page = open.clickSignIn()
    my_account = login_page.login('vered@gmail.com','123456')
    username = my_account.find_user()
    assert username == 'Vered Aharonov'

def test_empty_email(open)->None:
    """test for empty email"""
    mylogger.info("test for empty email")
    login_page = open.clickSignIn()
    my_account = login_page.login('', '123456')
    alert = my_account.check_alert()
    assert "error" in alert

def test_empty_passwd(open)->None:
    """test for empty passwoed"""
    mylogger.info("test for empty passwoed")
    login_page = open.clickSignIn()
    my_account = login_page.login('vered@gmail.com', '')
    alert = my_account.check_alert()
    assert "error" in alert

def test_empty_fildes(open)->None:
    """test for empty fields"""
    mylogger.info("test for empty fields")
    login_page = open.clickSignIn()
    my_account = login_page.login('', '')
    alert = my_account.check_alert()
    assert "error" in alert

def test_worng_passwd(open)->None:
    """test for wrong password"""
    mylogger.info("test for wrong password")
    login_page = open.clickSignIn()
    my_account = login_page.login('vered@gmail.com', '123')
    alert = my_account.check_alert()
    assert "error" in alert

def test_worng_email(open)->None:
    """test for wrong email"""
    mylogger.info("test for wrong email")
    login_page = open.clickSignIn()
    my_account = login_page.login('vere@gmail.com', '123456')
    alert = my_account.check_alert()
    assert "error" in alert


def test_forgat_passwd(open)->None:
    """test for forgat password"""
    mylogger.info("test for forget password")
    login_page = open.clickSignIn()
    forget_pass = login_page.click_forgat_passwd()
    assert forget_pass == 'Forgot your password - My Store'

def test_find_dress(open)->None:
    """test to buy cheapest dress"""
    mylogger.info("test to buy cheapest dress")
    login_page = open.clickSignIn()
    my_account = login_page.login('vered@gmail.com', '123456')
    home_page = my_account.search('summer')
    home_page_cheapest_dress = home_page.find_cheapest_dress()
    add_to_cart = home_page_cheapest_dress.add_to_cart()
    buy_dress = add_to_cart.buy_dress()
    assert "Your order on My Store is complete." in buy_dress
