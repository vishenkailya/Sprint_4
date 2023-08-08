import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker
from conftest import driver


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    def get_description(self, path):
        return self.driver.find_element(*path).text

    @allure.step('Открыть страницу {url}')
    def opening_page(self, url):
        self.driver.get(url)

    @allure.step('Опустить на странице до {element}')
    def scroll_page(self, element):
        order = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", order)

    def input_info(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_to_load(self, locator):
        WebDriverWait(self.driver, 10). \
            until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_to_hide(self, locator):
        WebDriverWait(self.driver, 10). \
            until(expected_conditions.invisibility_of_element(locator))

    def wait_for_tab_to_load(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    def wait_for_tab_to_open(self, tab):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(tab))
