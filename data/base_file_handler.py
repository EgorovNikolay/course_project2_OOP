from abc import ABC, abstractmethod

class BaseFileHandler(ABC):
    """Абстрактный базовый класс для работы с файлами"""
    @abstractmethod
    def add_vacancy(self, vacancy):
        """Добавляет вакансию в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        """Получает вакансии из файла по критериям"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Удаляет вакансию из файла"""
        pass
