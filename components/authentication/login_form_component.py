"""Компонент формы авторизации."""

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class LoginFormComponent(BaseComponent):
    """Инкапсулирует работу с полями email/пароля на странице входа."""

    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')

    def fill(self, email: str, password: str):
        """Заполняет оба поля формы авторизации."""
        self.email_input.fill(email)
        self.password_input.fill(password)

    def check_visible(self, email: str, password: str):
        """Проверяет отображение формы и введенных значений."""
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)

        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)


