"""Базовый класс для Page Object."""

from playwright.sync_api import Page


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
