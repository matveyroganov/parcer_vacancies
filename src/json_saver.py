import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class AbstractJSONSaver(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy: list):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary: int):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(AbstractJSONSaver):

    def __init__(self):
        self.file = "vacancy.json"

    def add_vacancy(self, list_vacancy: list):
        """
        Записывает объекты класса с вакансиями в файл JSON
        :param list_vacancy: список объектов класса Vacancy
        :return: None
        """
        all_vacancies = []
        for params in list_vacancy:
            vacancy = Vacancy.dict_vacancy(params)
            all_vacancies.append(vacancy)
        with open(self.file, "w", encoding="utf-8") as file:
            json.dump(all_vacancies, file, indent=2, ensure_ascii=False)

    def get_vacancies_by_salary(self, salary: int):
        """
        Получаем список вакансий исходя из указанной зарплаты
        :param salary: зарплата, с которой мы сравниваем вакансии
        :return: список вакансий, подходящих под указанную зарплату
        """
        with open(self.file, "r", encoding="utf-8") as file:
            list_vacancies = json.load(file)
        all_vacancy_by_salary = []
        for vacancy in list_vacancies:
            salary_from = vacancy["salary_from"]
            if vacancy["salary_to"] == 0:
                salary_to = salary_from
            else:
                salary_to = vacancy["salary_to"]

            if salary_from >= salary:
                all_vacancy_by_salary.append(vacancy)
            elif salary_from < salary <= salary_to:
                all_vacancy_by_salary.append(vacancy)
        return all_vacancy_by_salary

    def delete_vacancy(self):
        """
        Удаление данных из файла JSON
        """
        with open(self.file, "r", encoding="utf-8") as file:
            list_vacancy = json.load(file)
        clear_list_vacancy = list_vacancy.clear()
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(clear_list_vacancy, f)
