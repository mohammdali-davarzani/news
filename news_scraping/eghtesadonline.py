import re 
import requests 
from bs4 import BeautifulSoup



class eghtesad_online():
	
	main_url = "https://www.eghtesadonline.com/%D8%A8%D8%AE%D8%B4-%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%A8%D9%88%D8%B1%D8%B3-%D9%81%D8%B1%D8%A7%D8%A8%D9%88%D8%B1%D8%B3-%D8%AA%D9%87%D8%B1%D8%A7%D9%86-%D8%B4%D8%A7%D8%AE%D8%B5-%D9%86%D9%85%D8%A7%D8%AF%D9%87%D8%A7%DB%8C-%D8%A8%D9%88%D8%B1%D8%B3%DB%8C-8"

	request = requests.get(main_url)

	text = request.text

	page = BeautifulSoup(text, "html.parser")

	news_url = page.find_all("h2", attrs= {"class" : "fnb fn17 clr04 pb8"})

	news_urls = list()

	for i in news_url:

		href = "https://www.eghtesadonline.com{}".format(str(i)[61:]).find("itemprop")

		news_urls.append("https://www.eghtesadonline.com{}".format(str(i)[61:href+29]))

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

		news_title = list(news_page.find_all("h1", attrs= {"class" : "pt8 pb8"}))

		news_date_time = list(news_page.find_all("time", attrs= {"class" : "fn12 clr02"}))

		news_img = list(news_page.find_all("img", attrs= {"class" : "w75 mauto block border10"}))

		news_lead = list(news_page.find_all("p", attrs= {"class" : "fn16 clr04 bg11 box-border05 pr16 pl16"}))

		news_content = list(news_page.find_all("div", attrs= {"class" : "content-inner clear-both"}))

		
		for n in range(0, len(news_title)):
			
			news_titles.append(news_title[n].text.strip())
			news_date_times.append(news_date_time[n].text.strip())
			print(news_img[n])
			print("\n")




