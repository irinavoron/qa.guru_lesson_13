import allure
from selene import have

from demoqa_tests.application import app
from demoqa_tests.data import users


@allure.label('owner', 'irinavoron')
@allure.title('Test registration form')
def test_registration_form():
    allure.dynamic.link('https://demoqa.com')
    user = users.student

    with allure.step('Open registration from'):
        app.left_panel.open_registration_form()

    with allure.step('Fill registration form'):
        app.registration.fill_first_name(user.first_name)
        app.registration.fill_last_name(user.last_name)
        app.registration.fill_email(user.email)
        app.registration.select_gender(user.gender)
        app.registration.fill_phone_number(user.phone_number)
        app.registration.fill_birth_date(user.birth_date.year, user.birth_date.month, user.birth_date.day)
        app.registration.fill_subject(user.subject)
        app.registration.select_hobby(user.hobby)
        app.registration.upload_picture(user.file)
        app.registration.fill_current_address(user.current_address)
        app.registration.select_state(user.state)
        app.registration.select_city(user.city)

    with allure.step('Submit registration form'):
        app.registration.submit_form()

    with allure.step('Check registered data'):
        app.registration.registered_data.should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            user.birth_date.strftime(f'%d %B,%Y'),
            user.subject,
            user.hobby,
            user.file,
            user.current_address,
            f'{user.state} {user.city}'
        ))
