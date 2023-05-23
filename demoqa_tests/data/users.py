import dataclasses
from datetime import date
from typing import List


class Gender:
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subject:
    accounting = 'Accounting'
    arts = 'Arts'
    biology = 'Biology'
    english = 'English'
    chemistry = 'Chemistry'
    computer_science = 'Computer Scien'
    commerce = 'Commerce'
    maths = 'Maths'
    physics = 'Physics'
    economics = 'Economics'
    social_studies = 'Social Studies'


class Hobby:

    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    number: str
    birthday: date
    subjects: List[Subject]
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


user = User(
    first_name='Ivan',
    last_name='YA',
    email='name@example.com',
    gender=Gender.male,
    number='1234567891',
    birthday=date(1999, 5, 11),
    subjects=Subject.maths,
    hobbies=Hobby.reading,
    picture='foto.jpg',
    address='Bronnya Street 14',
    state='NCR',
    city='Delhi')

# admin = User(full_name='admina adminovych', email='super+admin@gmail.com')
# guest = User('harry', 'potter@hg.com')
