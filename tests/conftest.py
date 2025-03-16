import pytest
from data.json_handler import JSONHandler
from src.vacancies import Vacancy

@pytest.fixture
def json_handler(tmp_path):
    filename = tmp_path / "vacancies.json"
    handler = JSONHandler(filename=str(filename))
    return handler

@pytest.fixture
def sample_vacancy():
    return Vacancy("Python Developer", "http://example.com", 100000, "Описание вакансии")

@pytest.fixture
def sample_vacancies():
    return [
        Vacancy("Python Developer", "http://example.com", 100000, "Требуется опыт работы с Python."),
        Vacancy("Java Developer", "http://example.com", 120000, "Требуется опыт работы с Java."),
        Vacancy("Data Scientist", "http://example.com", 150000, "Требуется опыт работы с Python и Machine Learning."),
        Vacancy("Frontend Developer", "http://example.com", 90000, "Требуется опыт работы с JavaScript."),
    ]
