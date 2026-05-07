from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_name = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_btn = page.get_by_role("button", name="Login")

    def enter_username(self, username:str):
        self.user_name.fill(username)
    def enter_password(self, password:str):
        self.password.fill(password)
    def click_login(self):
        self.login_btn.click()

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.login()