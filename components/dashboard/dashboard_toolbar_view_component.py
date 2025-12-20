"""Компонент тулбара дашборда (Page Factory)."""
import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    """Следит за отображением заголовка Dashboard."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.title = Text(page, 'dashboard-toolbar-title-text', 'Заголовок Dashboard')

    @allure.step('Check visible Dashboard title')
    def check_visible(self):
        """Проверяет, что заголовок дашборда виден и корректен."""
        self.title.check_visible()
        self.title.check_have_text('Dashboard')
