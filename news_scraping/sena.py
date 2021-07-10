import re
import requests
from bs4 import BeautifulSoup


class sena_class():

    main_url = "https://www.sena.ir/service/capital"

    link = requests.get(main_url)

    text = link.text

    page = BeautifulSoup(text, "html.parser")

    news_url = page.find_all("h3")

    news_urls = list()

    for i in range(5, 30):
        
        href = str(news_url[i])[7:].find("target")
        
        news_urls.append("https://www.sena.ir{}".format(str(news_url[i])[13:href+5]))

    news_titles = list()
    
    news_date_times = list()

    news_images = list()

    news_leads = list()

    news_contents = list()

    news_links = list()

    for url in news_urls:

        news_link = requests.get(url)

        news_text = news_link.text

        news_page = BeautifulSoup(news_text, "html.parser")

        news_title = list(news_page.find_all("h1", attrs={"class":"title", "itemprop":"headline"}))
        
        news_date_time = list(news_page.find_all("div", attrs={"class": "col-xs-8 col-sm-5 item-date"}))
        
        news_img = list(news_page.find_all("img", attrs={"itemprop": "image"}))
        
        news_lead = list(news_page.find_all("p", attrs={"class" : "summary introtext", "itemprop": "description"}))
        
        news_content = list(news_page.find_all("div", attrs={"class":"item-text", "itemprop":"articleBody"}))

        for j in range(1, len(news_title)):

            news_titles.append(news_title[j].text)
            
            news_clean_datetime = re.sub(r"\s+", ' ', news_date_time[j].text).strip()
            
            news_date_times.append(re.sub(r"-", '', news_clean_datetime).strip())

            news_image_slice_1 = str(news_img[j]).find("src")
            
            news_image_slice_2 = str(news_img[j]).find("title")
            
            news_images.append(str(news_img[j])[news_image_slice_1+5:news_image_slice_2-2])

            news_leads.append(news_lead[j].text.strip())
            
            news_contents.append(news_content[j].text.strip())

            news_links.append(url)

    @staticmethod
    def output():
        
        return sena_class.news_date_times, sena_class.news_titles, sena_class.news_images, sena_class.news_leads, sena_class.news_contents, sena_class.news_links

