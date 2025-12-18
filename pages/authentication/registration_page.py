"""Page Object страницы регистрации."""
from typing import re

from playwright.sync_api import Page

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """Содержит форму регистрации и действия со ссылками."""

    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')
        self.login_button = Link(page, 'registration-page-login-link', 'Login')

    def click_registration_button(self):
        """Нажимает кнопку регистрации."""
        self.registration_button.click()

    def click_login_button(self):
        """Возвращает пользователя к странице входа."""
        self.login_button.click()
        self.check_current_url(re.compile(".*/#/auth/login"))
