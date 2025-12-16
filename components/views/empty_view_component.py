"""Компонент отображения пустого состояния (Page Factory)."""

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    """Проверяет иконку, заголовок и описание пустого блока."""

    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-empty-view-icon', 'Иконка пустого состояния')
        self.title = Text(page, f'{identifier}-empty-view-title-text', 'Заголовок пустого состояния')
        self.description = Text(page, f'{identifier}-empty-view-description-text', 'Описание пустого состояния')

    def check_visible(self, title: str, description: str):
        """Убеждается, что пустое состояние отображает нужный текст."""
        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text(title)
        self.description.check_visible()
        self.description.check_have_text(description)
