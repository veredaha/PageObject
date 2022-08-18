import pytest
from homepage import HomePage
import logging
from loginpage import LoginPage
from playwright.sync_api import sync_playwright
import asyncio
from myaccount import MyAccount

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


@pytest.fixture()
def open(url='http://automationpractice.com/index.php')->HomePage:
    """opens the clothing store site
    :param url -> str
    :return HomePage
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://automationpractice.com/index.php")
        yield page
        page.close()


def test_correct_details(open)->None:
    """test for correct details"""
    mylogger.info("test for correct details")
    page = HomePage(open)
    login_page = page.clickSignIn()
    my_account = login_page.login('vered@gmail.com','123456')
    assert my_account.title() == 'My account - My Store'

def test_empty_email(open)->None:
    """test for empty email"""
    mylogger.info("test for empty email")
    page = HomePage(open)
    login_page = page.clickSignIn()
    my_account = login_page.login('', '123456')
    assert  my_account.title() == 'Login - My Store'

def test_empty_passwd(open)->None:
    """test for empty passwoed"""
    mylogger.info("test for empty passwoed")
    page = HomePage(open)
    login_page = page.clickSignIn()
    my_account = login_page.login('vered@gmail.com', '')
    assert my_account.title() == 'Login - My Store'

def test_empty_fildes(open)->None:
    """test for empty fields"""
    mylogger.info("test for empty fields")
    page = HomePage(open)
    login_page = page.clickSignIn()
    my_account = login_page.login('', '')
    assert my_account.title() == 'Login - My Store'

def test_worng_passwd(open)->None:
    """test for wrong password"""
    mylogger.info("test for wrong password")
    page = HomePage(open)
    login_page = page.clickSignIn()
    my_account = login_page.login('vered@gmail.com', '123')
    assert my_account.title() == 'Login - My Store'

def test_worng_email(open)->None:
    """test for wrong email"""
    mylogger.info("test for wrong email")
    page = HomePage(open)
    login_page = page.clickSignIn()
    my_account = login_page.login('vere@gmail.com', '123456')
    assert my_account.title() == 'Login - My Store'


def test_forgat_passwd(open)->None:
    """test for forgat password"""
    mylogger.info("test for forget password")
    page = HomePage(open)
    login_page = page.clickSignIn()
    forget_pass = login_page.click_forgat_passwd()
    assert forget_pass == 'Forgot your password - My Store'

def test_find_dress(open)->None:
    """test to buy cheapest dress"""
    mylogger.info("test to buy cheapest dress")
    page = HomePage(open)
    login_page = page.clickSignIn()
    my = login_page.login('vered@gmail.com', '123456')
    my_account = MyAccount(my)
    home_page = my_account.search('summer')
    find_dress = home_page.find_cheapest_dress()
    add_to_cart = find_dress.add_to_cart()
    buy = add_to_cart.buy_dress()
    assert buy == "Order confirmation - My Store"