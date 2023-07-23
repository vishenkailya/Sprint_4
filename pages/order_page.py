import allure
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from faker import Faker
from selenium.webdriver.support import expected_conditions
from test_sets import OrderForm
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as O


class OrderPage:

    def set_subway_station(self, driver, metro):
        page = BasePage(driver)
        page.input_info(O.METRO_INPUT, metro)
        page.wait_for_element_to_load(O.METRO_DOWN_LIST)
        page.click_button(O.METRO_DOWN_LIST)
        page.wait_for_element_to_hide(O.METRO_DOWN_LIST)

    @allure.step('Заполнить форму для заказа самоката')
    def fill_form_correct(self, driver, metro):
        page = BasePage(driver)
        fake = OrderForm
        page.input_info(O.NAME_INPUT, fake.fill_form_name())
        page.input_info(O.SURNAME_INPUT, fake.fill_form_surname())
        page.input_info(O.ADDRESS_INPUT, fake.fill_form_street())
        self.set_subway_station(driver, metro)
        page.input_info(O.NUMBER_INPUT, fake.fill_form_phone())
        page.click_button(O.NEXT_BUTTON)

    @allure.step('Установить сроки аренды')
    def set_date_of_order(self, driver, date, period, colour):
        page = BasePage(driver)
        page.input_info(O.DATE_INPUT, date)
        page.click_button(O.DROPDOWN_PERIOD)
        method, locator = O.DROPDOWN_PERIOD_SELECTION
        locator = locator.format(period)
        page.click_button((method, locator))
        method, locator = O.DROPDOWN_PERIOD_SELECTION_PERIOD
        locator = locator.format(colour)
        page.click_button((method, locator))
        page.input_info(O.COMMENTARY_INPUT, 'Он будет для пьяных поездок')

    @allure.step('Подтвердить заказ и увидеть окно подтверждения')
    def make_order(self, driver):
        page = BasePage(driver)
        page.click_button(O.ORDER_BUTTON)
        page.wait_for_element_to_load(O.CONFIRMATION_WINDOW)
        page.click_button(O.CONFIRMATION_BUTTON)
        page.wait_for_element_to_load(O.ORDER_WINDOW)
