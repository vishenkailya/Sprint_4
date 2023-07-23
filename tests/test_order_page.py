import allure
import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from conftest import driver
from locators.order_page_locators import OrderPageLocators as O


class TestOrder:

    @allure.title('Оформление заказа через верхнюю кнопку заказать')
    @pytest.mark.parametrize('date, period, colour, metro',
                             [
                                 ['27.03.2023', 'сутки', 'black', 'Черкизовская'],
                                 ['30.08.2023', 'двое суток', 'grey', 'Курская']
                             ])
    def test_order_button_up_first_set_of_data_oder_made(self, driver, date, period, colour, metro):
        page = BasePage(driver)
        order_button = MainPage()
        order = OrderPage()
        page.opening_page('https://qa-scooter.praktikum-services.ru/')
        order_button.click_order_button_up(driver)
        page.wait_for_element_to_load(O.ORDER_WINDOW)
        order.fill_form_correct(driver, metro)
        order.set_date_of_order(driver, date, period, colour)
        order.make_order(driver)
        assert 'Заказ оформлен' in page.get_description(O.ORDER_MADE)

    @allure.title('Оформление заказа через нижнюю кнопку заказать')
    @pytest.mark.parametrize('date, period, colour, metro',
                             [
                                 ['3.02.2024', 'пятеро суток', 'black', 'Черкизовская'],
                                 ['20.08.2023', 'трое суток', 'grey', 'Курская']
                             ])
    def test_order_button_down_first_set_of_data_order_made(self, driver, date, period, colour, metro):
        page = BasePage(driver)
        order_button = MainPage()
        order = OrderPage()
        page.opening_page('https://qa-scooter.praktikum-services.ru/')
        order_button.click_order_button_down(driver)
        page.wait_for_element_to_load(O.ORDER_WINDOW)
        order.fill_form_correct(driver, metro)
        order.set_date_of_order(driver, date, period, colour)
        order.make_order(driver)
        assert 'Заказ оформлен' in page.get_description(O.ORDER_MADE)
