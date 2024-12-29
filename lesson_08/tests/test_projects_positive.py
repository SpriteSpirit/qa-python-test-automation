import uuid
import allure
import functools

import pytest

from utilities.logger_utils import logger


def allure_decorator(func):
    """
    Декоратор для добавления Allure-тэгов и описаний к тестам
    """

    @allure.story("Yougile 'Проекты'")
    @allure.tag("API")
    @allure.label("owner", "Халуева Ангелина")
    @allure.severity(allure.severity_level.CRITICAL)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@allure_decorator
@allure.description("Проверяет получение ключа авторизации")
@allure.link("https://ru.yougile.com/api-v2#/",
             name="Документация Yougile API. Получение ключа")
@pytest.mark.positive_test
def test_get_api_key(projects):
    """
    Получение токена авторизации
    """

    with allure.step("Получение ключа авторизованного пользователя"):
        logger.debug("Получение ключа авторизованного пользователя")
        key = projects.api_key
        logger.debug(f"API-ключ: {key}")

        assert key, "Ошибка получения ключа"
        assert isinstance(key, str), "Ключ авторизации не является строкой"
        assert len(key) > 0, "Ключ авторизации пустой"


@allure_decorator
@allure.description("Проверяет возможность создания проекта")
@allure.link("https://ru.yougile.com/api-v2#/operations/ProjectController_create",
             name="Документация Yougile API. Создание проекта")
@pytest.mark.positive_test
def test_create_project(projects):
    """
    Создание проекта
    """

    with allure.step("Создание проекта"):
        logger.debug("Создание проекта")

        title = f"Тестовый проект_{uuid.uuid4()}"

        response = projects.create_project(title=title)
        project_id = projects.get_json_from_response(response).get('id')
        logger.debug(f"Создан проект с ID: {project_id}")

        assert project_id, "Ошибка создания проекта"
        assert isinstance(project_id, str), "ID проекта не является строкой"
        assert response.status_code == 201, f"Ожидаемый статус 201. Текущий статус: {response.status_code}"


@allure_decorator
@allure.description("Проверяет возможность получения списка проектов")
@allure.link("https://ru.yougile.com/api-v2#/operations/ProjectController_search",
             name="Документация Yougile API. Список проектов")
@pytest.mark.positive_test
def test_get_project_list(projects):
    """
    Получить список проектов
    """

    with allure.step("Получение списка проектов"):
        logger.debug("Получение списка проектов")

        logger.debug("Получение списка объектов")
        response = projects.get_project_list()
        project_list = projects.get_json_from_response(response).get('content')

        assert response.status_code == 200
        assert len(project_list) > 0, "Список проектов пуст"
        assert isinstance(project_list, list), "Передан не список"


@allure_decorator
@allure.description("Проверяет возможность изменения проекта")
@allure.link("https://ru.yougile.com/api-v2#/operations/ProjectController_update",
             name="Документация Yougile API. Изменить проект")
@pytest.mark.positive_test
def test_update_project(projects, new_project_id):
    """
    Изменить проект
    """

    with allure.step("Изменить название проекта"):
        logger.debug("Изменение названия проекта")

        title = f"Тестовый проект_{uuid.uuid4()}"
        update_response = projects.update_project(project_id=new_project_id, title=title)
        updated_project_id = projects.get_json_from_response(update_response).get('id')

        logger.debug(f"ID проекта после изменения:\n{updated_project_id}")

        assert update_response.status_code == 200, \
            f"Ожидаемый статус: 200. Текущий статус: {update_response.status_code}"
        assert updated_project_id == new_project_id, "ID проекта изменился"
        assert isinstance(updated_project_id, str), "ID проекта не является строкой"

    with allure.step("Проверить, что название проекта изменилось"):
        logger.debug("Проверить, что название проекта изменилось")

        get_by_id_response = projects.get_project_by_id(project_id=updated_project_id)
        updated_project_data = projects.get_json_from_response(get_by_id_response)

        logger.debug(f"Проект после изменения:\n{updated_project_data}")

        assert update_response.status_code == 200, \
            f"Ожидаемый статус: 200. Текущий статус: {get_by_id_response.status_code}"
        assert updated_project_data["title"] == title, "Название проекта не изменилось"
        assert isinstance(updated_project_data, dict), "Передан не словарь"


@allure_decorator
@allure.description("Проверяет возможность получения проекта по ID")
@allure.link("https://ru.yougile.com/api-v2#/operations/ProjectController_get",
             name="Документация Yougile API. Получить проект по ID")
@pytest.mark.positive_test
def test_get_project_by_id(projects, new_project_id):
    """
    Получить проект по ID
    """

    with allure.step("Получение данных объекта по ID"):
        logger.debug(f"Получение данных объекта по ID: {new_project_id}")

        response = projects.get_project_by_id(project_id=new_project_id)
        project_data = projects.get_json_from_response(response)
        logger.debug(f"Данные объекта:\n{project_data}")

        assert response.status_code == 200, f"Ожидаемый статус: 200. Текущий статус: {response.status_code}"
        assert project_data, "Данные отсутствуют"
        assert isinstance(project_data, dict), "Передан не словарь"
