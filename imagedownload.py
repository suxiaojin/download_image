from icrawler.builtin import BaiduImageCrawler
from icrawler.builtin import BingImageCrawler
from icrawler.builtin import GoogleImageCrawler

#goole_image
google_storage={'root_dir':'/Users/developer/image/toys/panda_google'}
google_crawler=GoogleImageCrawler(parser_threads=2,
                                  downloader_threads=2,
                                  storage=google_storage)
google_crawler.crawl(keyword='panda toy',
                     max_num=1000)


#bing_image
bing_storage={'root_dir':'/Users/developer/image/toys/panda_bing'}
bing_crawler=BingImageCrawler(parser_threads=2,
                              downloader_threads=2,
                              storage=bing_storage)
bing_crawler.crawl(keyword='panda toy',
                   max_num=1000)


#baidu_image
baidu_storage={'root_dir':'/Users/developer/image/toys/panda_baidu'}
baidu_crawler=BaiduImageCrawler(parser_threads=2,
                                downloader_threads=2,
                                storage=baidu_storage)
baidu_crawler.crawl(keyword='panda toy',
                    max_num=1000)

