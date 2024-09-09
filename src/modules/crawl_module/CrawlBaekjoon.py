import requests
from bs4 import BeautifulSoup
from .CrawlInterface import CrawlInterface

class CrawlBaekjoon(CrawlInterface):
    def get_problem_description(self):
        response = requests.get(self.url)

        if response.status_code != 200:
            raise ValueError(f"ERR_CRAWLING_ALGOSPOT: {self.url}과의 연결이 원할하지 않습니다.")

        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 문제 정보의 각 섹션을 선택할 CSS 셀렉터들
        problem_section_selectors = [
            "section.problem_info",
            "section.problem_statement",
            "section.problem_input",
            "section.problem_output",
            "section.problem_sample_input",
            "section.problem_sample_output"
        ]

        problem_details = []
        for selector in problem_section_selectors:
            element = soup.select_one(selector)
            if element:
                problem_details.append(element.get_text(strip=True))
        
        if problem_details:
            problem_description = "\n".join(problem_details)
        else:
            raise ValueError("ERR_CRAWLING_ALGOSPOT: 문제 정보를 찾을 수 없습니다.")
        
        return problem_description
