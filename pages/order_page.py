import allure
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from faker import Faker
from selenium.webdriver.support import expected_conditions
from data import OrderForm
from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators as O


class OrderPage(MainPage):

    def set_subway_station(self, metro):
        self.input_info(O.METRO_INPUT, metro)
        self.wait_for_element_to_load(O.METRO_DOWN_LIST)
        self.click_button(O.METRO_DOWN_LIST)
        self.wait_for_element_to_hide(O.METRO_DOWN_LIST)

    @allure.step('Заполнить форму для заказа самоката')
    def fill_form_correct(self, metro):
        fake = OrderForm
        self.input_info(O.NAME_INPUT, fake.fill_form_name())
        self.input_info(O.SURNAME_INPUT, fake.fill_form_surname())
        self.input_info(O.ADDRESS_INPUT, fake.fill_form_street())
        self.set_subway_station(metro)
        self.input_info(O.NUMBER_INPUT, fake.fill_form_phone())
        self.click_button(O.NEXT_BUTTON)

    @allure.step('Установить сроки аренды')
    def set_date_of_order(self, date, period, colour):
        self.input_info(O.DATE_INPUT, date)
        self.click_button(O.DROPDOWN_PERIOD)
        method, locator = O.DROPDOWN_PERIOD_SELECTION
        locator = locator.format(period)
        self.click_button((method, locator))
        method, locator = O.DROPDOWN_PERIOD_SELECTION_PERIOD
        locator = locator.format(colour)
        self.click_button((method, locator))
        self.input_info(O.COMMENTARY_INPUT, 'Он будет для пьяных поездок')

    @allure.step('Подтвердить заказ и увидеть окно подтверждения')
    def make_order(self):
        self.click_button(O.ORDER_BUTTON)
        self.wait_for_element_to_load(O.CONFIRMATION_WINDOW)
        self.click_button(O.CONFIRMATION_BUTTON)
        self.wait_for_element_to_load(O.ORDER_WINDOW)
