import os
from playwright.sync_api import sync_playwright
from pages.orangehrm_login_page import LoginPage
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def setup_auth():
    #Make folder if not exists
    os.makedirs("auth", exist_ok = True)

    with sync_playwright() as p:

        browser = p.chromium.launch(headless = False)
        context = browser.new_context()

        #New page
        page = context.new_page()
        page.goto(BASE_URL)

        #Login
        login_page = LoginPage(page)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        #wait until login is successful
        page.wait_for_load_state("networkidle")

        #Save storage state into file
        context.storage_state(path = "auth/auth.json")

        print("Auth setup completed successfully")

        browser.close()

if __name__ == '__main__':
    setup_auth()
