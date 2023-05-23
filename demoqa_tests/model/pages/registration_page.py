import os

from selene import have, command
from selene.support.shared import browser


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def check_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_phone(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def check_hobbies(self, *args):
        for hobby in args:
            browser.all('.custom-checkbox').element_by(have.exact_text(hobby)).click()
            return self

    def upload_photo(self, value):
        browser.element('#uploadPicture').send_keys(os.getcwd() + f'/resources/{value}')
        return self

    def fill_currentAddress(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_state(self, value):
        browser.element('#state #react-select-3-input').type(value).press_enter()
        return self

    def select_city(self, value):
        browser.element('#city #react-select-4-input').type(value).press_enter()
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def close_submission(self):
        browser.element('#closeLargeModal').click()
        return self

    def assert_user_data(self):
        return browser.element('.table-responsive').all('td')
