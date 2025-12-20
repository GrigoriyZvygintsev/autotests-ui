"""Компонент навигационного бара."""
import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):
    """Проверяет заголовок приложения и приветствие пользователя."""

    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page, 'navigation-navbar-app-title-text', 'App')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Welcome')

    @allure.step('Check visible for user: "{username}"')
    def check_visible(self, username: str):
        """Убеждается, что приветствие соответствует переданному пользователю."""
        self.app_title.check_visible()
        self.app_title.check_have_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {username}!')
