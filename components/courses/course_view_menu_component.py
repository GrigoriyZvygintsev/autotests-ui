"""Компонент меню карточки курса."""

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CourseViewMenuComponent(BaseComponent):
    """Содержит действия меню редактирования/удаления курса."""

    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = page.get_by_test_id('course-view-menu-button')
        self.edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        self.delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')

    def click_edit(self, index: int):
        """Открывает меню нужной карточки и нажимает пункт Edit."""
        self.menu_button.nth(index).click()

        expect(self.edit_menu_item.nth(index)).to_be_visible()
        self.edit_menu_item.nth(index).click()

    def click_delete(self, index: int):
        """Открывает меню нужной карточки и нажимает пункт Delete."""
        self.menu_button.nth(index).click()

        expect(self.delete_menu_item.nth(index)).to_be_visible()
        self.delete_menu_item.nth(index).click()
