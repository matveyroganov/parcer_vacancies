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
    def delete_vacancy(self, vacancy: list):
        pass


class JSONSaver(AbstractJSONSaver):
    def add_vacancy(self, list_vacancy: list):
        all_vacancies = []
        for params in list_vacancy:
            vacancy = Vacancy.dict_vacancy(params)
            all_vacancies.append(vacancy)
        with open("vacancy.json", "w", encoding="utf-8") as file:
            json.dump(all_vacancies, file, indent=2, ensure_ascii=False)

    def get_vacancies_by_salary(self, salary: int):
        with open("vacancy.json", "r", encoding="utf-8") as file:
            json_vacancies = file.read()
            list_vacancies = json.loads(json_vacancies)
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

    def delete_vacancy(self, vacancy: list):
        pass
