import uuid

import pytest

from lesson_08.yougile.project_api import ProjectAPI
from utilities.logger_utils import logger


@pytest.fixture(scope="module")
def projects() -> ProjectAPI:
    """
    Фикстура для создания экземпляра ProjectsAPI.

    Возвращает:
        str: Экземпляр BaseAPI
    """

    logger.debug("Создание объекта projects")
    projects_api = ProjectAPI()
    logger.debug(f"Ключ: {projects_api.api_key}")

    yield projects_api

    logger.debug("Освобождение объекта projects и ключа")
    projects_api.delete_key(projects_api.api_key)
    del projects_api


@pytest.fixture(scope="module")
def new_project_id(projects) -> str:
    """
    Фикстура для создания тестового проекта.

    Возвращает:
        str: ID созданного проекта
    """

    logger.debug("Создание нового проекта")

    title = f"Тестовый проект_{uuid.uuid4()}"
    logger.debug(f"Название проекта: {title}")

    response = projects.create_project(title=title)
    project_id = projects.get_json_from_response(response).get('id')

    return project_id
