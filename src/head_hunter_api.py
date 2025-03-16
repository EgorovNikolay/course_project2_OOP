from src.base_api_class import BaseApi
import requests


class HeadHunterApi(BaseApi):
    """Класс для работы с API на hh.ru"""
    def __init__(self):
        """Конструктор класса"""
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []


    def load_vacancies(self, keyword):
        """Загружает вакансии по ключевому слову"""
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, params=self.params)
            if response.status_code == 200:
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.params['page'] += 1
            else:
                print(f"Ошибка при загрузке страницы {self.params['page'] + 1}: {response.status_code}")
                break
