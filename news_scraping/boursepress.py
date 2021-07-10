import re 
import requests 
from bs4 import BeautifulSoup


class bourse_press():

	main_url = "http://boursepress.ir/"

	request = requests.get(main_url)

	text = request.text

	page = BeautifulSoup(text, "html.parser")

	news_url = page.find_all("a", attrs= {"class" : "news-list-title-icon"})

	news_urls = list()

	for i in news_url[0:15]:

		href= str(i)[38:].find("target")

		news_urls.append(str(i)[38:href+36])

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

		news_title = list(news_page.find_all("h1"))

		news_date_time = list(news_page.find_all("div", attrs= {"style" : " position: absolute; left: 240px; "}))

		news_img = list(news_page.find_all("div", attrs= {"class" : "news-img"}))

		news_lead = list(news_page.find_all("div", attrs= {"class" : "news-lead"}))

		news_content = list(news_page.find_all("div", attrs= {"class" : "news-text"}))

		for i in range(0, len(news_title)):

			news_titles.append(re.sub(r"\s+", ' ', news_title[i].text).strip())

			news_clean_datetime = re.sub(r"\s+", ' ', news_date_time[i].text).strip()

			news_date_times.append(re.sub(r"-", '', news_clean_datetime).strip())

			news_image_src = str(news_img)[:-10].find("src")

			news_images.append(str(news_img)[news_image_src+5:-10])

			news_leads.append(re.sub(r"\s+", ' ', news_lead[i].text).strip())

			news_contents.append(re.sub(r"\s+", ' ', news_content[i].text).strip())

			news_links.append(url)

	@staticmethod
	def output():

		return bourse_press.news_date_times, bourse_press.news_titles, bourse_press.news_images, bourse_press.news_leads, bourse_press.news_contents, bourse_press.news_links

