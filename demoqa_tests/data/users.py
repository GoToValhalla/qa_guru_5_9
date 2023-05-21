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
    computer_science = 'Computer Science'
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
    genders: List[Gender]
    phone_number: int
    date_of_birth: date
    subjects: List[Subject]
    hobbies: List[Hobby]
    upload_filename: str
    current_address: str
    state: str
    city: str


admin = User(full_name='admina adminovych', email='super+admin@gmail.com')
guest = User('harry', 'potter@hg.com')
