from src.vacancy import Vacancy


def filter_vacancies(all_vacancies: list, filter_words: list):
    """
    Фильрует список объектов класса Vacancy по определенным словам
    :param all_vacancies: список объектов класса Vacancy
    :param filter_words: слова, по которым фильтруется список вакансий
    :return: отфильтрованный список объектов класса Vacancy
    """
    filtered_vacancies = []
    for obj_vacancy in all_vacancies:
        if all(word in obj_vacancy.requirement for word in filter_words):
            filtered_vacancies.append(obj_vacancy)
    return filtered_vacancies


def sort_vacancies(filtered_vacancies: list):
    """
    Сортирует список объектов класса Vacancy по зарплате
    :param filtered_vacancies: список объектов класса Vacancy
    :return: отсортированный список
    """
    return sorted(filtered_vacancies, reverse=True)


def get_top_vacancies(vacancies: list, top_n: int):
    """
    Получает список вакансий, соответствующий количеству топ N
    :param vacancies: список объектов класса Vacancy
    :param top_n: количество, которое будем показывать в топ N
    :return: вакансии в топе по заработной плате
    """
    if top_n > len(vacancies):
        return vacancies[:len(vacancies)]
    return vacancies[:top_n]


def print_vacancies(list_vacancies: list):
    """
    Печатает список вакансий в виде словаря с описанием каждой вакансии
    :param list_vacancies: список объектов класса Vacancy
    :return: список вакансий в виде словаря с описанием каждой вакансии
    """
    all_vacancies = []
    for params in list_vacancies:
        vacancy = Vacancy.dict_vacancy(params)
        all_vacancies.append(vacancy)
    return all_vacancies

