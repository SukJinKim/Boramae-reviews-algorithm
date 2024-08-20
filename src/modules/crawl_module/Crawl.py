from abc import ABC, abstractmethod

class Crawl(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get_problem(self):
        pass