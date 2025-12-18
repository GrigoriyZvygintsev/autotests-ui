"""Базовый класс для Page Object."""
from typing import Pattern

from playwright.sync_api import Page, expect


class BasePage:
    """Хранит ссылку на страницу и общие методы навигации."""

    def __init__(self, page: Page):
        """Принимает экземпляр Page, доступный наследникам."""
        self.page = page

    def visit(self, url: str):
        """Переходит по указанному URL, ожидая загрузку сети."""
        self.page.goto(url, wait_until='networkidle')

    def reload(self):
        """Перезагружает текущую страницу."""
        self.page.reload(wait_until='networkidle')

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)
