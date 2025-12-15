"""Базовые инструменты для компонент Page Object."""

from playwright.sync_api import Page, expect
from typing import Pattern


class BaseComponent:
    """Сохраняет экземпляр Page и предоставляет общие проверки."""

    def __init__(self, page: Page):
        """Принимает Playwright Page и хранит его для наследников."""
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        """Сравнивает текущий URL страницы с переданным шаблоном."""
        expect(self.page).to_have_url(expected_url)
