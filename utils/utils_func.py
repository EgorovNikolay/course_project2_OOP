def filter_vacancies(vacancies: list, filter_words: list) -> list:
    """Фильтрует вакансии по ключевым словам в описании"""
    return [vacancy for vacancy in vacancies
            if vacancy.description and
            any(word.lower() in vacancy.description.lower() for word in filter_words)]

def sort_vacancies(vacancies: list) -> list:
    """Сортирует вакансии по зарплате (по убыванию)."""
    return sorted(vacancies, reverse=True)

def get_top_vacancies(vacancies: list, top_n: int) -> list:
    """Возвращает топ N вакансий."""
    return vacancies[:top_n]
