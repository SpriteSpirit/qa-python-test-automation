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
@allure.description("Проверяет создание проекта с пустым названием")
@allure.link("https://ru.yougile.com/api-v2#/operations/ProjectController_create",
             name="Документация Yougile API. Создание проекта")
@pytest.mark.negative_test
def test_create_project_empty_title(projects):
    """
    Создание проекта с пустым названием
    """

    with allure.step("Создание проекта с пустым названием"):
        logger.debug("Создание проекта с пустым названием")

        response = projects.create_project(title="")
        project_id = projects.get_json_from_response(response).get('id')
        logger.debug(f"Создан проект с ID: {project_id}")

        assert response.status_code == 400, f"Ожидаемый статус 400. Текущий статус: {response.status_code}"


@allure_decorator
@allure.description("Проверяет изменение проекта с неверным ID")
@allure.link("https://ru.yougile.com/api-v2#/operations/ProjectController_update",
             name="Документация Yougile API. Изменить проект")
@pytest.mark.negative_test
def test_update_project_invalid_id(projects):
    """
    Изменить проект с неверным ID
    """

    with allure.step("Изменить название проекта с неверным ID"):
        logger.debug("Изменение названия проекта с неверным ID")

        title = f"Тестовый проект_{uuid.uuid4()}"
        update_response = projects.update_project(project_id="invalid_id", title=title)
        updated_project_id = projects.get_json_from_response(update_response).get('id')

        logger.debug(f"ID проекта после изменения:\n{updated_project_id}")

        assert update_response.status_code == 404, \
            f"Ожидаемый статус: 404. Текущий статус: {update_response.status_code}"


@allure_decorator
@allure.description("Проверяет получение проекта по неверному ID")
@allure.link("https://ru.yougile.com/api-v2#/operations/ProjectController_get",
             name="Документация Yougile API. Получить проект по ID")
@pytest.mark.negative_test
def test_get_project_by_id_invalid_id(projects):
    """
    Получить проект по неверному ID
    """

    with allure.step("Получение данных объекта по неверному ID"):
        logger.debug(f"Получение данных объекта по неверному ID")

        response = projects.get_project_by_id(project_id="invalid_id")
        project_data = projects.get_json_from_response(response)
        logger.debug(f"Данные объекта:\n{project_data}")

        assert response.status_code == 404, f"Ожидаемый статус: 404. Текущий статус: {response.status_code}"


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
