import os
import resource

from selene import have, command
from selene.support.shared import browser


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def check_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_phone(self, value):
        browser.element('#userNumber').type(value)

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

    def check_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def upload_photo(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'../{value}'))

    def fill_currentAddress(self, value):
        browser.element('#currentAddress').type(value)
    def fill_state(self, value):
        browser.element('#state #react-select-3-input').type(value).press_enter()

    def select_city(self, value):
        browser.element('#city #react-select-4-input').type(value).press_enter()

    def submit(self):
        browser.element('#submit').perform(command.js.click)

    def should_registered_user_with(self, full_name, email, *tbd):
        # todo: refactor to reuse parameters
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                'Male',
                '1234567891',
                '11 May,1999',
                'Computer Science',
                'Reading',
                'test.jpg',
                'Bronnya Street 14',
                'NCR Delhi',
            )
        )
        return self
