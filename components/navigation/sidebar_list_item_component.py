"""Компонент отдельного элемента бокового меню (Page Factory)."""

from typing import Pattern

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    """Инкапсулирует проверку и навигацию по пункту сайдбара."""

    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', f'Иконка пункта {identifier}')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', f'Название пункта {identifier}')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', f'Кнопка пункта {identifier}')

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visible(self, title: str):
        """Проверяет иконку, текст и кнопку пункта."""
        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text(title)
        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        """Переходит по пункту меню и проверяет URL."""
        self.button.click()
        self.check_current_url(expected_url)
