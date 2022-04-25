import json
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4972.0 Safari/537.36"
}

url = f"https://senat.uz/ru/senators/index"
# q = requests.get(url, headers)
# # print(q.text)
#
# with open("senats.html", "w", encoding="utf8") as file:
#     file.write(q.text)

with open("senats.html", encoding="utf8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
articles = soup.find_all(class_="list-group-item")

persons_list_url = []
for article in articles:
    person_url = f"https://senat.uz" + article.get("href")
    persons_list_url.append(person_url)
# print(f"{persons_list_url}")








# alpthbet = ['А', 'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ч', 'Ш', 'Э', 'Ю']
# person_url_list = []
# for i in alpthbet:
#     url = f"https://parliament.gov.uz/ru/structure/deputy/?abs={i}"
#     # print(url)
#
#
#     q = requests.get(url, headers)
#     result = q.content
#
#     soup = BeautifulSoup(result, "lxml")
#     persons = soup.find_all(class_="col-md-10 col-xs-10").find_all("h5")
#
#     for person in persons:
#         person_page_url = person.get("href")
#         person_url_list.append(person_page_url)
#
#         print(person_url_list)
# with open("person_list.txt", 'a') as file:
#     for line in person_url_list:
#         file.write(f"{line}\n")
