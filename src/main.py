import os
import re
from github import Github
from modules.crawl_module.CrawlFactory import CrawlFactory
from modules.query_module.QueryFactory import QueryFactory
from utils.ErrorHandler import post_error_comment

# Get environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
MOEL_COMPANY = os.getenv('MODEL_COMPANY')
FEW_SHOT_LEARNING = (os.getenv('FEW_SHOT_LEARNING').lower() == 'true')
API_KEY = os.getenv('API_KEY')
REPOSITORY = os.getenv('REPOSITORY')
PR_NUMBER = int(os.getenv('PR_NUMBER'))

# Initialize GitHub API
G = Github(GITHUB_TOKEN)
REPO = G.get_repo(REPOSITORY)
PR = REPO.get_pull(PR_NUMBER)

def extract_urls(commit_message):
    URL_PATTERN = r'(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))'
    urls = re.findall(URL_PATTERN, commit_message)
    return urls

def get_url_from_commit_message(pr):
    commits = pr.get_commits()
    latest_commit_message = list(commits)[-1].commit.message
    urls = [t[0] for t in extract_urls(latest_commit_message)]

    if len(urls) == 0:
        raise ValueError('ERR_NO_URL: commit message에 URL이 존재하지 않습니다.')
    elif len(urls) > 1:
        raise ValueError('ERR_MULTIPLE_URLS: commit message에 2개 이상의 URL이 존재합니다.')

    return urls[0]

def get_submitted_code(pr):
    submitted_codes = []
    commits = pr.get_commits()
    latest_commit = list(commits)[-1]
    
    for file in latest_commit.files:
        if file.filename.endswith(('.c', '.cpp', '.java', '.py')):
            submitted_codes.append(file)

    if len(submitted_codes) == 0:
        raise ValueError('ERR_SUBMITTED_CODES: 제출한 코드가 없습니다.')
    elif len(submitted_codes) > 1:
        raise ValueError('ERR_SUBMITTED_CODES: 제출한 코드가 2개 이상입니다.')
    
    return submitted_codes[0]

@post_error_comment(pr=PR)
def main():
    # Get submitted code
    submitted_code = get_submitted_code(PR)

    # Get problem_components from crawler
    url = get_url_from_commit_message(PR)
    crawler = CrawlFactory.create_crawler(url)
    problem_components = crawler.get_problem_description()

    # Get review from query
    query = QueryFactory.create_query(MOEL_COMPANY, API_KEY)
    review = query.optimize_after_review(submitted_code, problem_components, FEW_SHOT_LEARNING)

    # Post review comment
    PR.create_issue_comment(review)

if __name__ == "__main__":
    main()