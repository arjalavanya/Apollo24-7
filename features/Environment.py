
from features.utility.UtilityClass import UtilityClass

def before_scenario(context, driver):
    UtilityClass.launch_browser(context)
    context.driver.implicitly_wait(10)


    UtilityClass.launch_app(context)
    context.driver.implicitly_wait(10)
    UtilityClass.Maximize_browser(context)
    context.driver.implicitly_wait(10)

def after_scenario(context, driver):
    context.driver.implicitly_wait(10)
    UtilityClass.close_browser(context)
