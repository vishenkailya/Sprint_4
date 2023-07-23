from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_DOWN_LIST = (By.XPATH, "//div[contains(@class, 'select-search__select')]/ul/li")
    NUMBER_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text() = "Далее"]')
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DROPDOWN_PERIOD = (By.XPATH, "//span[@class='Dropdown-arrow']")
    DROPDOWN_PERIOD_SELECTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='{}')]")
    DROPDOWN_PERIOD_SELECTION_PERIOD = (By.XPATH, '//input[@id="{}"]')
    COMMENTARY_INPUT = (By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN"]')
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    CONFIRMATION_WINDOW = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    CONFIRMATION_BUTTON = (By.XPATH, '//button[text()="Да"]')
    ORDER_WINDOW = (By.XPATH, '//div[@class="Order_Header__BZXOb"]')
    ORDER_MADE = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')


