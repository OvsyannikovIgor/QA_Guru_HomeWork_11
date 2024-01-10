import os

from selene import browser, have

F_NAME = '#firstName'
L_NAME = '#lastName'
EMAIL = '#userEmail'
GENDER_1 = '#gender-radio-1'
GENDER_2 = '#gender-radio-2'
GENDER_3 = '#gender-radio-3'
MOBILE = '#userNumber'
BIRTH = '#dateOfBirthInput'
MONTH_BIRTH = 'option:nth-child(7)'
YEAR_BIRTH = 'option:nth-child(94)'
DAY_BIRTH = 'div.react-datepicker__day--018'
SUBJECTS = '#subjectsInput'
HOBBIES_1 = '[for="hobbies-checkbox-1"]'
HOBBIES_2 = '[for="hobbies-checkbox-2"]'
HOBBIES_3 = '[for="hobbies-checkbox-2"]'
PICTURE = '#uploadPicture'
C_ADDRESS = '#currentAddress'
STATE = '#react-select-3-input'
CITY = '#react-select-4-input'
SUBMIT = '#submit'
BODY = ' table > tbody > tr:nth-child(1) > td:nth-child(2)'


class RegistrationPage():
    def __init__(self):
        pass

    def open_registration_page(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element(F_NAME).type(value)
        return self

    def fill_last_name(self, value):
        browser.element(L_NAME).type(value)
        return self

    def choice_gender(self):
        browser.element(GENDER_2).double_click()
        return self

    def fill_email(self, value):
        browser.element(EMAIL).type(value)
        return self

    def fill_user_number(self, value):
        browser.element(MOBILE).type(value)
        return self

    def fill_date_of_birth(self):
        browser.element(BIRTH).click()
        browser.element(MONTH_BIRTH).click()
        browser.element(YEAR_BIRTH).click()
        browser.element(DAY_BIRTH).click()
        return self

    def fill_subjects(self, value):
        browser.element(SUBJECTS).type(value).press_enter()
        return self

    def fill_current_address(self, value):
        browser.element(C_ADDRESS).type(value)
        return self

    def choice_hobies(self):
        browser.element(HOBBIES_2).click()
        return self

    def fill_state(self, state, city):
        browser.element(STATE).type(state).press_enter()
        browser.element(CITY).type(city).press_enter()
        return self

    def upload_picture(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/picture.png'))
        return self

    def should_registered_user_with(self):
        browser.all(' table > tbody > tr').all('td:nth-child(2)').should(
            have.exact_texts('Мистер Твистер',
                             'glavniy@ministr.ru',
                             'Female', '7925002222',
                             '18 July,1993',
                             'Maths',
                             'Reading',
                             'picture.png',
                             'Petrovka 38',
                             'Uttar Pradesh Merrut')
        )

    def submit_btn(self):
        browser.element(SUBMIT).press_enter()
        return self
