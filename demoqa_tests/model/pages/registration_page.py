import os
from selene import have, command
from selene.support.shared import browser
from demoqa_tests.data.users import User


class RegistrationPage:
    # def __init__(self):
    #     self.first_name = browser.element('#firstName')
    #     self.last_name = browser.element('#lastName')
    #     self.state = browser.element('#state')

    # def open(self):
    #     browser.open('/automation-practice-form')
    #     browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
    #         have.size_greater_than_or_equal(3)
    #     )
    #     browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
    #     return self
    #
    # def fill_first_name(self, value):
    #     self.first_name.type(value)
    #     return self
    #
    # def fill_last_name(self, value):
    #     self.last_name.type(value)
    #     return self
    #
    # def fill_date_of_birth(self, year, month, day):
    #     browser.element('#dateOfBirthInput').click()
    #     browser.element('.react-datepicker__month-select').type(month)
    #     browser.element('.react-datepicker__year-select').type(year)
    #     browser.element(
    #         f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
    #     ).click()
    #     return self
    #
    # def fill_state(self, name):
    #     self.state.perform(command.js.scroll_into_view)
    #     self.state.click()
    #     browser.all('[id^=react-select][id*=option]').element_by(
    #         have.exact_text(name)
    #     ).click()
    #     return self
    #
    # def should_registered_user_with(self, full_name, email, gender):
    #     # todo: refactor to reuse parameters
    #     browser.element('.table').all('td').even.should(
    #         have.exact_texts(
    #             full_name,
    #             email,
    #             gender,
    #             '1234567891',
    #             '11 May,1999',
    #             'Computer Science',
    #             'Reading',
    #             'foto.jpg',
    #             'Moscowskaya Street 18',
    #             'NCR Delhi',
    #         )
    #     )
    #     return self
    def open(self):
        browser.open('/automation-practice-form')

    def registration(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('[id="userEmail"]').send_keys(user.email)
        browser.element('[name="gender"][value=Male]').double_click()
        browser.element('[id="userNumber"]').send_keys(user.number)
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__year-select').type(user.birthday)
        browser.element('.react-datepicker__month-select').type(user.birthday.strftime('%B'))
        browser.element('.react-datepicker__day--011').click()
        browser.element('#subjectsInput').type(user.subjects).press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text(user.hobbies)).click()
        # переписать
        browser.element('#uploadPicture').send_keys(os.getcwd() + f"/{user.picture}")

        browser.element('#currentAddress').type(user.address)

        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.city)
        ).click()

        browser.element('#submit').execute_script('element.click()')

    def should_have_registered(self, user: User):
        full_name = f'{user.first_name} {user.last_name}'
        birthday = f'{user.birthday.strftime("%d")} {user.birthday.strftime("%B")},{user.birthday.year}'
        state_and_city = f'{user.state} {user.city}'
        subject = ''.join([subject for subject in user.subjects])
        browser.all('tbody tr').should(have.exact_texts(
            f'Student Name {full_name}', f'Student Email {user.email}',
            f'Gender {user.gender}',
            f'Mobile {user.number}',
            f'Date of Birth {birthday}',
            f'Subjects {subject}',
            f'Hobbies {user.hobbies}',
            f'Picture {user.picture}',
            f'Address {user.address}',
            f'State and City {state_and_city}'))

