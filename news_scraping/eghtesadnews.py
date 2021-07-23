import re 
import requests
from bs4 import BeautifulSoup

class eghtesad_news():
    
    main_url = "https://www.eghtesadnews.com/%D8%A8%D8%AE%D8%B4-%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%A8%D9%88%D8%B1%D8%B3-38"

    request = requests.get(main_url)

    text = request.text

    page = BeautifulSoup(text, "html.parser")

    news_url = page.find_all("div", attrs={"class": "title"})

    news_urls = list()

    news_images = list()

    for i in range(0, 20):

        href= str(news_url[i])[29:].find("title")
        
        news_urls.append("https://www.eghtesadnews.com/{}".format(str(news_url[i])[29:href-4]))

        news_img = list(page.find_all("div", attrs={"class":"image"}))

        news_image_slice1 = str(news_img[i]).find("data-in-view")

        news_images.append(str(news_img[i])[news_image_slice1+48:-91])

    news_titles = list()
    
    news_date_times = list()

    news_leads = list()

    news_contents = list()

    news_links = list()

    for url in news_urls:
        
        news_request = requests.get(url)

        news_text = news_request.text

        news_page = BeautifulSoup(news_text, "html.parser")

        news_title = news_page.find("div", attrs={"class":"title"})

        news_date_time = news_page.find("time", attrs={"class":"news_time"})

        news_lead = news_page.find("div", attrs={"class":"lead"})

        news_content = news_page.find("div", attrs={"class":"innerbody"})

        news_titles.append(re.sub(r"\s+", ' ', news_title.text).strip())

        news_date_times.append(re.sub(r"\s+", ' ', news_date_time.text).strip())

        news_leads.append(re.sub(r"\s+", ' ', news_lead.text).strip())

        news_contents.append(re.sub(r"\s+", ' ', news_content.text).strip())

        news_links.append(url)

    @staticmethod
    def output():
        
        return eghtesad_news.news_date_times, eghtesad_news.news_titles, eghtesad_news.news_images, eghtesad_news.news_leads, eghtesad_news.news_contents, eghtesad_news.news_links
