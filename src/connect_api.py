import requests
import os
from abc import ABC, abstractmethod


class ConnectAPI(ABC):

    @abstractmethod
    def get_vacancies(self, search: str):
        pass


class HeadHunterAPI(ConnectAPI):

    def __init__(self, url: str = "https://api.hh.ru/vacancies/"):
        self.url = url

    def get_vacancies(self, search):
        params = {"text": search,
                  "area": 113,
                  "per_page": 100}
        response = requests.get(self.url, params=params).json()
        return response


class SuperJobAPI(ConnectAPI):

    def __init__(self, url: str = "https://api.superjob.ru/2.0/vacancies/"):
        self.url = url

    def get_vacancies(self, search):
        api_super_job = os.getenv('TOKEN_API_SUPERJOB')
        headers = {"X-Api-App-Id": api_super_job}
        params = {
            'POST': '/2.0/vacancies/',
            'Host': 'api.superjob.ru',
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded',
            'keywords': search,
            'c': 1
        }

        response = requests.get(self.url, headers=headers, params=params).json()
        return response
