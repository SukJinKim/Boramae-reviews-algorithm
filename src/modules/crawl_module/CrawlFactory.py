from urllib.parse import urlparse
from .CrawlLeetcode import CrawlLeetcode
from .CrawlProgrammers import CrawlProgrammers
from .CrawlAlgospot import CrawlAlgospot

class CrawlFactory:
    @staticmethod
    def create_crawler(url):
        domain = urlparse(url).netloc

        if domain == 'school.programmers.co.kr':
            return CrawlProgrammers(url)
        elif domain == 'algospot.com':
            return CrawlAlgospot(url)
        elif domain == 'leetcode.com':
            return CrawlLeetcode(url)
        else:
            raise ValueError("ERR_UNSUPPORTED_URL : 지원하는 사이트의 URL이 아닙니다.")
