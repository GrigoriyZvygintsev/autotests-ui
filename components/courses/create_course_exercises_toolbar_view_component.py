"""Компонент тулбара блока упражнений при создании курса."""

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    """Позволяет проверять панель и нажимать «Create exercise»."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Toolbar title')
        self.create_exercise_button = Button(
            page, 'create-course-exercises-box-toolbar-create-exercise-button', 'Create exercise button'
        )

    def check_visible(self):
        """Убеждается, что заголовок и кнопка отображаются."""
        self.title.check_visible()
        self.title.check_have_text('Exercises')
        self.create_exercise_button.check_visible()

    def click_create_exercise_button(self):
        """Нажимает кнопку добавления упражнения."""
        self.create_exercise_button.click()
