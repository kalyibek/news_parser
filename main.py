import requests
import json
from bs4 import BeautifulSoup
from model import New


URL_MAIN = "https://newsline.kg/"
URL_SOCIETY = "https://newsline.kg/society"
URL_POLITICS = "https://newsline.kg/politics"
URL_ECONOMICS = "https://newsline.kg/economics"
URL_INCIDENTS = "https://newsline.kg/incidents"
URL_SPORT = "https://newsline.kg/sport"
URL_BUSINESS = "https://newsline.kg/business"

request = requests.get(URL_MAIN)
request_society = requests.get(URL_SOCIETY)
request_politics = requests.get(URL_POLITICS)
request_economics = requests.get(URL_ECONOMICS)
request_incidents = requests.get(URL_INCIDENTS)
request_sport = requests.get(URL_SPORT)
request_business = requests.get(URL_BUSINESS)

soup = BeautifulSoup(request.text, 'html.parser')
soup_society = BeautifulSoup(request_society.text, 'html.parser')
soup_politics = BeautifulSoup(request_politics.text, 'html.parser')
soup_economics = BeautifulSoup(request_economics.text, 'html.parser')
soup_incidents = BeautifulSoup(request_incidents.text, 'html.parser')
soup_sport = BeautifulSoup(request_sport.text, 'html.parser')
soup_business = BeautifulSoup(request_business.text, 'html.parser')

news_info = soup.find_all('div', class_='col s12 m8 offset-m2 l6 offset-l3 media')
news_content = soup.find_all('div', class_='modal-content')

titles = soup.find_all('div', class_='title')
titles_society = soup_society.find_all('div', class_='title')
titles_politics = soup_politics.find_all('div', class_='title')
titles_economics = soup_economics.find_all('div', class_='title')
titles_incidents = soup_incidents.find_all('div', class_='title')
titles_sport = soup_sport.find_all('div', class_='title')
titles_business = soup_business.find_all('div', class_='title')

categories = soup.find_all('a', class_='category')
result = []

for i in range(len(news_content)):

    id = news_info[i]['target'][5:]
    date = news_info[i]['id']
    category = None
    title = titles[i]
    link = news_content[i].find_next('div', class_='resource-link-block').a['href']
    description = news_content[i].find_all('p')
    if news_content[i].find('div', class_='modal_img'):
        img = news_content[i].find('div', class_='modal_img').img['src']
    else:
        img = None

    if title in titles_society:
        category = 'Общество'
    elif title in titles_politics:
        category = 'Политика'
    elif title in titles_economics:
        category = 'Экономика'
    elif title in titles_incidents:
        category = 'Проишествия'
    elif title in titles_sport:
        category = 'Спорт'
    elif title in titles_business:
        category = 'Бизнес'

    news_object = New(id, date, category, title.text, link, description, img)
    result.append(
        {
            'id': news_object.id,
            'date': news_object.date,
            'category': news_object.category,
            'title': news_object.title,
            'link': news_object.link,
            'desc': news_object.desc,
            'img': news_object.img,
            'site_name': news_object.site_name
        }
    )

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)
