import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(300)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Поиск")
def test_search_bar_is_displayed(driver):
    with allure.step("Открываем сайт Кинопоиск"):
        driver.get("https://www.kinopoisk.ru/")

    with allure.step("Проверяем наличие строки поиска"):
        search_bar = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "kp_query"))
        )
        assert search_bar.is_displayed()


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Карточка фильма")
def test_movie_card_is_displayed(driver):

    with allure.step("Открываем сайт Кинопоиск"):
        driver.get("https://www.kinopoisk.ru/")

    with allure.step("Вводим текст в поиск"):
        search_bar = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "kp_query"))
        )
        search_bar.send_keys("Оно\n")

    with allure.step("Проверяем наличие карточки фильма"):
        movie_card = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'a[href*="/film/"]')
            )
        )
        assert movie_card.is_displayed()


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Популярные фильмы")
def test_popular_movies_page(driver):
    with allure.step("Открываем страницу популярных фильмов"):
        driver.get("https://www.kinopoisk.ru/lists/movies/popular/")

    with allure.step("Проверяем наличие карточки фильма"):
        movie_card = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'a[href*="/film/"]')
            )
        )
        assert movie_card.is_displayed()



@pytest.mark.ui
@allure.feature("UI")
@allure.story("Главная страница")
def test_main_page_title(driver):

    with allure.step("Открываем сайт Кинопоиск"):
        driver.get("https://www.kinopoisk.ru/")

    with allure.step("Проверяем заголовок страницы"):
        assert "Кинопоиск" in driver.title


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Кнопка входа")
def test_login_button_is_displayed(driver):

    with allure.step("Открываем сайт Кинопоиск"):
        driver.get("https://www.kinopoisk.ru/")

    with allure.step("Проверяем наличие кнопки 'Войти'"):
        login_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Войти')]")
            )
        )
        assert login_button.is_displayed()
