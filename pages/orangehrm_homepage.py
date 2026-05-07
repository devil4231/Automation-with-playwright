from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.admin = page.get_by_role("link", name="Admin")
        self.dashboard = page.get_by_role("link", name="Dashboard")
        self.client_banner = page.get_by_role("link", name="client brand banner")
        self.employee_text = page.get_by_text("Employee Distribution by Location")

    def click_admin(self):
        self.admin.click()

    def click_dashboard(self):
        self.dashboard.click()

    