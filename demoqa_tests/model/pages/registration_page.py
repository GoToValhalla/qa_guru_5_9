import os
from selene import have, command
from selene.support.shared import browser
from demoqa_tests.data.users import User
from tests import resource


class RegistrationPage:

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
        browser.element('#uploadPicture').send_keys(os.getcwd() + f"/resources/{user.picture}")

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
