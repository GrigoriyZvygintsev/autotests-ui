"""Базовый класс для Page Object."""
import allure

from typing import Pattern

from playwright.sync_api import Page, expect

from tools.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    """Хранит ссылку на страницу и общие методы навигации."""

    def __init__(self, page: Page):
        """Принимает экземпляр Page, доступный наследникам."""
        self.page = page

    def visit(self, url: str):
        """Переходит по указанному URL, ожидая загрузку сети."""
        step = f'Opening page "{url}"'
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        """Перезагружает текущую страницу."""
        current_url = self.page.url
        step = f'Reloading page "{current_url}"'
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until='networkidle')

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
