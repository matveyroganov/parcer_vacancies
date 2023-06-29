from src.connect_api import HeadHunterAPI, SuperJobAPI
from src.vacancy import Vacancy
from src.json_saver import JSONSaver
from src.utils import filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies


def user_interaction():

    # просит выбрать, на каких платформах будем собирать вакансии
    try:
        input_platforms = int(input("Необходимо ввести число, которое соответствует тому, с каких платформ вы хотите "
                                    "получить вакансии:\n1. Head Hunter\n2. Super Job\n3. Все платформы\n"))
        while input_platforms not in [1, 2, 3]:
            print("Неверное число. Введите число из списка")
            input_platforms = int(
                input("Необходимо ввести число, которое соответствует тому, с каких платформ вы хотите "
                      "получить вакансии:\n1. Head Hunter\n2. Super Job\n3. Все платформы\n"))
    except ValueError:
        print("Некорректный выбор. Нужно выбрать число из списка. Перезапустите программу")
        exit()

    # просит ввести поисковый запрос
    search_query = input("Введите поисковый запрос: ")

    # просит ввести количество вакансий для вывода в топ N
    try:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    except ValueError:
        print("Некорректный ввод. Нужно ввести целое число. Перезапустите программу")
        exit()

    # просит ввести слова для фильтрации вакансии
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    list_all_vacancies = []

    # проверяет условия выбора платформы

    if input_platforms == 1:
        # формирует объект для работы с API HeadHunter
        obj_hh_api = HeadHunterAPI()

        # получает вакансии с API HeadHunter исходя из запроса юзера
        hh_vac_by_search = obj_hh_api.get_vacancies(search_query)

        # получает список вакансий HeadHunter с определенными данными, которые прописаны в классе Vacancy
        list_obj_hh_vac = Vacancy.get_vac_hh(hh_vac_by_search)

        list_all_vacancies = list_obj_hh_vac

    if input_platforms == 2:
        # формирует объект для работы с API SuperJob
        obj_sj_api = SuperJobAPI()

        # получает вакансии с API SuperJob исходя из запроса юзера
        sj_vac_by_search = obj_sj_api.get_vacancies(search_query)

        # получает список вакансий SuperJob с определенными данными, которые прописаны в классе Vacancy
        list_obj_sj_vac = Vacancy.get_vac_sj(sj_vac_by_search)

        list_all_vacancies = list_obj_sj_vac

    if input_platforms == 3:
        # формирует объект для работы с API SuperJob и HeadHunter
        obj_hh_api = HeadHunterAPI()
        obj_sj_api = SuperJobAPI()

        # получает вакансии с API HeadHunter и SuperJob исходя из запроса юзера
        hh_vac_by_search = obj_hh_api.get_vacancies(search_query)
        sj_vac_by_search = obj_sj_api.get_vacancies(search_query)

        # получает список вакансий HeadHunter и SuperJob с определенными данными, которые прописаны в классе Vacancy
        list_obj_hh_vac = Vacancy.get_vac_hh(hh_vac_by_search)
        list_obj_sj_vac = Vacancy.get_vac_sj(sj_vac_by_search)

        list_all_vacancies = list_obj_hh_vac + list_obj_sj_vac

    # фильтрует список вакансий по ключевым словам
    filtered_vacancies = filter_vacancies(list_all_vacancies, filter_words)

    # формирует объект для записи списка вакансий в JSON
    json_vacancies = JSONSaver()

    # записывает отфильтрованные вакансии в файл JSON
    json_vacancies.add_vacancy(filtered_vacancies)

    # проверяет существование вакансий с введенными словами для фильтрации
    if len(filtered_vacancies) == 0:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    # сортирует список вакансий по зарплате
    sorted_vacancies = sort_vacancies(filtered_vacancies)

    # получает топ N вакансий по сортированному списку
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # печатает список топ N вакансий
    print(print_vacancies(top_vacancies))


if __name__ == "__main__":
    user_interaction()
