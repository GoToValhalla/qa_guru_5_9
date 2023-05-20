from selene.support.shared import browser
from selene import have
from selene import command
from demoqa_tests import resource
from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('YA')
    registration_page.fill_email('name@example.com')
    registration_page.check_gender('Male')
    registration_page.fill_phone('1234567891')
    registration_page.fill_date_of_birth('1999', 'May', '11')
    registration_page.fill_subjects('Computer Science')
    registration_page.check_hobbies('Reading')
    registration_page.upload_photo('test.png')
    registration_page.fill_currentAddress('Bronnya Street 14')
    registration_page.fill_state('NCR')
    registration_page.select_city('Delhi')
    registration_page.submit()

    # THEN
    registration_page.should_registered_user_with(
        'Ivan YA',
        'name@example.com',
        'Male',
        '1234567891',
        '11 May,1999',
        'Computer Science',
        'Reading',
        'test.jpg',
        'Bronnya Street 14',
        'NCR Delhi',
    )
    '''
    # example of implementing assertion-free pageobjects
    registration_page.registered_user_data.should(
        have.exact_texts(
            'Ivan YA',
            'name@example.com',
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
    '''
