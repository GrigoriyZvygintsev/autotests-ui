"""Компонент тулбара списка курсов."""

import re
import allure

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CoursesListToolbarViewComponent(BaseComponent):
    """Отвечает за заголовок списка и кнопку создания курса."""

    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'courses-list-toolbar-title-text', 'Toolbar title text')
        self.create_course_button = Button(page, 'courses-list-toolbar-create-course-button', 'Create Course Button')

    @allure.step('Check visible Toolbar')
    def check_visible(self):
        """Убеждается, что тулбар отображается корректно."""
        self.title.check_visible()
        self.title.check_have_text('Courses')

        self.create_course_button.check_visible()

    @allure.step('Click create course exercise button')
    def click_create_course_button(self):
        """Нажимает кнопку и проверяет переход на создание курса."""
        self.create_course_button.click()
        self.check_current_url(re.compile(".*/#/courses/create"))


