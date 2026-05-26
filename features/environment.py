from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    options = Options()
    options.add_argument("--incognito")
    # # 1 = Allow, 2 = Block location prompts globally
    # prefs = {"profile.default_content_setting_values.geolocation": 2}
    # options.add_experimental_option("prefs", prefs)

    context.driver = webdriver.Chrome(service=service, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(2)
    # driver.wait?
    context.driver.wait = WebDriverWait(context.driver, 10)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
