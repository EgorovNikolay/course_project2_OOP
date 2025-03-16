import json
from .base_file_handler import BaseFileHandler

class JSONHandler(BaseFileHandler):
    """Класс для работы с JSON-файлами"""
    def __init__(self, filename="data/vacancies.json"):
        """Конструктор класса. Устанавливает имя файла"""
        self.__filename = filename

    def add_vacancy(self, vacancy):
        """Добавляет вакансию в JSON-файл."""
        with open(self.__filename, "a", encoding="utf-8") as file:
            json.dump(vacancy.to_dict(), file, ensure_ascii=False)
            file.write("\n")

    def get_vacancies(self, criteria):
        """Получает вакансии из JSON-файла по критериям"""
        with open(self.__filename, "r", encoding="utf-8") as file:
            return [json.loads(line) for line in file if criteria.lower() in line.lower()]

    def delete_vacancy(self, vacancy):
        """Удаляет вакансию из JSON-файла"""
        with open(self.__filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        with open(self.__filename, "w", encoding="utf-8") as file:
            for line in lines:
                if json.loads(line) != vacancy.to_dict():
                    file.write(line)
