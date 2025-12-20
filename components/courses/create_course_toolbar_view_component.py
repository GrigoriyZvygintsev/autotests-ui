"""Компонент тулбара создания курса."""
import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    """Содержит заголовок и кнопку создания курса."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.title = Text(page, 'create-course-toolbar-title-text', 'Toolbar title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Create course button')

    @allure.step('Check visible button, title, status of button create course: "{is_create_course_disabled}"')
    def check_visible(self, is_create_course_disabled: bool = True):
        """Проверяет отображение заголовка и состояние кнопки."""
        self.title.check_visible()
        self.title.check_have_text('Create course')

        self.create_course_button.check_visible()
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

    def click_create_course_button(self):
        """Нажимает кнопку Create course."""
        self.create_course_button.click()
