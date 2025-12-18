import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.courses
class TestCourses:
    def test_create_course (self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="",
            description="",
            estimated_time="",
            max_score="0",
            min_score="0",
        )

        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image(file='./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10",
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0,
                                                    title = "Playwright",
                                                    estimated_time = "2 weeks",
                                                    max_score = "100",
                                                    min_score = "10")

    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()

    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        initial_course = {
            'title': 'Story o Kulibyaki',
            'estimated_time': '2 weeks',
            'description': 'Story_K',
            'max_score': '100',
            'min_score': '10',
        }

        updated_course = {
            'title': 'Story o Kulibyaki 2',
            'estimated_time': '3 weeks',
            'description': 'Story_K_2',
            'max_score': '150',
            'min_score': '20',
        }

        create_course_page.create_course_form.fill(**initial_course)
        create_course_page.image_upload_widget.upload_preview_image(file='./testdata/files/image.png')
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page.course_view.check_visible(
            index=0,
            title=initial_course['title'],
            estimated_time=initial_course['estimated_time'],
            max_score=initial_course['max_score'],
            min_score=initial_course['min_score'],
        )

        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.check_visible(**initial_course)

        create_course_page.create_course_form.fill(**updated_course)
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page.course_view.check_visible(
            index=0,
            title=updated_course['title'],
            estimated_time=updated_course['estimated_time'],
            max_score=updated_course['max_score'],
            min_score=updated_course['min_score'],
        )

        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.check_visible(**updated_course)
