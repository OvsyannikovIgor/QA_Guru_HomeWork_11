import os

from selene import browser, have

# F_NAME = '#firstName'
# L_NAME = '#lastName'
# EMAIL = '#userEmail'
# GENDER_1 = '#gender-radio-1'
# GENDER_2 = '#gender-radio-2'
# GENDER_3 = '#gender-radio-3'
# MOBILE = '#userNumber'
# BIRTH = '#dateOfBirthInput'
# MONTH_BIRTH = 'option:nth-child(7)'
# YEAR_BIRTH = 'option:nth-child(94)'
# DAY_BIRTH = 'div.react-datepicker__day--018'
# SUBJECTS = '#subjectsInput'
# HOBBIES_1 = '[for="hobbies-checkbox-1"]'
# HOBBIES_2 = '[for="hobbies-checkbox-2"]'
# HOBBIES_3 = '[for="hobbies-checkbox-2"]'
# PICTURE = '#uploadPicture'
# C_ADDRESS = '#currentAddress'
# STATE = '#react-select-3-input'
# CITY = '#react-select-4-input'
# SUBMIT = '#submit'
# BODY = ' table > tbody > tr:nth-child(1) > td:nth-child(2)'


def test_fill_form():
    browser.open('/')
    browser.element('#firstName').type('Мистер')
    browser.element('#lastName').type('Твистер')
    browser.element('#userEmail').type('glavniy@ministr.ru')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').type('79250022225')

    browser.element('#dateOfBirthInput').click()
    browser.element('option:nth-child(7)').click()
    browser.element('option:nth-child(94)').click()
    browser.element('div.react-datepicker__day--018').click()

    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('#currentAddress').type('Petrovka 38')
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Merrut').press_enter()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/picture.png'))
    browser.element('#submit').press_enter()

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