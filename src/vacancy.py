class Vacancy:

    """
    Создаем класс для работы с вакансиями
    """

    def __init__(self, name_vac: str | None, url_vac: str | None, salary_from: int | None, salary_to: int | None,
                 requirement: str | None, experience: str | None):

        # название вакансии
        self.__name_vac = name_vac

        # ссылка на вакансию
        self.__url_vac = url_vac

        # заработная плата от
        if salary_from is not None:
            self.__salary_from = salary_from
        else:
            self.__salary_from = 0

        # заработная плата до
        if salary_to is not None:
            self.__salary_to = salary_to
        else:
            self.__salary_to = 0

        # требования по вакансии
        self.__requirement = requirement

        # требуемый опыт
        self.__experience = experience

    @property
    def name_vac(self):
        """
        Геттер для приватного атрибута названия вакансии
        :return:
        """
        return self.__name_vac

    @name_vac.setter
    def name_vac(self, name_vac):
        """
        Сеттер name_vac проверяет валидность названия вакансии
        """
        if type(name_vac) is str and name_vac != "":
            self.__name_vac = name_vac
        else:
            raise Exception("Внимание! Название вакансии указана")

    @property
    def url_vac(self):
        """
        Геттер для приватного атрибута ссылки на вакансию
        :return:
        """
        return self.__url_vac

    @url_vac.setter
    def url_vac(self, url_vac):
        """
        Сеттер url_vac проверяет валидность ссылки на вакансию
        """
        if type(url_vac) is str and url_vac != "":
            self.__name_vac = url_vac
        else:
            raise Exception("Внимание! Ссылка на вакансию указана некорректно")

    @property
    def salary_from(self):
        """
        Геттер для приватного атрибута заработной платы от
        :return:
        """
        return self.__salary_from

    @property
    def salary_to(self):
        """
        Геттер для приватного атрибута заработной платы до
        :return:
        """
        return self.__salary_from

    @property
    def requirement(self):
        """
        Геттер для приватного атрибута требования по вакансии
        :return:
        """
        return self.__requirement

    @property
    def experience(self):
        """
        Геттер для приватного атрибута требуемого опыта
        :return:
        """
        return self.__experience

    def __eq__(self, other):
        return self.__salary_from == other.__salary_from

    def __gt__(self, other):
        return self.__salary_from > other.__salary_from

    def __le__(self, other):
        return self.__salary_from <= other.__salary_from

    def dict_vacancy(self):
        vacancy = {
            "name_vacancy": self.__name_vac,
            "url_vacancy": self.__url_vac,
            "salary_from": self.__salary_from,
            "salary_to": self.__salary_to,
            "requirement": self.__requirement,
            "experience": self.__experience
        }
        return vacancy

    @classmethod
    def get_vac_hh(cls, vacancies_hh: dict | None):
        """
        Получаем вакансии из Head Hunter
        :param vacancies_hh: список вакансий, полученный через API
        :return: список объектов класса Vacancy
        """
        all_vacancies_hh = []
        vac_hh = vacancies_hh["items"]

        for params in vac_hh:
            name_hh = params["name"]
            if params["salary"] is not None:
                salary_from_hh = params["salary"]["from"]
                salary_to_hh = params["salary"]["to"]
            else:
                salary_from_hh = 0
                salary_to_hh = 0
            url_hh = params["alternate_url"]
            requirement_hh = params["snippet"]["requirement"]
            experience_hh = params["experience"]["name"]
            vacancy_hh = cls(name_hh, url_hh, salary_from_hh, salary_to_hh, requirement_hh, experience_hh)
            all_vacancies_hh.append(vacancy_hh)

        return all_vacancies_hh
