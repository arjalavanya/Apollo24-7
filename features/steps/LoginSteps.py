import time
from behave import *
from hamcrest import *
from features.pages.LoginPageClass import LoginPageClass

@given(u'Chrome is opened and Apollo24/7 app is opened')
def step_impl(context):
    time.sleep(3)
    expectedTitle = "Apollo 247 - Online Doctor Consultation & Book Lab Tests at Home"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@when(u'user click on later button')
def step_impl(context):
    time.sleep(3)
    LaterButton=LoginPageClass(context.driver)
    LaterButton.click_Later_button()

@when(u'User clicks on login button')
def step_impl(context):
    loginButton = LoginPageClass(context.driver)
    loginButton.click_login_icon()
    time.sleep(3)


@then(u'It navigates to Mobile Number window')
def step_impl(context):
    time.sleep(3)
    MWText = LoginPageClass(context.driver)
    expectedMWText = "Please enter your mobile number to login"
    actualMWText = MWText.check_MobileWindow_Text()
    print(actualMWText)
    assert_that(expectedMWText, equal_to(actualMWText))


@step(u'User enter "{number}"')
def step_impl(context, number):
    time.sleep(3)
    MobileNumber = LoginPageClass(context.driver)
    MobileNumber.enter_mobilenumber_textbox(number)
    time.sleep(3)


@when(u'User clicks on Next button')
def step_impl(context):
    NextButton = LoginPageClass(context.driver)
    NextButton.click_next_button()
    time.sleep(3)


@then(u'It navigates to OTP window')
def step_impl(context):
    time.sleep(3)
    textofotp = LoginPageClass(context.driver)
    expectedtextofotpText = "Now type in the OTP sent to you for authentication"
    actualtextofotpText = textofotp.check_otpWindow_Text()
    print(actualtextofotpText)
    assert_that(expectedtextofotpText, equal_to(actualtextofotpText))


@when(u'User enter otp')
def step_impl(context):
    time.sleep(20)
    pass


@then(u'It navigates to Home page')
def step_impl(context):
    time.sleep(3)
    username = LoginPageClass(context.driver)
    expectedusernameText = "jungkook"
    actualusernameText = username.check_User_Name()
    print(actualusernameText)
    assert_that(expectedusernameText, equal_to(actualusernameText))





#====================================================================================

@when(u'User enter Mobile Number {MobNum}')
def step_impl(context, MobNum):
    time.sleep(3)
    OutMobNum= LoginPageClass(context.driver)
    OutMobNum.enter_mobnum_tb(MobNum)
    time.sleep(3)

@then(u'User cannot click on Next button')
def step_impl(context):
    time.sleep(3)
    errormsg = LoginPageClass(context.driver)
    expectedalertText = "This seems like a wrong number\nBy signing up, I agree to the Privacy Policy, Terms and Conditions of Apollo247"
    actualalertText = errormsg.check_error()
    print(actualalertText)
    assert_that(expectedalertText, equal_to(actualalertText))


