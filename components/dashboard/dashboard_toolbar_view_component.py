"""Компонент тулбара дашборда."""

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class DashboardToolbarViewComponent(BaseComponent):
    """Следит за отображением заголовка Dashboard."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_visible(self):
        """Проверяет, что заголовок дашборда виден и корректен."""
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Dashboard')
