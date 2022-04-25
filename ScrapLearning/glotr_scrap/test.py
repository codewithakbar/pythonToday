from bs4 import BeautifulSoup
import requests

url = "https://glotr.uz/search/?q=lg"
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

all_links = soup.find_all('a', class_='proposal-item-link')
for link in all_links:
    url = "https://glotr.uz" + link['href']
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")

    name = soup.find("div", class_="single-main-info").find("h1")
    # print(name.text)
    price = soup.find("div", class_="single-price").find("span").text
    # print(price)

    img = soup.find(class_="large-img-item slick-slide slick-current slick-active").get("href")
    print(img)



