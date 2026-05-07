import re
from playwright.sync_api import Page, expect
from pages.orangehrm_login_page import LoginPage
from pages.orangehrm_homepage import HomePage

def test_orangehrm(page):

    login_page = LoginPage(page)
    home_page = HomePage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    
    expect(home_page.client_banner).to_be_visible()
    expect(home_page.employee_text).to_be_visible()
    home_page.click_admin()
    home_page.click_dashboard()