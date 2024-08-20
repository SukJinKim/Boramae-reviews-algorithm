from modules.crawl_module.CrawlFactory import CrawlFactory
    

def main():
    url = "https://school.programmers.co.kr/learn/courses/30/lessons/118666"
    crawler = CrawlFactory.create_crawler(url)
    print(crawler.get_problem())

    print()

    url = "https://algospot.com/judge/problem/read/PI"
    crawler = CrawlFactory.create_crawler(url)
    print(crawler.get_problem())


if __name__ == "__main__":
    main()