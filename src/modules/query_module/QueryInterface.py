from abc import ABC, abstractmethod

class QueryInterface(ABC):
    def __init__(self, api_key):
        self.api_key = api_key

    @abstractmethod
    def extract_problem_components(self, problem_description):
        pass

    @abstractmethod
    def optimize_after_review(self, submitted_code, problem_components, few_shot_learning):
        pass