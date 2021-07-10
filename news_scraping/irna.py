import re 
import requests 
from bs4 import BeautifulSoup


class irna_class():
	
	main_url = "https://www.irna.ir/service/economy/stockmarket"

	request = requests.get(main_url)

	text = request.text

	page = BeautifulSoup(text, "html.parser")

	news_url = page.find_all("h3")

	news_urls = list()

	for i in range(0, 10):

		href = str(news_url[i])[13:].find("target")

		news_urls.append("https://www.irna.ir{}".format(str(news_url[i])[13:href+11]))

	news_titles = list()

	news_date_times = list()

	news_images = list()

	news_leads = list()

	news_contents = list()

	news_links = list()

	for url in news_urls:

		news_request = requests.get(url)

		news_text = news_request.text

		news_page = BeautifulSoup(news_text, "html.parser")

		news_title = list(news_page.find_all("h1", attrs= {"class" : "title"}))

		news_date_time = list(news_page.find_all("div", attrs= {"class" : "item-date"}))

		news_img = list(news_page.find_all("img", attrs= {"itemprop" : "image"}))
	
		news_lead = list(news_page.find_all("p", attrs= {"itemprop" : "description"}))

		news_content = list(news_page.find_all("div", attrs= {"class" : "item-body"}))

		for news in range(0, len(news_title)):
			
			news_titles.append(news_title[news].text.strip())

			news_clean_datetime = re.sub(r"\s+", ' ', news_date_time[news].text).strip()
			
			news_date_times.append(re.sub(r"،", '', news_clean_datetime).strip())

			news_img_slice_1 = str(news_img).find("src")
			
			news_img_slice_2 = str(news_img).find("title")

			news_images.append(str(news_img)[news_img_slice_1+5:news_img_slice_2-2])

			news_leads.append(news_lead[news].text.strip())

			news_contents.append(news_content[news].text.strip())

			news_links.append(url)

	@staticmethod
	def output():

		return irna_class.news_date_times, irna_class.news_titles, irna_class.news_images, irna_class.news_leads, irna_class.news_contents, irna_class.news_links
