from playwright.sync_api import sync_playwright, expect

from config import settings
from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(AppRoute.REGISTRATION)

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(settings.test_user.email)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(settings.test_user.username)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(settings.test_user.password)

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="browser-state.json")



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state = "browser-state.json")
    page = context.new_page()

    page.goto(AppRoute.COURSES)

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_have_text('Courses')

    courses_subtitle = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_subtitle).to_have_text('There is no results')

    courses_subsubtitle = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_subsubtitle).to_have_text('Results from the load test pipeline will be displayed here')

    icon_file = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_file).to_be_visible()

    page.wait_for_timeout(5000)


