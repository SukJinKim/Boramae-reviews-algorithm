from urllib.parse import urlparse
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
        else:
            raise ValueError("Unsupported URL")
