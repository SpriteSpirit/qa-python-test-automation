import os

import requests
import dotenv
from requests import Response

from utilities.logger_utils import logger


class BaseAPI:
    """
    Page Object для API Yougile.
    """

    def __init__(self):
        self.base_url = "https://ru.yougile.com/api-v2"
        self.session = requests.Session()
        self.api_key = self.get_api_key()
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def __del__(self):
        """
        Деструктор для освобождения ресурсов
        """

        if hasattr(self, 'session'):
            self.session.close()
            print("Сессия закрыта, объект BaseAPI удален.")

    def _build_url(self, endpoint: str) -> str:
        return f"{self.base_url}{endpoint}"

    @property
    def auth_json(self) -> dict:
        dotenv.load_dotenv()
        return {
            "login": os.getenv("YOUGILE_LOGIN"),
            "password": os.getenv("YOUGILE_PASSWORD"),
            "companyId": os.getenv("YOUGILE_COMPANY_ID")
        }

    def get_json_from_response(self, response: Response) -> dict:
        """
        Получает JSON из ответа.

        Returns:
            dict: JSON из ответа
        """

        return response.json()

    def get_api_key(self) -> str:
        """
        Получает API ключ через авторизацию пользователя.

        Returns:
            str: API ключом в строковом представлении
        """

        response = self.session.post(
            self.base_url + "/auth/keys",
            json=self.auth_json
        )

        return response.json().get('key')

    def get_object_list(self, url: str) -> Response:
        """
        Получает список объектов из указанного URL с добавленными параметрами.
        Возвращает ответ.

        Args:
            url (str): URL для получения списка объектов. (format: /url)
        """

        response = self.session.get(
            self._build_url(url),
            headers=self.headers
        )

        return response

    def create_object(self, url: str, title: str, users: dict = None) -> Response:
        """
        Создание объекта.
        Возвращает ответ.

        Args:
            url (str): URL для создания объекта (format: /url)
            title (str): Название объекта
            users (dict): Список пользователей для объекта
        """

        response = self.session.post(
            self._build_url(url),
            json={"title": title, "users": users} if users is not None else {"title": title},
            headers=self.headers
        )

        return response

    def update_object(self, url: str, object_id: str, title: str, users: dict = None) -> Response:
        """
        Обновление объекта с указанным ID.
        Возвращает ответ.

        Args:
            url (str): URL для получения объекта (format: /url)
            object_id (str): ID объекта
            title (str): Новое название объекта
            users (dict): Новый список пользователей для объекта
        """

        response = self.session.put(
            f"{self._build_url(url)}/{object_id}",
            json={"title": title, "users": users} if users is not None else {"title": title},
            headers=self.headers
        )

        return response

    def get_object_by_id(self, url: str, object_id: str) -> Response:
        """
        Получение объекта по его ID.
        Возвращает ответ.

        Args:
            url (str): URL для получения объекта (format: /url)
            object_id (str): ID объекта
        """

        response = self.session.get(
            f"{self._build_url(url)}/{object_id}",
            headers=self.headers
        )

        return response

    def get_key_list(self) -> Response:
        """
        Получение списка ключей доступа.
        Возвращает ответ.
        """

        logger.debug(self.auth_json)
        response = self.session.post(self._build_url(f"/auth/keys/get"), json=self.auth_json)
        logger.debug(response.json())

        return response

    def delete_key(self, key: str) -> Response:
        """
        Удаление текущего ключа доступа.
        Возвращает ответ.
        """

        logger.debug(f"Удаление ключа: {key[:10]}...")

        return self.session.delete(
            self._build_url(f"/auth/keys/{key}"),
            headers=self.headers
        )

    def delete_all_keys(self) -> None:
        """
        Удаление всех ключей доступа из списка.
        """

        keys = self.get_json_from_response(self.get_key_list())
        logger.debug(f"Получено ключей для удаления: {len(keys)}")

        deleted_count = 0

        for key_data in keys:
            if isinstance(key_data, dict) and 'key' in key_data:
                if self.delete_key(key_data['key']):
                    deleted_count += 1

        logger.debug(f"Успешно удалено ключей: {deleted_count} из {len(keys)}")
