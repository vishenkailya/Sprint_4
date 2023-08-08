import allure
import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.main_page import MainPage
from conftest import driver
from locators.main_page_locators import MainPageLocators as L
from locators.order_page_locators import OrderPageLocators as O
from urls import Urls


class TestMainPage:

    @allure.title('Переход на страницу Дзен через кнопку "Яндекс"')
    def test_go_to_dzen_dzen_page_open(self, driver):
        main_page = MainPage(driver)
        main_page.opening_page(Urls.MAIN_PAGE)
        main_page.click_button_dzen_page()
        main_page.wait_for_tab_to_load(Urls.DZEN_MAIN_PAGE)
        main_page.wait_for_tab_to_open(2)
        assert driver.current_url == Urls.DZEN_MAIN_PAGE

    @allure.title('Переход на главную страницу через кнопку "Самокат"')
    def test_go_to_main_page_main_page_opened(self, driver):
        main_page = MainPage(driver)
        main_page.opening_page(Urls.MAIN_PAGE)
        main_page.click_button(L.MAKE_ORDER_UP_BUTTON)
        main_page.wait_for_element_to_load(O.NAME_INPUT)
        main_page.click_scooter_button_main_page()
        main_page.wait_for_element_to_load(L.MAKE_ORDER_UP_BUTTON)
        assert driver.current_url == Urls.MAIN_PAGE


class TestQuestions:

    @allure.title('Открываем вопрос {index} и проверяем текст {answers}')
    @pytest.mark.parametrize('index, answers',
                             [
                                 [1, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
                                 [2, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
                                 [3, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                                 [4, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                                 [5, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
                                 [6, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
                                 [7, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
                                 [8, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
                             ]
                             )
    def test_get_faq_answers(self, driver, index, answers):
        main_page = MainPage(driver)
        main_page.opening_page(Urls.MAIN_PAGE)
        main_page.scroll_to_faq()
        main_page.click_on_question(index)
        answer = main_page.get_answer_text()
        assert answer == answers


