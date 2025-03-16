import pytest
from src.vacancies import Vacancy

class TestVacancy:

    def test_vacancy_initialization(self):
        vacancy = Vacancy("Python Developer", "http://example.com", 100000, "Описание вакансии")
        assert vacancy.title == "Python Developer"
        assert vacancy.link == "http://example.com"
        assert vacancy.salary == 100000
        assert vacancy.description == "Описание вакансии"

    @pytest.mark.parametrize("salary, expected", [
        ({"from": 120000}, 120000),
        ({"to": 150000}, 150000),
        (130000, 130000),
        (140000.0, 140000),
        (None, 0),
    ])
    def test_validate_salary(self, salary, expected):
        vacancy = Vacancy("Python Developer", "http://example.com", salary, "Описание вакансии")
        assert vacancy.salary == expected

    def test_vacancy_equality(self):
        vacancy1 = Vacancy("Python Developer", "http://example.com", 100000, "Описание вакансии")
        vacancy2 = Vacancy("Java Developer", "http://example.com", 100000, "Описание вакансии")
        assert vacancy1 == vacancy2

    def test_vacancy_less_than(self):
        vacancy1 = Vacancy("Python Developer", "http://example.com", 90000, "Описание вакансии")
        vacancy2 = Vacancy("Java Developer", "http://example.com", 100000, "Описание вакансии")
        assert vacancy1 < vacancy2

    def test_vacancy_greater_than(self):
        vacancy1 = Vacancy("Python Developer", "http://example.com", 110000, "Описание вакансии")
        vacancy2 = Vacancy("Java Developer", "http://example.com", 100000, "Описание вакансии")
        assert vacancy1 > vacancy2

    def test_to_dict(self):
        vacancy = Vacancy("Python Developer", "http://example.com", 100000, "Описание вакансии")
        expected_dict = {
            "title": "Python Developer",
            "link": "http://example.com",
            "salary": 100000,
            "description": "Описание вакансии"
        }
        assert vacancy.to_dict() == expected_dict

    def test_cast_to_object_list(self):
        vacancies_data = [
            {
                "name": "Python Developer",
                "alternate_url": "http://example.com",
                "salary": {"from": 100000},
                "snippet": {"requirement": "Знание Python"}
            },
            {
                "name": "Java Developer",
                "alternate_url": "http://example.com",
                "salary": {"to": 120000},
                "snippet": {"requirement": "Знание Java"}
            }
        ]
        vacancies = Vacancy.cast_to_object_list(vacancies_data)
        assert len(vacancies) == 2
        assert vacancies[0].title == "Python Developer"
        assert vacancies[1].title == "Java Developer"
        assert vacancies[0].salary == 100000
        assert vacancies[1].salary == 120000