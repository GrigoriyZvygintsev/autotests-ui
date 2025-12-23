"""Базовые инструменты для компонент Page Object."""
import allure

from playwright.sync_api import Page
from typing import Pattern
from tools.logger import get_logger


logger = get_logger("BASE_COMPONENT")


class BaseComponent:
    """Сохраняет экземпляр Page и предоставляет общие проверки."""

    def __init__(self, page: Page):
        """Принимает Playwright Page и хранит его для наследников."""
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        """Сравнивает текущий URL страницы с переданным шаблоном."""
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            self.page.wait_for_url(expected_url)
