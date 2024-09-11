import requests
from bs4 import BeautifulSoup
from .CrawlInterface import CrawlInterface

class CrawlBaekjoon(CrawlInterface):
    def get_problem_description(self):
        headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(self.url, headers=headers)

        if response.status_code != 200:
            raise ValueError(f"ERR_CRAWLING_ALGOSPOT: {self.url}과의 연결이 원할하지 않습니다.")

        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # PROBLEM_DESCRIPTION 찾기
        description_element = soup.find('div', id='problem_description')
        problem_description = description_element.text.strip() if description_element else 'Proplem description not found'

        # INPUT_DESCRIPTION 찾기
        input_element = soup.find('div', id='problem_input')
        input_description = input_element.text.strip() if input_element else 'Input description not found'

        # OUTPUT_DESCRIPTIO 찾기
        output_element = soup.find('div', id='problem_output')
        output_description = output_element.text.strip() if output_element else 'Output description not found'

        # INPUT_EXAMPLE 찾기
        input_example_element = soup.find('pre', id='sample-input-1')
        input_example = input_example_element.text.strip() if input_example_element else 'Input example not found'

        # OUTPUT_EXAMPLE 찾기
        output_example_element = soup.find('pre', id='sample-output-1')
        output_example = output_example_element.text.strip() if output_example_element else 'Output example not found'
        
        # 모든 정보를 하나의 문자열로 결합
        combined_text = f"""PROBLEM_DESCRIPTION:
        {problem_description}

        INPUT_DESCRIPTION:
        {input_description}

        OUTPUT_DESCRIPTION:
        {output_description}

        INPUT_EXAMPLE:
        {input_example}

        OUTPUT_EXAMPLE:
        {output_example}"""

        return combined_text
