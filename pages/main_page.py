import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as L


class MainPage(BasePage):

    @allure.step('Переходим к секции с вопросами и ответами')
    def scroll_to_faq(self):
        self.scroll_page(L.LOCATOR_FAQ)
        self.wait_for_element_to_load(L.LOCATOR_QUESTIONS)

    def get_question(self):
        return self.driver.find_elements(*L.LOCATOR_QUESTIONS)

    @allure.step('Нажимаем на вопрос {index}')
    def click_on_question(self, index):
        question = self.get_question()
        question[index - 1].click()
        WebDriverWait(self.driver, 25).until(
            expected_conditions.visibility_of_element_located(L.LOCATOR_FAQ_ANSWER))

    @allure.step('Получаем ответ на вопрос')
    def get_answer_text(self):
        return self.driver.find_element(*L.LOCATOR_FAQ_ANSWER).text

    @allure.step('Нажать на кнопку "Заказать" в шапке')
    def click_order_button_up(self):
        self.click_button(L.MAKE_ORDER_UP_BUTTON)

    @allure.step('Нажать на кнопку "Заказать" внизу')
    def click_order_button_down(self):
        self.scroll_page(L.MAKE_ORDER_DOWN_BUTTON)
        self.click_button(L.MAKE_ORDER_DOWN_BUTTON)

    @allure.step('Нажать на лого "Самокат" для перехода на главную страницу')
    def click_scooter_button_main_page(self):
        self.scroll_page(L.SCOOTER_BUTTON)
        self.click_button(L.SCOOTER_BUTTON)

    @allure.step('Нажать на лого "Яндекс" для перехода на главную страницу Дзен')
    def click_button_dzen_page(self):
        self.scroll_page(L.YANDEX_DZEN_BUTTON)
        self.click_button(L.YANDEX_DZEN_BUTTON)

