import allure
import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from pages.order_page import OrderPage
from conftest import driver
from locators.order_page_locators import OrderPageLocators as O
from urls import Urls


class TestOrder:

    @allure.title('Оформление заказа через верхнюю кнопку заказать')
    @pytest.mark.parametrize('date, period, colour, metro',
                             [
                                 ['27.03.2023', 'сутки', 'black', 'Черкизовская'],
                                 ['30.08.2023', 'двое суток', 'grey', 'Курская']
                             ])
    def test_order_button_up_first_set_of_data_oder_made(self, driver, date, period, colour, metro):
        order = OrderPage(driver)
        order.opening_page(Urls.MAIN_PAGE)
        order.click_order_button_up()
        order.wait_for_element_to_load(O.ORDER_WINDOW)
        order.fill_form_correct(metro)
        order.set_date_of_order(date, period, colour)
        order.make_order()
        assert 'Заказ оформлен' in order.get_description(O.ORDER_MADE)

    @allure.title('Оформление заказа через нижнюю кнопку заказать')
    @pytest.mark.parametrize('date, period, colour, metro',
                             [
                                 ['3.02.2024', 'пятеро суток', 'black', 'Черкизовская'],
                                 ['20.08.2023', 'трое суток', 'grey', 'Курская']
                             ])
    def test_order_button_down_first_set_of_data_order_made(self, driver, date, period, colour, metro):
        order = OrderPage(driver)
        order.opening_page(Urls.MAIN_PAGE)
        order.click_order_button_down()
        order.wait_for_element_to_load(O.ORDER_WINDOW)
        order.fill_form_correct(metro)
        order.set_date_of_order(date, period, colour)
        order.make_order()
        assert 'Заказ оформлен' in order.get_description(O.ORDER_MADE)
