import requests
import json
from bs4 import BeautifulSoup
import re

def clean_html(raw_html):
    # Remove HTML tags
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    # Replace HTML entities
    cleantext = re.sub('&nbsp;', ' ', cleantext)
    cleantext = re.sub('&quot;', '"', cleantext)
    cleantext = re.sub('&lt;', '<', cleantext)
    cleantext = re.sub('&gt;', '>', cleantext)
    # Remove extra whitespace
    cleantext = re.sub(r'\s+', ' ', cleantext).strip()
    return cleantext

def extract_leetcode_problem_description(problem_url):
    # Extract the titleSlug from the URL
    title_slug = problem_url.split('/')[-2]
    
    # Construct the API URL
    api_url = f"https://alfa-leetcode-api.onrender.com/select?titleSlug={title_slug}"
    
    try:
        # Make the API request
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()
        
        # Extract the question content
        question_content = data['question']
        
        # Clean the HTML co
        # ntent
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