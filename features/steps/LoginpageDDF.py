import time
from hamcrest import *
from behave import *
from datafiles import ExcelUtils
from features.pages.LoginPageClass import LoginPageClass
from features.utility.ConfigClass import ConfigClass

@given(u'Chrome is opened and Apollo app is opened')
def step_impl(context):
    time.sleep(3)
    expectedTitle = "Apollo 247 - Online Doctor Consultation & Book Lab Tests at Home"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


@when(u'user clicks on later button')
def step_impl(context):
    time.sleep(3)
    LaterButton=LoginPageClass(context.driver)
    LaterButton.click_Later_button()

@when(u'User click on login button')
def step_impl(context):
    loginButton = LoginPageClass(context.driver)
    loginButton.click_login_icon()
    time.sleep(3)

@then(u'It navigate to Mobile Number window')
def step_impl(context):
    time.sleep(3)
    MWText = LoginPageClass(context.driver)
    expectedMWText = "Please enter your mobile number to login"
    actualMWText = MWText.check_MobileWindow_Text()
    print(actualMWText)
    assert_that(expectedMWText, equal_to(actualMWText))


@step(u'User enters mobile number"{number}"')
def step_impl(context, number):
    time.sleep(3)
    ExcelUtils.get_row_count(ConfigClass.datafilepath, "Sheet1")
    data = ExcelUtils.read_data(ConfigClass.datafilepath, "Sheet1", 2, 1)
    dataenter = LoginPageClass(context.driver)
    dataenter.enter_mobilenumber_textbox(data)

@then(u'It shows error message')
def step_impl(context):
    time.sleep(3)
    errormsg = LoginPageClass(context.driver)
    expectedalertText = "This seems like a wrong number\nBy signing up, I agree to the Privacy Policy, Terms and Conditions of Apollo247"
    actualalertText = errormsg.check_error()
    print(actualalertText)
    assert_that(expectedalertText, equal_to(actualalertText))
    time.sleep(2)
    try:
        if (expectedalertText == actualalertText):
         assert True
         print("Test is passed")
         ExcelUtils.write_data(ConfigClass.datafilepath, "Sheet1", 2, 2, "Passed")
         time.sleep(3)
        else:
         print("Test is failed")
         ExcelUtils.write_data(ConfigClass.datafilepath, "Sheet1", 2, 2, "Failed")
         assert False
        time.sleep(3)

    finally:
        closebutton = LoginPageClass(context.driver)
        closebutton.click_close_button()
        time.sleep(3)
