import requests
import json
from bs4 import BeautifulSoup
import re
import html

def clean_html(raw_html):
    # HTML tag 제거
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    
    # HTML 엔티티를 일반 문자로 변환
    cleantext = html.unescape(cleantext)
    
    # 연속된 공백 제거 및 줄바꿈 처리
    cleantext = re.sub(r'\s+', ' ', cleantext).strip()
    cleantext = re.sub(r'\n\s*\n', '\n\n', cleantext)
    
    return cleantext

def extract_leetcode_problem_description(problem_url):
    # url에서 title 추출(description으로 끝나는 경우도 처리)
    title_slug = problem_url.rstrip('/').split('/')[-1]
    if title_slug == 'description':
        title_slug = problem_url.rstrip('/').split('/')[-2]
    
    # API URL 생성
    api_url = f"https://alfa-leetcode-api.onrender.com/select?titleSlug={title_slug}"
    
    try:
        # API request 요청
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        
        # Extract the question content
        question_content = data['question']
        
        # Clean the HTML content
        clean_description = clean_html(question_content)
        
        return clean_description
    
    except requests.RequestException as e:
        return f"Error fetching data: {e}"
    except (KeyError, IndexError, AttributeError) as e:
        return f"Error parsing data: {e}"

# Example usage
problem_url = "https://leetcode.com/problems/binary-tree-maximum-path-sum/"
problem_description = extract_leetcode_problem_description(problem_url)
print(problem_description)