from requests import Response
from lesson_08.yougile.base_api import BaseAPI


class ProjectAPI(BaseAPI):
    """
    Page Object для API Проекты.
    """

    def __init__(self):
        super().__init__()
        self.url = "/projects"

    def get_project_list(self) -> Response:
        """
        Получает список проектов.
        Возвращает ответ.
        """

        return self.get_object_list(self.url)

    def create_project(self, title: str, users: dict = None) -> Response:
        """
        Создает объект.
        Возвращает ответ.

        Args:
            title (str): Название объекта
            users (dict): Список пользователей для объекта
        """

        return self.create_object(self.url, title, users)

    def update_project(self, project_id: str, title: str, users: dict = None) -> Response:
        """
        Обновление объекта с указанным ID.
        Возвращает ответ.

        Args:
            project_id (str): ID объекта
            title (str): Новое название объекта
            users (dict): Новый список пользователей для объекта
        """

        return self.update_object(self.url, project_id, title, users)

    def get_project_by_id(self, project_id: str) -> Response:
        """
        Получение объекта по его ID.
        Возвращает ответ.

        Args:
            project_id (str): ID объекта
        """

        return self.get_object_by_id(self.url, project_id)
