"""Компонент боковой панели навигации."""

import re

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    """Управляет пунктами меню Dashboard/Courses/Logout."""

    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, 'logout')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')

    @allure.step("Check visible sidebar")
    def check_visible(self):
        """Проверяет наличие всех пунктов меню."""
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    @allure.step("Click logout on sidebar")
    def click_logout(self):
        """Кликает по Logout и проверяет переход на страницу логина."""
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    @allure.step("Click courses on sidebar")
    def click_courses(self):
        """Кликает по Courses и проверяет редирект."""
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    @allure.step("Click dashboard on sidebar")
    def click_dashboard(self):
        """Кликает по Dashboard и проверяет редирект."""
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))
