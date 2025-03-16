from unittest.mock import patch, Mock
from src.head_hunter_api import HeadHunterApi

class TestHeadHunterApi:

    def test_initialization(self):
        api = HeadHunterApi()
        assert api.url == 'https://api.hh.ru/vacancies'
        assert api.params == {'text': '', 'page': 0, 'per_page': 100}
        assert api.vacancies == []


    @patch('requests.get')
    def test_load_vacancies_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        api = HeadHunterApi()
        api.load_vacancies('Python')

        assert len(api.vacancies) == 0
        assert api.params['page'] == 0


    @patch('requests.get')
    def test_load_vacancies_max_pages(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'items': [
                {'id': '1', 'name': 'Python Developer', 'alternate_url': 'http://example.com', 'salary': None, 'snippet': {'requirement': 'Знание Python'}}
            ]
        }
        mock_get.return_value = mock_response

        api = HeadHunterApi()
        api.load_vacancies('Python')

        assert api.params['page'] == 20
