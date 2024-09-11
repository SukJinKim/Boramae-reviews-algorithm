import requests
from bs4 import BeautifulSoup

def get_baekjoon_problem(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # HTML 파싱
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error occurred while fetching the page: {e}")
        return None

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

    return {
        "PROBLEM_DESCRIPTION": problem_description,
        "INPUT_DESCRIPTION": input_description,
        "OUTPUT_DESCRIPTION": output_description,
        "INPUT_EXAMPLE": input_example,
        "OUTPUT_EXAMPLE": output_example
    }

# 사용 예
url = 'https://www.acmicpc.net/problem/19941'
problem_info = get_baekjoon_problem(url)

if problem_info:
    for key, value in problem_info.items():
        print(f"{key}:")
        print(value)
        print("-" * 50)  # 구분선 추가
else:
    print("문제 정보를 가져오는데 실패했습니다.")