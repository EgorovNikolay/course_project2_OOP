from abc import ABC, abstractmethod


class BaseApi(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def load_vacancies(self, keyword):
        """Абстрактный метод для получения вакансий по ключевому слову"""
        pass
