"""Компонент отображения графиков на дашборде."""

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class ChartViewComponent(BaseComponent):
    """Формирует динамические локаторы для заголовка и графика."""

    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)
        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible(self, title: str):
        """Проверяет, что отображаются заголовок и сам график."""
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)
        expect(self.chart).to_be_visible()
