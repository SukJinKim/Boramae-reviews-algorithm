import requests
import re
import html
from .CrawlInterface import CrawlInterface

class CrawlLeetCode(CrawlInterface):
    API_BASE_URL = "https://alfa-leetcode-api.onrender.com/select"

    @staticmethod
    def clean_html(raw_html):
        # HTML 태그와 엔티티 제거, 공백 정리를 한 번에 처리
        cleantext = re.sub(r'<.*?>', '', raw_html)
        cleantext = html.unescape(cleantext)
        cleantext = re.sub(r'\s+', ' ', cleantext).strip()
        cleantext = re.sub(r'\n\s*\n', '\n\n', cleantext)
        return cleantext

    def get_problem_description(self):
        title_slug = self.extract_title_slug()
        api_url = f"{self.API_BASE_URL}?titleSlug={title_slug}"

        try:
            response = requests.get(api_url)

            # HTTP 오류 발생 시 예외 발생 처리
            response.raise_for_status()

            # JSON 응답을 파이썬 딕셔너리로 변환
            data = response.json()

            # 'question' 키에서 문제 내용 추출
            question_content = data['question']
            
            return self.clean_html(question_content)
        except requests.RequestException as e:
            return f"Error fetching data: {e}"
        except (KeyError, IndexError, AttributeError) as e:
            return f"Error parsing data: {e}"

    def extract_title_slug(self):
        parts = self.url.rstrip('/').split('/')
        return parts[-2] if parts[-1] == 'description' else parts[-1]