import pytest
import requests
import allure

BASE_URL = "https://api.kinopoisk.dev/v1.4"
API_TOKEN = ""

@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_movie_by_title():
    url = f"{BASE_URL}/movie/search"
    headers = {"X-API-KEY": API_TOKEN}
    params = {"query": "Оно"}

    with allure.step("Отправляем запрос на поиск фильма по названию"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверяем статус-код и наличие результатов"):
        assert response.status_code == 200
        assert len(response.json().get("docs", [])) > 0


@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_movie_interstellar():
    url = f"{BASE_URL}/movie/search"
    headers = {"X-API-KEY": API_TOKEN}
    params = {"query": "Интерстеллар"}

    with allure.step("Отправляем запрос на поиск фильма 'Интерстеллар'"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверяем статус-код и наличие результатов"):
        assert response.status_code == 200
        assert len(response.json().get("docs", [])) > 0


@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_with_limit():
    url = f"{BASE_URL}/movie/search"
    headers = {"X-API-KEY": API_TOKEN}
    params = {"query": "Оно", "limit": 1}

    with allure.step("Отправляем запрос с параметром limit=1"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверяем статус-код и количество результатов"):
        assert response.status_code == 200
        assert len(response.json().get("docs", [])) == 1


@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_empty_query():
    url = f"{BASE_URL}/movie/search"
    headers = {"X-API-KEY": API_TOKEN}
    params = {"query": ""}

    with allure.step("Отправляем запрос с пустым query"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверяем статус-код (200 или 400)"):
        assert response.status_code in [200, 400]


@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_with_invalid_token():
    url = f"{BASE_URL}/movie/search"
    headers = {"X-API-KEY": "12345"}
    params = {"query": "Оно"}

    with allure.step("Отправляем запрос с неверным токеном"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверяем, что возвращается 401 Unauthorized"):
        assert response.status_code == 401