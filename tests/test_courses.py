import pytest
from playwright.sync_api import expect


@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_have_text('Courses')

    courses_subtitle = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_subtitle).to_have_text('There is no results')

    courses_subsubtitle = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_subsubtitle).to_have_text('Results from the load test pipeline will be displayed here')

    icon_file = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_file).to_be_visible()

    page.wait_for_timeout(500)
