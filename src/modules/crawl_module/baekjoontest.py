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
    
    # Find the problem title
    title_element = soup.find('span', id='problem_title')
    title = title_element.text if title_element else 'Title not found'

    # Find the problem description
    description_element = soup.find('div', id='problem_description')
    description = description_element.text.strip() if description_element else 'Description not found'

    # Find the input description
    input_element = soup.find('div', id='problem_input')
    input_description = input_element.text.strip() if input_element else 'Input description not found'

    # Find the output description
    output_element = soup.find('div', id='problem_output')
    output_description = output_element.text.strip() if output_element else 'Output description not found'

    return {
        "title": title,
        "description": description,
        "input": input_description,
        "output": output_description
    }

# 사용 예
url = 'https://www.acmicpc.net/problem/5073'
problem_info = get_baekjoon_problem(url)

if problem_info:
    print(f"Title: {problem_info['title']}")
    print(f"Description: {problem_info['description']}")
    print(f"Input: {problem_info['input']}")
    print(f"Output: {problem_info['output']}")
else:
    print("Failed to retrieve problem information.")