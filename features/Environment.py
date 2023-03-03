import time
from features.utility.UtilityClass import UtilityClass

def before_scenario(context, driver):
    UtilityClass.launch_browser(context)
    time.sleep(2)


    UtilityClass.launch_app(context)
    time.sleep(2)
    UtilityClass.Maximize_browser(context)
    time.sleep(2)

def after_scenario(context, driver):
    time.sleep(2)
    UtilityClass.close_browser(context)
