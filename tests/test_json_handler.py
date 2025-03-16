import os
import json
from src.vacancies import Vacancy

def test_add_vacancy(json_handler, sample_vacancy):
    json_handler.add_vacancy(sample_vacancy)

    assert os.path.exists(json_handler._JSONHandler__filename)
    with open(json_handler._JSONHandler__filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        assert len(lines) == 1
        assert json.loads(lines[0]) == sample_vacancy.to_dict()

def test_get_vacancies(json_handler, sample_vacancy):
    json_handler.add_vacancy(sample_vacancy)

    vacancies = json_handler.get_vacancies("Python")
    assert len(vacancies) == 1
    assert vacancies[0] == sample_vacancy.to_dict()

    vacancies = json_handler.get_vacancies("Java")
    assert len(vacancies) == 0

def test_delete_vacancy(json_handler, sample_vacancy):
    json_handler.add_vacancy(sample_vacancy)

    with open(json_handler._JSONHandler__filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        assert len(lines) == 1

    json_handler.delete_vacancy(sample_vacancy)

    with open(json_handler._JSONHandler__filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        assert len(lines) == 0

def test_add_multiple_vacancies(json_handler, sample_vacancy):
    json_handler.add_vacancy(sample_vacancy)
    another_vacancy = Vacancy("Java Developer", "http://example.com", 120000, "Описание вакансии")
    json_handler.add_vacancy(another_vacancy)

    with open(json_handler._JSONHandler__filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        assert len(lines) == 2
        assert json.loads(lines[0]) == sample_vacancy.to_dict()
        assert json.loads(lines[1]) == another_vacancy.to_dict()

def test_delete_one_of_multiple_vacancies(json_handler, sample_vacancy):
    json_handler.add_vacancy(sample_vacancy)
    another_vacancy = Vacancy("Java Developer", "http://example.com", 120000, "Описание вакансии")
    json_handler.add_vacancy(another_vacancy)

    json_handler.delete_vacancy(sample_vacancy)

    with open(json_handler._JSONHandler__filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        assert len(lines) == 1
        assert json.loads(lines[0]) == another_vacancy.to_dict()
