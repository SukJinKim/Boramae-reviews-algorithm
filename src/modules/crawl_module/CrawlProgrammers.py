import requests
from bs4 import BeautifulSoup
from .Crawl import Crawl

class CrawlProgrammers(Crawl):
    def get_problem(self):
        response = requests.get(self.url)

        if response.status_code != 200:
            raise ValueError(f"ERR_CRAWLING_PROGRAMMERS: {self.url}과의 연결이 원할하지 않습니다.")

        # HTML 파싱
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')

        # 문제 설명을 포함하는 CSS 클래스 이름
        problem_section_class = "guide-section"
        
        # 해당 클래스 이름을 가진 div 요소 찾기
        problem_section = soup.find("div", class_=problem_section_class)
        if problem_section:
            problem_description = problem_section.get_text(strip=True)
        else:
            raise ValueError("ERR_CRAWLING_PROGRAMMERS: 문제 설명 섹션을 찾을 수 없습니다.")
        
        return problem_description
