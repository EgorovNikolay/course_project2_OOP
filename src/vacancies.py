class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ["title", "link", "salary", "description"]

    def __init__(self, title, link, salary, description):
        """Конструктор класса"""
        self.title = title
        self.link = link
        self.salary = self.__validate_salary(salary)
        self.description = description

    def __validate_salary(self, salary):
        """Преобразует зарплату в целое число или возвращает 0, если данных нет"""
        if isinstance(salary, dict):
            if salary.get("from"):
                return int(salary["from"])
            elif salary.get("to"):
                return int(salary["to"])
        elif isinstance(salary, (int, float)):
            return int(salary)
        return 0

    def __eq__(self, other):
        """Сравнивает две вакансии по зарплате (равенство)"""
        return self.salary == other.salary

    def __lt__(self, other):
        """Сравнивает две вакансии по зарплате (меньше)"""
        return self.salary < other.salary

    def __gt__(self, other):
        """Сравнивает две вакансии по зарплате (больше)"""
        return self.salary > other.salary

    def to_dict(self):
        """Возвращает словарь с данными вакансии"""
        return {
            "title": self.title,
            "link": self.link,
            "salary": self.salary,
            "description": self.description
        }

    @staticmethod
    def cast_to_object_list(vacancies_data: list) -> list:
        """Преобразует список словарей с данными о вакансиях в список объектов Vacancy"""
        return [Vacancy(
            item["name"],
            item["alternate_url"],
            item.get("salary", {}),
            item["snippet"].get("requirement", "Описание не указано")
        ) for item in vacancies_data]
