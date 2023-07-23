from selenium.webdriver.common.by import By

class MainPageLocators:
    MAKE_ORDER_UP_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    MAKE_ORDER_DOWN_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    SCOOTER_BUTTON = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    YANDEX_DZEN_BUTTON = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]')
    LOCATOR_FAQ = (By.XPATH, '//*[@class="Home_FAQ__3uVm4"]')
    LOCATOR_FAQ_ANSWER = (By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]")
    LOCATOR_QUESTIONS = By.XPATH, "//div[contains(@class, 'accordion__item')]"
