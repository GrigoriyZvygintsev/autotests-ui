"""Page Object страницы авторизации."""

from playwright.sync_api import Page, expect

from components.authentication.login_form_component import LoginFormComponent
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Содержит компонент формы логина и ключевые действия страницы."""

    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    def click_login_button(self):
        """Нажимает кнопку входа."""
        self.login_button.click()

    def click_registration_link(self):
        """Переходит по ссылке регистрации."""
        self.registration_link.click()

    def check_visible_wrong_email_or_password_alert(self):
        """Проверяет отображение алерта об ошибке авторизации."""
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")
