from utils.utils_func import filter_vacancies, sort_vacancies, get_top_vacancies

def test_filter_vacancies(sample_vacancies):
    filtered = filter_vacancies(sample_vacancies, ["Python"])
    assert len(filtered) == 2
    assert filtered[0].title == "Python Developer"
    assert filtered[1].title == "Data Scientist"
    filtered = filter_vacancies(sample_vacancies, ["Java"])
    assert len(filtered) == 2
    assert filtered[0].title == "Java Developer"
    filtered = filter_vacancies(sample_vacancies, ["C++"])
    assert len(filtered) == 0

def test_sort_vacancies(sample_vacancies):
    sorted_vacancies = sort_vacancies(sample_vacancies)
    assert sorted_vacancies[0].salary == 150000
    assert sorted_vacancies[1].salary == 120000
    assert sorted_vacancies[2].salary == 100000
    assert sorted_vacancies[3].salary == 90000

def test_get_top_vacancies(sample_vacancies):
    top_vacancies = get_top_vacancies(sample_vacancies, 2)
    assert len(top_vacancies) == 2
    assert top_vacancies[0].title == "Python Developer"
    assert top_vacancies[1].title == "Java Developer"
    top_vacancies = get_top_vacancies(sample_vacancies, 10)
    assert len(top_vacancies) == 4