from abc import ABC, abstractmethod

class CrawlInterface(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get_problem_description(self):
        pass