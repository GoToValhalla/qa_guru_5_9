import time

from selene import have

from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

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

    time.sleep(10)

    registration_page.assert_user_data().should(have.texts('Student Name', 'Ivan YA',
                                                           'Student Email', 'name@example.com',
                                                           'Gender', 'Male',
                                                           'Mobile', '1234567891',
                                                           'Date of Birth', '11 May,1999',
                                                           'Subjects Computer', 'Science',
                                                           'Hobbies', 'Reading',
                                                           'Picture', 'test.jpg',
                                                           'Address Russia', 'Bronnya Street 14',
                                                           'State and City', 'NCR Delhi'))

    # registration_page.close_submission()
