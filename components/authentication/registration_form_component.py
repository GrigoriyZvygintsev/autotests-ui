"""Компонент формы регистрации."""

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    """Содержит поля email, username и пароль формы регистрации."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = Input(page, 'registration-form-email-input', 'Email')
        self.username_input = Input(page, 'registration-form-username-input', 'Username')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')

    def fill(self, email: str, username: str, password: str):
        """Заполняет поля регистрации указанными значениями."""
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    def check_visible(self, email: str, username: str, password: str):
        """Проверяет доступность полей и корректность введенных данных."""
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.username_input.check_visible()
        self.username_input.check_have_value(username)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)
