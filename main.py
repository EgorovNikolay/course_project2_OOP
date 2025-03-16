from src.head_hunter_api import HeadHunterApi
from src.vacancies import Vacancy
from data.json_handler import JSONHandler
from utils.utils_func import filter_vacancies, sort_vacancies, get_top_vacancies

def user_interaction():
    """Функция для взаимодействия с пользователем через консоль"""
    hh_api = HeadHunterApi()
    json_saver = JSONHandler()

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий (через пробел): ").split()

    hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_api.vacancies)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    for vacancy in top_vacancies:
        json_saver.add_vacancy(vacancy)
        print(f"{vacancy.title} | {vacancy.salary} руб. | {vacancy.link}\n{vacancy.description}\n")

if __name__ == "__main__":
    user_interaction()
